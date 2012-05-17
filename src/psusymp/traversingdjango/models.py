from django.db.models import Model
from django.db.models import CharField


class Person(Model):
    name = CharField(max_length=255)
    city = CharField(max_length=255)
    state = CharField(max_length=255)
    phone = CharField(max_length=255)

    def __unicode__(self):
        return "%s - %s" % (self.name, self.city)
