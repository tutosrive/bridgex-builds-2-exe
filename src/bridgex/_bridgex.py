from pathlib import Path
from .database import Manager
from chromologger import Logger as Log

# Initial paths to files
log:Log = Log(f'{Path(__file__).parent}/logs/log_bridgex.log')

class Bridgex:
    @staticmethod
    def run_app():
        try:
            Manager.database_config()
            from .interface import run
            run()
        except Exception as e:
            log.log_e(e)