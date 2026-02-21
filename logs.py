"""
Modulo de Logs
"""
from datetime import datetime
from pathlib import Path
from collections import deque

class Logs:
    """
    _Clase principal para gestionar los logs_

    Args:
        directory (str): Ruta de la carpeta (default: './Logs')
        info (str): Nombre del archivo Info
        error (str): Nombre del archivo Error
        warning (str): Nombre del archivo Warning
        max_size (int): Tamaño máximo del archivo (default: 1MB)
        max_backups (int): Número de copias de seguridad (default: 5)
        extension (str): Extension del archivo (default: '.log')
        encoding (str): Codificación del archivo (default: 'utf-8')
        console (bool): Mostrar logs en la consola (default: True)

    Methods:
        log: Guarda el log
        save_info_log: Guarda el log de Info
        save_error_log: Guarda el log de Error
        save_warning_log: Guarda el log de Warning
        show_info_logs: Muestra el log de Info
        show_error_logs: Muestra el log de Error
        show_warning_logs: Muestra el log de Warning
    """
    def __init__(self, directory='./Logs', info="info_logs", error="error_logs", warning="warning_logs", max_size=1024*1024, max_backups=5, extension=".log", encoding="utf-8", console=True):
        self.directory = Path(directory)
        self.extension = extension
        self.archive_info = f"{info}.{self.extension}"
        self.archive_error = f"{error}.{self.extension}"
        self.archive_warning = f"{warning}.{self.extension}"
        self.max_size = max_size
        self.max_backups = max_backups
        self.encoding = encoding
        self.console = console

        if not self.directory.exists():
            try:       
                self.directory.mkdir(parents=True, exist_ok=True)
            except OSError:
                self.log("Error al crear la carpeta de logs, comprueba la ruta o los permisos.")

    def _rotate_file(self, file_path: Path):
        """Rota el archivo si supera el tamaño máximo."""
        if file_path.exists() and file_path.stat().st_size >= self.max_size:
            for i in range(self.max_backups, 0, -1):
                backup = file_path.with_suffix(f"{file_path.suffix}.{i}")
                if backup.exists():
                    if i == self.max_backups:
                        backup.unlink()  # Eliminar el más antiguo
                    else:
                        backup.rename(file_path.with_suffix(f"{file_path.suffix}.{i+1}"))
            # Rotar el archivo actual
            file_path.rename(file_path.with_suffix(f"{file_path.suffix}.1"))
    def _sanitize_message(self, message: str) -> str:
        """Sanitiza el mensaje para evitar caracteres problemáticos."""
        if not isinstance(message, str):
            message = str(message)
        message = message.replace('\n', ' ').replace('\r', ' ')
        message = message.strip()
        return message[:1000] 
    def log(self, message:str):
        """_Metodo para mostrar el log en la consola_

        Args:
            message (str): Mensaje a mostrar en consola
        """
        if self.console:
            print(f"{message}")

    def save_info_log(self, message:str):
        """_Metodo para guardar el log info_

        Args:
            message (str): Mensaje para guardar en el log info
        """
        message = self._sanitize_message(message)
        timestamp = datetime.now().strftime("[%Y-%m-%d %H:%M:%S]")
        try:
            self._rotate_file(self.directory / self.archive_info)
            with open(f'{self.directory}/{self.archive_info}', 'a', encoding=self.encoding) as f:
                f.write(f"{timestamp} {message}")
                f.write('\n')
            self.log(f"Nuevo log guardado en {self.archive_info}.")
        except OSError:
            self.log("Error al guardar el log info, comprueba la ruta o los permisos.")    

    def save_error_log(self, message:str):
        """_Metodo para guardar el log error_

        Args:
            message (str): Mensaje para guardar en el log error
        """
        message = self._sanitize_message(message)
        timestamp = datetime.now().strftime("[%Y-%m-%d %H:%M:%S]")
        try:
            self._rotate_file(self.directory / self.archive_error)
            with open(f'{self.directory}/{self.archive_error}', 'a', encoding=self.encoding) as f:
                f.write(f"{timestamp} {message}")
                f.write('\n')
            
            self.log(f"Nuevo error log guardado en {self.archive_error}.")
        except OSError:
            self.log("Error al guardar el log error, comprueba la ruta o los permisos.")

    def save_warning_log(self, message:str):
        """_Metodo para guardar el log warning_

        Args:
            message (str): Mensaje para guardar en el log warning
        """
        message = self._sanitize_message(message)
        timestamp = datetime.now().strftime("[%Y-%m-%d %H:%M:%S]")
        try:
            self._rotate_file(self.directory / self.archive_warning)
            with open(f'{self.directory}/{self.archive_warning}', 'a', encoding=self.encoding) as f:
                f.write(f"{timestamp} {message}")
                f.write('\n')
            
            self.log(f"Nuevo warning log guardado en {self.archive_warning}.")
        except OSError:
            self.log("Error al guardar el log warning, comprueba la ruta o los permisos.")
    
    def show_info_logs(self, last_n=None, filter_date=None):
        """
        _Mostrar todos los logs de info por consola_

        Args:
            last_n (int, optional): Número de últimas lineas a mostrar. Si None, muestra todo.
            filter_date (str, optional): Fecha en formato 'YYYY-MM-DD' para filtrar logs. Si None, no filtra.
        """
        try:
            with open(f'{self.directory}/{self.archive_info}', 'r', encoding=self.encoding) as f:
                lines = f.readlines()
            if filter_date:
                lines = [line for line in lines if filter_date in line]
            
            if last_n and last_n > 0:
                lines = deque(lines, maxlen=last_n)
        
            print(''.join(lines))
        except OSError:
            self.log("Error al mostrar el log info, comprueba la ruta o los permisos.")
        
    def show_error_logs(self, last_n=None, filter_date=None):
        """
        _Mostrar todos los logs de error por consola_
        Args:
            last_n (int, optional): Número de últimas lineas a mostrar. Si None, muestra todo.
            filter_date (str, optional): Fecha en formato 'YYYY-MM-DD' para filtrar logs. Si None, no filtra.
        """
        try:
            with open(f'{self.directory}/{self.archive_error}', 'r', encoding=self.encoding) as f:
                lines = f.readlines()
            if filter_date:
                lines = [line for line in lines if filter_date in line]
            
            if last_n and last_n > 0:
                lines = deque(lines, maxlen=last_n)
        
            print(''.join(lines))
        except OSError:
            self.log("Error al mostrar el log error, comprueba la ruta o los permisos.")
        
    def show_warning_logs(self, last_n=None, filter_date=None):
        """
        _Mostrar todos los logs de warning por consola_
        Args:
            last_n (int, optional): Número de últimas lineas a mostrar. Si None, muestra todo.
            filter_date (str, optional): Fecha en formato 'YYYY-MM-DD' para filtrar logs. Si None, no filtra.
        """
        try:
            with open(f'{self.directory}/{self.archive_warning}', 'r', encoding=self.encoding) as f:
                lines = f.readlines()
            if filter_date:
                lines = [line for line in lines if filter_date in line]
            
            if last_n and last_n > 0:
                lines = deque(lines, maxlen=last_n)
        
            print(''.join(lines))
        except OSError:
            self.log("Error al mostrar el log warning, comprueba la ruta o los permisos.")