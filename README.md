# TRANSPORTE SERRANO DEL ORIENTE
## Sistema Web Multiplataforma para Gestión y Control de Pasajeros

![Version](https://img.shields.io/badge/version-1.0.0-blue.svg)
![Status](https://img.shields.io/badge/status-En%20desarrollo-yellow.svg)
![License](https://img.shields.io/badge/license-Privado-red.svg)

---

## 📋 Descripción del Proyecto

Sistema web multiplataforma con base de datos centralizada desarrollado para optimizar la venta y reserva de pasajes, el control de pasajeros en tramos intermedios, el registro de menores de edad y la generación de reportes confiables para la gestión administrativa de la Flota Serrano del Oriente.

---

## 🎯 Objetivos

### Objetivo General
Desarrollar un sistema web multiplataforma con base de datos centralizada que permita optimizar la venta y reserva de pasajes, el control de pasajeros en tramos intermedios, el registro de menores de edad y la generación de reportes confiables para la gestión administrativa de la Flota Serrano del Oriente.

### Objetivos Específicos
- **RF-01:** Analizar los procesos actuales de registro, venta y control de pasajes
- **RF-02:** Diseñar una base de datos centralizada eficiente
- **RF-03:** Implementar un sistema web multiplataforma
- **RF-04:** Integrar módulos de seguridad con gestión de roles
- **RF-05:** Generar reportes automatizados parametrizados

---

## ⚡ Requerimientos Funcionales

| ID | Descripción |
|----|----|
| **RF-01** | Autenticación de Usuario |
| **RF-02** | Gestión de Roles |
| **RF-03** | Gestión de Rutas y Tramos |
| **RF-04** | Programación de Salidas |
| **RF-05** | Registro de Pasajeros Adultos |
| **RF-06** | Consulta de Disponibilidad |
| **RF-07** | Reserva de Asiento |
| **RF-08** | Confirmación de Pago |
| **RF-09** | Emisión de Boleto |
| **RF-10** | Generación de Lista de Pasajeros |

---

## 🔧 Requerimientos No Funcionales

| ID | Descripción | Especificación |
|----|----|----|
| **RNF-01** | Rendimiento | 500 transacciones simultáneas con 2 seg de respuesta |
| **RNF-02** | Seguridad | Cifrado de contraseñas, roles RBAC, HTTPS y VPN |
| **RNF-03** | Disponibilidad | Uptime ≥ 99%, incluso en horas pico |
| **RNF-04** | Portabilidad | Accesible desde web y apps móviles Android/iOS |
| **RNF-05** | Confiabilidad | Transacciones ACID y control de concurrencia |
| **RNF-06** | Recuperación | Backups automáticos y restauración en < 2 horas |

---

## 🏗️ Arquitectura del Sistema

### Arquitectura 3 Capas + Screaming Architecture por Dominio

```
TRANSPORTE SERRANO DEL ORIENTE/
├── backend/                    # API Backend (Python Flask)
│   ├── config/                # Configuración global
│   ├── shared/                # Utilidades compartidas
│   ├── auth/                  # Dominio: Autenticación
│   │   ├── repository/        # Capa de datos
│   │   ├── service/          # Lógica de negocio
│   │   └── routes/           # Capa de presentación
│   ├── pasajeros/            # Dominio: Pasajeros
│   ├── ventas/               # Dominio: Ventas
│   ├── buses/                # Dominio: Buses
│   ├── choferes/             # Dominio: Choferes
│   ├── rutas/                # Dominio: Rutas
│   └── reportes/             # Dominio: Reportes
├── frontend/                   # Interfaz de Usuario
│   ├── assets/               # Recursos estáticos
│   ├── components/           # Componentes reutilizables
│   ├── pages/                # Páginas por módulo
│   ├── services/             # Servicios de API
│   └── utils/                # Utilidades
└── data/                      # Base de Datos
    └── database_complete.sql  # Schema completo
```

---

## 💻 Tecnologías Utilizadas

### Backend
- **Lenguaje:** Python 3.9+
- **Framework:** Flask 2.3.3
- **Base de Datos:** MySQL 8.0
- **Conector:** mysql-connector-python (sin ORM)

### Frontend  
- **Lenguaje:** JavaScript ES6+
- **Estructura:** HTML5
- **Estilos:** CSS3 + Bootstrap 5
- **Framework:** Vanilla JavaScript (SPA)

### Base de Datos
- **SGBD:** MySQL 8.0
- **Características:** 
  - Procedimientos almacenados
  - Triggers
  - Funciones personalizadas
  - Transacciones ACID

---

## 🚀 SERVIDOR WEB INTEGRADO

### ✨ Novedad: Una Sola Aplicación Web
El sistema ahora funciona como **una aplicación web integrada** donde Flask sirve tanto el backend como el frontend desde una sola URL.

### Prerrequisitos
- Python 3.9 o superior
- MySQL 8.0 o superior (XAMPP recomendado)
- Navegador web moderno

### Pasos de Instalación

#### 1. Preparar el proyecto
```bash
# Navegar al directorio del proyecto
cd "TRANSPORTE SERRANO DEL ORIENTE"
```

#### 2. Configurar Base de Datos
```bash
# En phpMyAdmin o cliente MySQL:
# Importar el archivo: data/database_complete.sql
```

#### 3. Instalar dependencias
```bash
cd backend
pip install -r requirements.txt
cp .env.example .env
# Editar .env con sus credenciales de MySQL
```

#### 4. 🎉 Ejecutar el Sistema Integrado

**Opción 1: Script de inicio (Recomendado)**
```bash
python start_server.py
```

**Opción 2: Windows (Batch)**
```cmd
start_server.bat
```

**Opción 3: Comando directo**
```bash
cd backend
python app.py
```

### 🌐 Acceso al Sistema

- **🏠 Sistema completo**: http://localhost:5000
- **📊 Dashboard**: http://localhost:5000/dashboard  
- **🔧 API REST**: http://localhost:5000/api/*
- **⚕️ Estado del sistema**: http://localhost:5000/api/health

### 🎯 Ventajas del Servidor Integrado

- ✅ **Una sola URL**: Todo desde http://localhost:5000
- ✅ **Sin CORS**: Elimina problemas de cross-origin
- ✅ **Despliegue simple**: Un solo comando para iniciar todo
- ✅ **SPA integrada**: Navegación fluida sin recargas
- ✅ **Menos configuración**: No necesita servidor web separado

---

## 👥 Usuarios por Defecto

| Usuario | Password | Rol | Descripción |
|----|----|----|----| 
| `admin` | `secret123` | Administrador | Acceso completo al sistema |
| `vendedor1` | `secret123` | Vendedor | Ventas y gestión de pasajeros |
| `chofer1` | `secret123` | Chofer | Visualización de salidas |

> ⚠️ **Importante:** Cambiar las contraseñas por defecto en producción

---

## 📊 Funcionalidades Principales

### 🔐 Autenticación y Seguridad
- Login con validación de credenciales
- Gestión de roles y permisos (RBAC)
- Sesiones seguras con timeout
- Cifrado de contraseñas

### 🎫 Gestión de Ventas
- Consulta de disponibilidad en tiempo real
- Reserva y confirmación de asientos
- Emisión de boletos digitales
- Control de tramos intermedios

### 👥 Gestión de Pasajeros
- Registro de pasajeros adultos y menores
- Validación de documentos de identidad
- Historial de viajes
- Formularios especiales para menores

### 🚌 Gestión Operativa
- Administración de buses y asientos
- Control de choferes y licencias
- Programación de rutas y salidas
- Gestión de oficinas intermedias

### 📈 Reportes y Analytics
- Reportes de ventas por fecha/ruta/bus
- Estadísticas de ocupación
- Control de ingresos
- Exportación en múltiples formatos

---

## 🛠️ API Endpoints

### Autenticación
- `POST /api/auth/login` - Iniciar sesión
- `POST /api/auth/logout` - Cerrar sesión
- `GET /api/auth/profile` - Obtener perfil de usuario

### Ventas
- `GET /api/ventas` - Listar ventas
- `POST /api/ventas` - Crear nueva venta
- `GET /api/ventas/disponibilidad` - Consultar disponibilidad

### Pasajeros
- `GET /api/pasajeros` - Listar pasajeros
- `POST /api/pasajeros` - Registrar pasajero
- `PUT /api/pasajeros/:id` - Actualizar pasajero

### Reportes
- `GET /api/reportes/ventas-fecha` - Reporte de ventas por fecha
- `GET /api/reportes/ocupacion` - Reporte de ocupación

---

## 🔒 Seguridad

### Medidas Implementadas
- ✅ Autenticación por sesiones
- ✅ Control de acceso basado en roles (RBAC)
- ✅ Validación de entrada de datos
- ✅ Protección contra SQL Injection
- ✅ Cifrado de contraseñas (SHA-256)
- ✅ Logging de auditoría
- ✅ Timeout de sesiones

### Recomendaciones para Producción
- Implementar HTTPS
- Usar bcrypt para contraseñas
- Configurar firewall y VPN
- Monitoreo de logs de seguridad
- Backups encriptados

---

## 🧪 Testing

```bash
# Pruebas y scripts ahora están en scripts/testing/

# Ejemplos de ejecución directa de scripts de prueba
python scripts/testing/test_health.py
python scripts/testing/test_endpoints.py

# Si usas pytest para descubrir pruebas (si están preparadas para pytest)
cd scripts/testing
pytest -v
```

---

## 📁 Estructura de Archivos Importantes

```
├── backend/
│   ├── app.py                 # Aplicación principal Flask
│   ├── requirements.txt       # Dependencias Python
│   ├── config/
│   │   ├── database.py       # Configuración BD
│   │   └── settings.py       # Configuración general
│   └── auth/
│       ├── repository/auth_repository.py
│       ├── service/auth_service.py
│       └── routes/auth_routes.py
├── frontend/
│   ├── index.html            # Página principal
│   ├── assets/css/styles.css # Estilos principales
│   ├── assets/js/main.js     # JavaScript principal
│   └── services/
│       ├── api.js            # Cliente API
│       └── auth.js           # Servicio de autenticación
└── data/
    └── database_complete.sql  # Schema y datos iniciales
```

---

## 📝 Procedimientos Almacenados

### Principales Stored Procedures
- `VentaCompletaPasajes()` - Proceso completo de venta
- `ActualizarChoferSeguro()` - Actualización segura de choferes
- `ReservarAsientoSeguro()` - Reserva con control de concurrencia

### Funciones
- `CalcularEdad()` - Cálculo de edad del pasajero
- `VerificarBloqueoAsiento()` - Verificación de estado de asiento

---

## 🐛 Debugging y Logs

### Archivos de Log
- `backend/logs/app.log` - Logs generales de la aplicación
- `backend/logs/error.log` - Logs de errores
- Base de datos: Tabla `bitacora` para auditoría

### Debugging
```bash
# Modo debug activado en .env
DEBUG=True
LOG_LEVEL=DEBUG

# Ejecutar con logs detallados
python app.py --debug
```

---

## 📈 Monitoreo y Rendimiento

### Métricas Clave
- Tiempo de respuesta API: < 2 segundos
- Concurrencia: 500 usuarios simultáneos
- Uptime objetivo: 99%
- Tamaño máximo de archivo: 16MB

### Herramientas de Monitoreo
- Logs de aplicación
- Monitoreo de base de datos MySQL
- Estadísticas de uso por navegador

---

## 🤝 Contribución

### Estándares de Código
- Python: PEP 8
- JavaScript: ES6+ con JSDoc
- SQL: Nomenclatura en español, comentarios obligatorios

### Flujo de Desarrollo
1. Crear rama feature/nombre-funcionalidad
2. Implementar con tests correspondientes
3. Documentar cambios
4. Pull request con revisión

---

## 📞 Soporte y Contacto

### Información de la Empresa
- **Nombre:** Transporte Serrano del Oriente
- **Teléfono:** 591-12345678
- **Dirección:** Av. Principal #123, Ciudad

### Soporte Técnico
- **Desarrollador:** [Nombre del Desarrollador]
- **Email:** [email@dominio.com]
- **Versión del Sistema:** 1.0.0

---

## 📄 Licencia

Este proyecto es de uso exclusivo de **Transporte Serrano del Oriente**. 
Todos los derechos reservados © 2025.

---

## 🔄 Changelog

### v1.0.0 (2025-01-04)
- ✨ Implementación inicial del sistema
- ✅ Módulo de autenticación completo
- ✅ Gestión básica de ventas y pasajeros
- ✅ Base de datos con procedimientos almacenados
- ✅ Interface web responsive
- ✅ Sistema de reportes básico

---

**Última actualización:** 4 de Septiembre, 2025  
**Estado:** En desarrollo activo 🚧
