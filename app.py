from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
from datetime import datetime
from database import Database

app = Flask(__name__, static_folder='.')
CORS(app)

# Inicializar base de datos
db = Database('testing.db')

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
        sin_ejecutar = int(datos.get('sin_ejecutar', 0))
        mensaje = datos.get('mensaje', '')
        
        # Validar que la suma no supere el total
        suma = bloqueados + en_curso + finalizados + sin_ejecutar
        if suma > total:
            return jsonify({
                'error': f'La suma ({suma}) supera el total de casos ({total})'
            }), 400
        
        # Calcular porcentajes
        reporte = {
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
        
        # Guardar en base de datos
        reporte_id = db.crear_reporte(reporte)
        reporte['id'] = reporte_id
        
        return jsonify(reporte), 201
    
    except Exception as e:
        return jsonify({'error': str(e)}), 400

@app.route('/api/reportes', methods=['GET'])
def listar_reportes():
    try:
        reportes = db.listar_reportes()
        return jsonify(reportes)
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/reporte/<int:id>', methods=['GET'])
def obtener_reporte(id):
    try:
        reporte = db.obtener_reporte(id)
        if reporte:
            return jsonify(reporte)
        return jsonify({'error': 'Reporte no encontrado'}), 404
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/reporte/<int:id>', methods=['PUT'])
def actualizar_reporte(id):
    try:
        datos = request.get_json()
        
        total = int(datos.get('total_casos', 0))
        bloqueados = int(datos.get('bloqueados', 0))
        en_curso = int(datos.get('en_curso', 0))
        finalizados = int(datos.get('finalizados', 0))
        sin_ejecutar = int(datos.get('sin_ejecutar', 0))
        
        suma = bloqueados + en_curso + finalizados + sin_ejecutar
        if suma > total:
            return jsonify({
                'error': f'La suma ({suma}) supera el total de casos ({total})'
            }), 400
        
        reporte = {
            'titulo': datos.get('titulo', 'Reporte de Avance de Testing'),
            'total_casos': total,
            'bloqueados': bloqueados,
            'en_curso': en_curso,
            'finalizados': finalizados,
            'sin_ejecutar': sin_ejecutar,
            'mensaje': datos.get('mensaje', ''),
            'porcentajes': {
                'bloqueados': round((bloqueados / total) * 100, 2) if total > 0 else 0,
                'en_curso': round((en_curso / total) * 100, 2) if total > 0 else 0,
                'finalizados': round((finalizados / total) * 100, 2) if total > 0 else 0,
                'sin_ejecutar': round((sin_ejecutar / total) * 100, 2) if total > 0 else 0
            }
        }
        
        if db.actualizar_reporte(id, reporte):
            return jsonify({'message': 'Reporte actualizado'}), 200
        return jsonify({'error': 'Reporte no encontrado'}), 404
    
    except Exception as e:
        return jsonify({'error': str(e)}), 400

@app.route('/api/reporte/<int:id>', methods=['DELETE'])
def eliminar_reporte(id):
    try:
        if db.eliminar_reporte(id):
            return jsonify({'message': 'Reporte eliminado'}), 200
        return jsonify({'error': 'Reporte no encontrado'}), 404
    except Exception as e:
        return jsonify({'error': str(e)}), 500
import os

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=False, host='0.0.0.0', port=port)



## if __name__ == '__main__':
##    app.run(debug=True, port=5000)

