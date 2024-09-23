from mongoengine import Document, StringField, EmailField, ListField

class ExtractedData(Document):
    email = EmailField(required=True, unique=True)
    nouns = ListField(StringField())
    verbs = ListField(StringField())

    def __str__(self):
        return self.email