"""
Modulo de Logs
"""
from time import ctime
from pathlib import Path

class Logs:
    """
    _Clase principal para gestionar los logs_

    Atributos:
        dir (str): Ruta de la carpeta (default: './Logs')
        archive_info (str): Nombre del archivo Info
        archive_error (str): Nombre del archivo Error
        archive_warning (str): Nombre del archivo Warning

    Metodos:
        log: Guarda el log
        save_info_log: Guarda el log de Info
        save_error_log: Guarda el log de Error
        save_warning_log: Guarda el log de Warning
    """
    def __init__(self, dir='./Logs', info="info_logs", error="error_logs", warning="warning_logs"):
        self.dir = Path(dir)
        self.archive_info = f"{info}.txt"
        self.archive_error = f"{error}.txt"
        self.archive_warning = f"{warning}.txt"

        if not self.dir.exists():
            self.dir.mkdir(parents=True, exist_ok=True)

    def log(self, message:str):
        """_Metodo para mostrar el log en la consola_

        Args:
            message (str): Mensaje a mostrar en consola
        """
        print(f"{message}")

    def save_info_log(self, message:str):
        """_Metodo para guardar el log info_

        Args:
            message (str): Mensaje para guardar en el log info
        """
        with open(f'{self.dir}/{self.archive_info}', 'a') as f:
            f.write("[" + ctime() + "] " + message)
            f.write('\n')
        
        self.log(f"Nuevo log guardado en {self.archive_info}.")

    def save_error_log(self, message:str):
        """_Metodo para guardar el log error_

        Args:
            message (str): Mensaje para guardar en el log error
        """
        with open(f'{self.dir}/{self.archive_error}', 'a') as f:
            f.write("[" + ctime() + "] " + message)
            f.write('\n')
        
        self.log(f"Nuevo error log guardado en {self.archive_error}.")

    def save_warning_log(self, message):
        """_Metodo para guardar el log warning_

        Args:
            message (str): Mensaje para guardar en el log warning
        """
        with open(f'{self.dir}/{self.archive_warning}', 'a') as f:
            f.write("[" + ctime() + "] " + message)
            f.write('\n')
        
        self.log(f"Nuevo warning log guardado en {self.archive_warning}.")
    
    def show_info_logs(self):
        """
        _Mostrar todos los logs de info por consola_
        """
        with open(f'{self.dir}/{self.archive_info}', 'r') as f:
            print(f.read())
        
    def show_error_logs(self):
        """
        _Mostrar todos los logs de error por consola_
        """
        with open(f'{self.dir}/{self.archive_error}', 'r') as f:
            print(f.read())
        
    def show_warning_logs(self):
        """
        _Mostrar todos los logs de warning por consola_
        """
        with open(f'{self.dir}/{self.archive_warning}', 'r') as f:
            print(f.read())