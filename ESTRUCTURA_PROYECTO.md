# ESTRUCTURA REORGANIZADA DEL PROYECTO
## Transporte Serrano del Oriente

### 📁 Estructura Propuesta

```
TRANSPORTE SERRANO DEL ORIENTE/
├── 📂 backend/                     # API Backend (Python Flask)
│   ├── 📂 config/                  # Configuración global
│   │   ├── database.py            # Configuración de BD
│   │   └── settings.py            # Configuración general
│   ├── 📂 auth/                    # Dominio: Autenticación
│   │   ├── repository/            # Capa de datos
│   │   ├── service/               # Lógica de negocio
│   │   └── routes/                # Capa de presentación
│   ├── 📂 pasajeros/              # Dominio: Pasajeros
│   ├── 📂 ventas/                 # Dominio: Ventas
│   ├── 📂 buses/                  # Dominio: Buses
│   ├── 📂 rutas/                  # Dominio: Rutas
│   ├── 📂 reportes/               # Dominio: Reportes
│   ├── 📂 shared/                 # Utilidades compartidas
│   ├── app.py                     # Aplicación principal
│   ├── requirements.txt           # Dependencias
│   └── .env.example              # Variables de entorno
├── 📂 frontend/                    # Interfaz de Usuario
│   ├── 📂 assets/                 # Recursos estáticos
│   │   ├── css/                   # Estilos
│   │   ├── js/                    # JavaScript
│   │   └── images/                # Imágenes
│   ├── 📂 components/             # Componentes reutilizables
│   ├── 📂 pages/                  # Páginas por módulo
│   ├── 📂 services/               # Servicios de API
│   ├── 📂 admin/                  # Panel de administración
│   └── index.html                 # Página principal
├── 📂 scripts/                     # Scripts de utilidad
│   ├── 📂 database/               # Scripts de BD
│   ├── 📂 deployment/             # Scripts de despliegue
│   ├── 📂 maintenance/            # Scripts de mantenimiento
│   └── 📂 testing/                # Scripts de pruebas
├── 📂 data/                        # Base de Datos
│   ├── database_complete.sql      # Schema completo
│   └── backups/                   # Respaldos
├── 📂 docs/                        # Documentación
│   ├── api/                       # Documentación API
│   ├── installation/              # Guías de instalación
│   └── user/                      # Manual de usuario
├── start_server.py                # Script principal de inicio
├── start_server.bat              # Script de inicio Windows
├── README.md                     # Documentación principal
└── .gitignore                    # Archivos ignorados por Git
```

### 🗑️ Archivos a Eliminar (Duplicados/Innecesarios)

#### Backend - Scripts de prueba y duplicados:
- `analyze_real_db_structure.py`
- `arreglar_simple.py`
- `arreglar_usuarios.py`
- `consulta_simple.py`
- `create_user.py`
- `database_structure_analysis.json`
- `db_complete_init.py`
- `db_diagnostic.py`
- `diagnostico_db.py`
- `diagnostico_db_reporte.json`
- `ejemplo_agregar_usuario.py`
- `fix_all_users.py`
- `fix_mysql.py`
- `fix_passwords.py`
- `listar_usuarios.py`
- `monitor_db.py`
- `optimize_database.py`
- `repair_mysql_aria.py`
- `repair_mysql_system.py`
- `run_tests.py`
- `test_*.py` (varios archivos de prueba)
- `venv/` (entorno virtual - debe recrearse)

#### Documentación duplicada:
- `CREDENCIALES.md`
- `CREDENCIALES_FINALES.md`
- `DOCUMENTACION_TECNICA.txt`
- `GUIA_COMPLETA_INSTALACION.txt`
- `GUIA_INSTALACION.txt`
- `RESUMEN_CREDENCIALES.md`

### ✅ Archivos Funcionales a Mantener

#### Backend Core:
- `app.py` - Aplicación principal Flask
- `requirements.txt` - Dependencias
- `.env.example` - Template de variables
- Carpetas de dominio: `auth/`, `pasajeros/`, `ventas/`, `buses/`, `rutas/`, `reportes/`
- `config/` - Configuración

#### Frontend Core:
- `index.html` - Página principal
- `assets/` - Recursos estáticos
- `admin/` - Panel administrativo
- `services/` - Servicios API
- `pages/` - Páginas del sistema

#### Scripts Útiles:
- `start_server.py` - Inicio del servidor
- `start_server.bat` - Inicio Windows
- `test_endpoints.py` - Pruebas de API (mover a scripts/testing/)

#### Datos:
- `data/database_complete.sql` - Schema de BD

### 🔄 Plan de Reorganización

1. **Crear estructura de carpetas limpia**
2. **Mover archivos funcionales a ubicaciones correctas**
3. **Eliminar archivos duplicados/innecesarios**
4. **Consolidar documentación**
5. **Actualizar referencias en código**
6. **Crear documentación organizada**
