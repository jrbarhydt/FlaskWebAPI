# mongo-engine packages
import mongoengine

# project resources
from app import default_config

# external packages
from types import FunctionType
import os

def mongo(function: FunctionType) -> FunctionType:
    """
    Decorator method for running mongoengine before function execution.

    :param function: Function to run after execution.
    :return: wrapper function
    """
    def load():
        if 'MONGODB_URI' in os.environ:
            default_config.update({'MONGODB_SETTINGS': {"host": os.environ['MONGODB_URI']}})
        mongoengine.connect(**default_config['MONGODB_SETTINGS'])
        function()
    return load
