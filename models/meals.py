from mongoengine import Document, StringField, FloatField


class Meal(Document):
    """
    Template for a mongoengine document, which represents a user's favorite meal.

    :param name: required string value
    :param description: optional string value, fewer than 120 characters
    :param price: optional float value
    :param image_url: optional string image url
    :Example:

    >>> import mongoengine
    >>> from app import default_config

    >>> mongoengine.connect(**default_config['MONGODB_SETTINGS'])
    MongoClient(host=['localhost:27017'], document_class=dict, tz_aware=False, connect=True, read_preference=Primary())

    >>> new_meal = Meal(name= "Vegetable Spring Rolls", \
                        description= "These crisp veggie rolls are filled with"  \
                                     "cabbage, peppers, cucumber, and home-made peanut sauce.")
    >>> new_meal.save()
    <Meal: Meal object>

    """

    name = StringField(required=True)
    description = StringField()
    price = FloatField()
    image_url = StringField()