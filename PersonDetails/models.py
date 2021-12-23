from django.db import models
from Person.models import Person


# Create your models here.

class PersonDetails(models.Model):
    person_data = models.ForeignKey(Person, on_delete=models.CASCADE)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zip = models.CharField(max_length=100)
    country = models.CharField(max_length=100)

    def __str__(self):
        return self.city

    def person(self):
        personData = Person.objects.filter(id=self.person_data_id)
        personData.update(city=self.city, state=self.state, zip=self.zip, country=self.country)

    def save(self, *args, **kwargs):
        self.person()
        super(PersonDetails, self).save(*args, **kwargs)
