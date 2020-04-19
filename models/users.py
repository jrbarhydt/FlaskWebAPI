from mongoengine import Document, EmbeddedDocument, EmbeddedDocumentField, ListField, StringField, \
    EmailField, DateField, ReferenceField, BooleanField
from flask_bcrypt import generate_password_hash, check_password_hash
import re


class Access(EmbeddedDocument):
    guest = BooleanField(default=True)
    user = BooleanField(default=True)
    server = BooleanField(default=False)
    cook = BooleanField(default=False)
    manager = BooleanField(default=False)
    admin = BooleanField(default=False)


class PhoneField(StringField):
    # Modification of http://regexlib.com/REDetails.aspx?regexp_id=61
    #
    # US Phone number that accept a dot, a space, a dash, a forward slash, between the numbers.
    # Will Accept a 1 or 0 in front. Area Code not necessary
    REGEX = re.compile(r"((\(\d{3}\)?)|(\d{3}))([-\s./]?)(\d{3})([-\s./]?)(\d{4})")

    def validate(self, value):
        if not PhoneField.REGEX.match(string=value):
            self.error(f"ERROR: `{value}` Is An Invalid Phone Number.")
        super(PhoneField, self).validate(value=value)


class User(Document):
    email = EmailField(required=True, unique=True)
    password = StringField(required=True, min_length=6, regex=None)
    access = ListField(EmbeddedDocumentField(Access), default=[Access(guest=True)])

    def generate_pw_hash(self):
        self.password = generate_password_hash(password=self.password).decode('utf-8')

    def check_pw_hash(self, password):
        return check_password_hash(pw_hash=self.password, password=password)