# Módulo de Logs

Un módulo Python simple y configurable para gestionar logs en aplicaciones. Permite guardar mensajes en archivos separados por tipo (info, error, warning), con rotación automática, filtrado y visualización eficiente.

## Características

- **Gestión de logs por tipo**: Archivos separados para info, error y warning.
- **Rotación automática**: Limita el tamaño de archivos y mantiene backups.
- **Configuración flexible**: Personaliza extensión, codificación, tamaño máximo, etc.
- **Visualización avanzada**: Muestra logs filtrados por fecha o últimas líneas.
- **Manejo de errores**: Robustez ante problemas de permisos o disco.
- **Independiente**: No depende de módulos externos como `logging`.

## Instalación

1. Copia el archivo `logs.py` a tu proyecto.
2. Importa la clase: `from logs import Logs`.

No requiere dependencias externas (usa solo módulos estándar de Python).

## Uso Básico

### Inicialización
```python
from logs import Logs

# Instancia básica
logger = Logs()

# Con configuración personalizada
logger = Logs(
    directory='./MiLogs',  # Carpeta para logs
    max_size=500*1024,    # 500 KB máximo por archivo
    extension='.log',     # Extensión de archivos
    console=False         # Sin prints en consola
)
```

### Guardar Logs
```python
logger.save_info_log("Aplicación iniciada correctamente.")
logger.save_error_log("Error de conexión a la base de datos.")
logger.save_warning_log("Advertencia: memoria baja.")
```

### Mostrar Logs
```python
# Mostrar todos los logs de info
logger.show_info_logs()

# Mostrar últimas 10 líneas de error
logger.show_error_logs(last_n=10)

# Mostrar logs de warning filtrados por fecha
logger.show_warning_logs(filter_date="2026-02-21")
```

## Configuración Avanzada

El constructor acepta los siguientes parámetros:

- `directory` (str): Ruta de la carpeta de logs (default: './Logs').
- `info/error/warning` (str): Nombres base de archivos (default: 'info_logs', etc.).
- `max_size` (int): Tamaño máximo en bytes por archivo (default: 1 MB).
- `max_backups` (int): Número de backups a mantener (default: 5).
- `extension` (str): Extensión de archivos (default: '.log').
- `encoding` (str): Codificación de archivos (default: 'utf-8').
- `console` (bool): Si mostrar mensajes en consola (default: True).

Ejemplo avanzado:
```python
logger = Logs(
    directory='/var/log/miapp',
    info='app_info',
    error='app_error',
    warning='app_warning',
    max_size=2*1024*1024,  # 2 MB
    max_backups=10,
    extension='.txt',
    encoding='latin-1',
    console=True
)
```

## API

### Métodos Principales

- `save_info_log(message: str)`: Guarda un log de información.
- `save_error_log(message: str)`: Guarda un log de error.
- `save_warning_log(message: str)`: Guarda un log de advertencia.
- `show_info_logs(last_n=None, filter_date=None)`: Muestra logs de info.
- `show_error_logs(last_n=None, filter_date=None)`: Muestra logs de error.
- `show_warning_logs(last_n=None, filter_date=None)`: Muestra logs de warning.

### Parámetros de `show_*_logs`
- `last_n` (int, opcional): Número de últimas líneas a mostrar.
- `filter_date` (str, opcional): Fecha en formato 'YYYY-MM-DD' para filtrar.

## Ejemplos

### Ejemplo Completo
```python
from logs import Logs

# Configurar logger
logger = Logs(directory='./logs', max_size=100*1024, console=False)

# Guardar logs
logger.save_info_log("Usuario logueado: admin")
logger.save_error_log("Fallo en autenticación")
logger.save_warning_log("CPU al 90%")

# Mostrar logs
logger.show_info_logs(last_n=5)  # Últimas 5 líneas de info
logger.show_error_logs(filter_date="2026-02-21")  # Errores de hoy
```

### Rotación de Archivos
Los archivos se rotan automáticamente cuando superan `max_size`. Ejemplo:
- `info_logs.log` (actual)
- `info_logs.log.1` (backup 1)
- `info_logs.log.2` (backup 2)
- ...

### Manejo de Errores
Si hay problemas (permisos, disco lleno), se muestra un mensaje en consola y se continúa.

## Notas

- **Compatibilidad**: Python 3.6+ (usa `pathlib` y `collections.deque`).
- **Rendimiento**: La rotación y filtrado son eficientes para archivos medianos.
- **Seguridad**: No valida inputs; sanitiza mensajes si es necesario.

## Contribuciones

Si encuentras bugs o mejoras, abre un issue o pull request en el repositorio.

## Licencia

Este proyecto está bajo la licencia MIT. Úsalo libremente.