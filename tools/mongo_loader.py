# mongo-engine packages
import mongoengine

# project resources
from app import default_config

# external packages
from types import FunctionType


def mongo(function: FunctionType) -> FunctionType:
    """
    Decorator method for running mongoengine before function execution.

    :param function: Function to run after execution.
    :return: wrapper function
    """
    def load():
        mongoengine.connect(**default_config['MONGODB_SETTINGS'])
        function()
    return load
