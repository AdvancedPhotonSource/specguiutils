import logging
import logging.config
import os
from ConfigParser import NoSectionError
LOGGER_NAME="specguiutils"
LOGGER_DEFAULT = {
    'version' : 1,
    'handlers' : {'consoleHandler' : {'class' : 'logging.StreamHandler',
                               'level' : 'INFO',
                               'formatter' : 'consoleFormat',
                               'stream' : 'ext://sys.stdout'}
                  },
    'formatters' : {'consoleFormat' : {'format' : '%(asctime)-15s - %(name)s - %(funcName)s- %(levelname)s - %(message)s'}
                    },
    'loggers' : {'root' :{'level' : 'INFO',
                        'handlers' : ['consoleHandler',],
                      },
               'specguiutils' : {'level' : 'INFO',
                            'handlers' : ['consoleHandler',],
                            'qualname' : 'specguiutils'
                            }
               },
   }

userDir = os.path.expanduser("~")
logConfigFile = os.path.join(userDir, LOGGER_NAME + 'Log.config')
try:
    logging.config.fileConfig(logConfigFile)
except NoSectionError:
    logging.config.dictConfig(LOGGER_DEFAULT)
    
logger = logging.getLogger(LOGGER_NAME)
