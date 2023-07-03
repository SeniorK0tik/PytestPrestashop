import pathlib

from loguru import logger

p = pathlib.Path(__file__).parent
debug_f = p.joinpath('logs', 'debug.log')
info_f = p.joinpath('logs', 'info.log')
warning_f = p.joinpath('logs', 'warning.log')
error_f = p.joinpath('logs', 'error.log')

logger.add(debug_f, backtrace=True, diagnose=True, format='{time} {level} {message}',
           level='DEBUG', rotation='10 Mb', compression='zip')

logger.add(info_f, format='{time} {level} {message}',
           level='INFO', rotation='10 Mb', compression='zip')

logger.add(warning_f, format='{time} {level} {message}',
           level='WARNING', rotation='10 Mb', compression='zip')

logger.add(error_f, format='{time} {level} {message}',  backtrace=True,
           level='ERROR', rotation='10 Mb', compression='zip')

if __name__ == '__main__':
    print(pathlib.Path(__name__))