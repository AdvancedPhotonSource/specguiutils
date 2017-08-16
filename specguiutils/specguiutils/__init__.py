import logging
import logging.config
import os
import traceback
from configparser import NoSectionError

LOGGER_NAME="specguiutils"
LOGGER_DEFAULT = {
    'version' : 1,
    'handlers' : {'consoleHandler' : {'class' : 'logging.StreamHandler',
                               'level' : 'DEBUG',
                               'formatter' : 'consoleFormat',
                               'stream' : 'ext://sys.stdout'}
                  },
    'formatters' : {'consoleFormat' : {'format' : '%(asctime)-15s - %(name)s - %(funcName)s- %(levelname)s - %(message)s'}
                    },
    'loggers' : {'root' :{'level' : 'DEBUG',
                        'handlers' : ['consoleHandler',],
                      },
               'specguiutils' : {'level' : 'DEBUG',
                            'handlers' : ['consoleHandler',],
                            'qualname' : 'specguiutils'
                            }
               },
   }

userDir = os.path.expanduser("~")
logConfigFile = os.path.join(userDir, LOGGER_NAME + 'Log.config')
try:
    logging.config.fileConfig(logConfigFile)
except (NoSectionError,TypeError):
    logging.config.dictConfig(LOGGER_DEFAULT)
# except TypeError as ex:
#     print("Trouble reading log file %s %s" % (logConfigFile, str(ex)))
#     #traceback.print_stack()
    
logger = logging.getLogger(LOGGER_NAME)
