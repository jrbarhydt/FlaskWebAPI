from models.meals import Meals
from tools.mongo_loader import mongo
import csv


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

