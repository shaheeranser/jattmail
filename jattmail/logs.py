from datetime import datetime
from sys import stdout
from jattmail.settings import LOG_ECHO, LOG_WRITE, LOG_FILE

class Logs:
    def __init__(self):
        self.logfile = open(LOG_FILE, "at")
    
    def new(self, address:tuple[str, int], data:bytes|str):
        log = f"{address[0], address[1]} - {datetime.now()} - {data}\n"
        if LOG_ECHO:
            stdout.write(log)
        if LOG_WRITE:
            self.logfile.write(log)

    def customLog(self, log:str):
        log = f"{datetime.now()} - {log}\n"
        if LOG_ECHO:
            stdout.write(log)
        if LOG_WRITE:
            self.logfile.write(log)
        
    def close(self):
        self.logfile.close()