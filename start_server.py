#!/usr/bin/env python3
"""
Script para iniciar el servidor web integrado de Transporte Serrano del Oriente
Ejecuta tanto el backend Flask como sirve el frontend desde una sola aplicación
"""

import sys
import os
import subprocess
from pathlib import Path

# Agregar el directorio backend al path para imports
backend_dir = Path(__file__).parent / 'backend'
sys.path.insert(0, str(backend_dir))
# También agregar el directorio raíz para imports relativos
root_dir = Path(__file__).parent
sys.path.insert(0, str(root_dir))

def check_requirements():
    """Verificar si están instaladas las dependencias"""
    try:
        import flask
        import flask_cors
        import mysql.connector
        print("✓ Todas las dependencias están instaladas")
        return True
    except ImportError as e:
        print(f"✗ Falta instalar dependencias: {e}")
        print("Ejecute: pip install -r backend/requirements.txt")
        return False

def start_server():
    """Iniciar el servidor web integrado"""
    print("=" * 60)
    print("TRANSPORTE SERRANO DEL ORIENTE")
    print("Sistema Web Integrado")
    print("=" * 60)
    
    if not check_requirements():
        return False
    
    # Cambiar al directorio backend para importar módulos correctamente
    os.chdir(backend_dir)
    
    try:
        # Importar y crear la aplicación
        from app import create_app
        
        app = create_app()
        
        print("\n🚀 Iniciando servidor web integrado...")
        print("📱 Frontend: Página web completa")
        print("🔧 Backend: API REST + Base de datos")
        print(f"🌐 URL: http://localhost:5000")
        print(f"🏠 Página principal: http://localhost:5000/")
        print(f"💰 Módulo Ventas: http://localhost:5000/ventas")
        print(f"⚕️ Estado del sistema: http://localhost:5000/api/health")
        print("\nPresione Ctrl+C para detener el servidor")
        print("-" * 60)
        
        # Iniciar el servidor
        app.run(
            host='0.0.0.0',
            port=5000,
            debug=True,
            use_reloader=False
        )
        
    except ImportError as e:
        print(f"✗ Error importando módulos: {e}")
        print("Verifique que esté en el directorio correcto del proyecto")
        return False
    except Exception as e:
        print(f"✗ Error iniciando servidor: {e}")
        return False
    
    return True

if __name__ == '__main__':
    try:
        start_server()
    except KeyboardInterrupt:
        print("\n\n👋 Servidor detenido por el usuario")
        sys.exit(0)
    except Exception as e:
        print(f"\n✗ Error inesperado: {e}")
        sys.exit(1)
