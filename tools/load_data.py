# mongoengine resources
from mongoengine import NotUniqueError, ValidationError

# project resources
from models.meals import Meals
from models.users import Users
from tools.mongo_loader import mongo
from tools.get_random_document import get_random

# external packages
import csv
from random import randint


@mongo
def csv_to_meal(filepath: str = 'resources/meal_data.csv', delimiter: str = '\t'):
    """
    Converts data in csv file to documents in meal collection.
    Uses @mongo wrapper to connect via mongoengine during execution.

    :param filepath:
    :param delimiter:
    :return:
    """
    with open(filepath, 'r') as file:
        data = csv.DictReader(file, delimiter=delimiter)

        for datum in data:
            dish = Meals(**datum, __auto_convert=True).save()
            print(f"Added: {dish.name} | {dish.description} | {dish.price} => {dish.id}")


@mongo
def generate_test_users(filepath: str = 'resources/user_data.csv', delimiter: str = '\t'):
    """
    Converts data in csv file to documents in user collection.
    Uses @mongo wrapper to connect via mongoengine during execution.
    Randomly generates fav_meals list and access__admin parameters.

    :param filepath:
    :param delimiter:
    :return:
    """
    with open(filepath, 'r') as file:
        data = csv.DictReader(file, delimiter=delimiter)

        for datum in data:
            try:
                user = Users(**datum, __auto_convert=True)
                # generate random admin access, password, and favorite meals
                user.access.admin = (randint(0, 1) == 1)
                user.fav_meals = get_random(Meals, randint(1, 5))
                user.password = user.name + str(randint(0, 9))

                user.save()
                print(f"Added: {user.name} | {user.email} | {user.password} | Admin-{user.access.admin is True} => {user.id}")
            except NotUniqueError:
                print(f'Invalid Entry: {user.email} is already taken.')
            except ValidationError:
                print(f'Validation Error: {user}')


def load_all(config: dict = None):
    """
    Load test data into given configuration.
    :return:
    """
    from tools.mongo_loader import default_config

    if config:
        default_config.update(config)

    csv_to_meal()
    generate_test_users()
