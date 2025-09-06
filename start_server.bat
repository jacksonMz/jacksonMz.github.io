@echo off
title Transporte Serrano del Oriente - Servidor Web

echo ============================================================
echo TRANSPORTE SERRANO DEL ORIENTE
echo Sistema de Gestion de Pasajeros - WEB INTEGRADO
echo ============================================================
echo.

REM Verificar si Python está instalado
python --version >nul 2>&1
if errorlevel 1 (
    echo ERROR: Python no esta instalado o no esta en el PATH
    echo Instale Python desde https://python.org
    pause
    exit /b 1
)

REM Cambiar al directorio del proyecto
cd /d "%~dp0"

echo Verificando dependencias...
python -c "import flask, flask_cors, mysql.connector" 2>nul
if errorlevel 1 (
    echo Instalando dependencias...
    pip install -r backend\requirements.txt
)

echo.
echo 🚀 Iniciando servidor web integrado...
echo 📱 Frontend + Backend + Base de Datos
echo 🌐 URL: http://localhost:5000
echo 💰 Ventas: http://localhost:5000/ventas
echo ⚙️ API Health: http://localhost:5000/api/health
echo.
echo Usuarios por defecto:
echo   - admin / secret123 (Administrador)
echo   - vendedor1 / secret123 (Vendedor)
echo.
echo ============================================================
echo Presione Ctrl+C para detener el servidor
echo ============================================================

REM Cambiar al directorio backend y ejecutar
cd backend
python app.py

echo.
echo Servidor detenido.
pause
