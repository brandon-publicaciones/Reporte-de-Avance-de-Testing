import sqlite3
from datetime import datetime
import os

class Database:
    def __init__(self, db_path='testing.db'):
        self.db_path = db_path
        self.init_db()
    
    def get_connection(self):
        conn = sqlite3.connect(self.db_path)
        conn.row_factory = sqlite3.Row  # Para acceder a columnas por nombre
        return conn
    
    def init_db(self):
        """Crear las tablas si no existen"""
        conn = self.get_connection()
        cursor = conn.cursor()
        
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS reportes (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                titulo TEXT NOT NULL,
                fecha_generacion TEXT NOT NULL,
                total_casos INTEGER NOT NULL,
                bloqueados INTEGER NOT NULL,
                en_curso INTEGER NOT NULL,
                finalizados INTEGER NOT NULL,
                sin_ejecutar INTEGER NOT NULL,
                mensaje TEXT,
                porcentaje_bloqueados REAL,
                porcentaje_en_curso REAL,
                porcentaje_finalizados REAL,
                porcentaje_sin_ejecutar REAL
            )
        ''')
        
        conn.commit()
        conn.close()
        print(f"✅ Base de datos inicializada: {self.db_path}")
    
    def crear_reporte(self, datos):
        """Insertar un nuevo reporte"""
        conn = self.get_connection()
        cursor = conn.cursor()
        
        cursor.execute('''
            INSERT INTO reportes (
                titulo, fecha_generacion, total_casos, 
                bloqueados, en_curso, finalizados, sin_ejecutar,
                mensaje, porcentaje_bloqueados, porcentaje_en_curso,
                porcentaje_finalizados, porcentaje_sin_ejecutar
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        ''', (
            datos['titulo'],
            datos['fecha_generacion'],
            datos['total_casos'],
            datos['bloqueados'],
            datos['en_curso'],
            datos['finalizados'],
            datos['sin_ejecutar'],
            datos['mensaje'],
            datos['porcentajes']['bloqueados'],
            datos['porcentajes']['en_curso'],
            datos['porcentajes']['finalizados'],
            datos['porcentajes']['sin_ejecutar']
        ))
        
        reporte_id = cursor.lastrowid
        conn.commit()
        conn.close()
        return reporte_id
    
    def listar_reportes(self):
        """Obtener todos los reportes"""
        conn = self.get_connection()
        cursor = conn.cursor()
        
        cursor.execute('SELECT * FROM reportes ORDER BY id DESC')
        reportes = [dict(row) for row in cursor.fetchall()]
        
        conn.close()
        return reportes
    
    def obtener_reporte(self, reporte_id):
        """Obtener un reporte por ID"""
        conn = self.get_connection()
        cursor = conn.cursor()
        
        cursor.execute('SELECT * FROM reportes WHERE id = ?', (reporte_id,))
        row = cursor.fetchone()
        
        conn.close()
        if row:
            return dict(row)
        return None
    
    def eliminar_reporte(self, reporte_id):
        """Eliminar un reporte"""
        conn = self.get_connection()
        cursor = conn.cursor()
        
        cursor.execute('DELETE FROM reportes WHERE id = ?', (reporte_id,))
        deleted = cursor.rowcount
        
        conn.commit()
        conn.close()
        return deleted > 0
    
    def actualizar_reporte(self, reporte_id, datos):
        """Actualizar un reporte existente"""
        conn = self.get_connection()
        cursor = conn.cursor()
        
        cursor.execute('''
            UPDATE reportes SET
                titulo = ?, total_casos = ?, 
                bloqueados = ?, en_curso = ?, 
                finalizados = ?, sin_ejecutar = ?,
                mensaje = ?, porcentaje_bloqueados = ?,
                porcentaje_en_curso = ?, porcentaje_finalizados = ?,
                porcentaje_sin_ejecutar = ?
            WHERE id = ?
        ''', (
            datos['titulo'],
            datos['total_casos'],
            datos['bloqueados'],
            datos['en_curso'],
            datos['finalizados'],
            datos['sin_ejecutar'],
            datos['mensaje'],
            datos['porcentajes']['bloqueados'],
            datos['porcentajes']['en_curso'],
            datos['porcentajes']['finalizados'],
            datos['porcentajes']['sin_ejecutar'],
            reporte_id
        ))
        
        updated = cursor.rowcount
        conn.commit()
        conn.close()
        return updated > 0
