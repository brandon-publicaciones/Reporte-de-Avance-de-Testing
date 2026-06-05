from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
from datetime import datetime

app = Flask(__name__, static_folder='.')
CORS(app)

reportes = []

@app.route('/')
def index():
    return send_from_directory('.', 'index.html')

@app.route('/api/reporte', methods=['POST'])
def crear_reporte():
    try:
        datos = request.get_json()
        
        total = int(datos.get('total_casos', 0))
        bloqueados = int(datos.get('bloqueados', 0))
        en_curso = int(datos.get('en_curso', 0))
        finalizados = int(datos.get('finalizados', 0))
        mensaje = datos.get('mensaje', '')
        
        suma = bloqueados + en_curso + finalizados
        if suma > total:
            return jsonify({
                'error': f'La suma ({suma}) supera el total de casos ({total})'
            }), 400
        
        sin_ejecutar = total - suma
        
        reporte = {
            'id': len(reportes) + 1,
            'titulo': datos.get('titulo', 'Reporte de Avance de Testing'),
            'fecha_generacion': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            'fecha_corta': datetime.now().strftime('%d/%m/%Y'),
            'total_casos': total,
            'bloqueados': bloqueados,
            'en_curso': en_curso,
            'finalizados': finalizados,
            'sin_ejecutar': sin_ejecutar,
            'mensaje': mensaje,
            'porcentajes': {
                'bloqueados': round((bloqueados / total) * 100, 2) if total > 0 else 0,
                'en_curso': round((en_curso / total) * 100, 2) if total > 0 else 0,
                'finalizados': round((finalizados / total) * 100, 2) if total > 0 else 0,
                'sin_ejecutar': round((sin_ejecutar / total) * 100, 2) if total > 0 else 0
            }
        }
        
        reportes.append(reporte)
        return jsonify(reporte), 201
    
    except Exception as e:
        return jsonify({'error': str(e)}), 400

@app.route('/api/reportes', methods=['GET'])
def listar_reportes():
    return jsonify(reportes)

@app.route('/api/reporte/<int:id>', methods=['GET'])
def obtener_reporte(id):
    reporte = next((r for r in reportes if r['id'] == id), None)
    if reporte:
        return jsonify(reporte)
    return jsonify({'error': 'Reporte no encontrado'}), 404

if __name__ == '__main__':
    app.run(debug=True, port=5000)
