from django.db import models


class Breed(models.Model):
    name = models.CharField(max_length=100, default='')

    def __str__(self):
        return self.name


class Curator(models.Model):

    name = models.CharField(max_length=100, default='')
    surname = models.CharField(max_length=100, default='')

    def __str__(self):
        return self.surname

    def get_full_name(self):
        return self.name + ' ' + self.surname


class Dog(models.Model):

    name = models.CharField(max_length=100, default='')
    breed = models.ForeignKey(Breed, null=True, on_delete=models.SET_NULL)
    birth_date = models.DateField()
    curator = models.ForeignKey(Curator, null=True, on_delete=models.SET_NULL)
    fixed = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class Payment(models.Model):

    date = models.DateTimeField()
    number = models.DecimalField(max_digits=9, decimal_places=0)
    amount = models.DecimalField(max_digits=15, decimal_places=2)
    dog = models.ForeignKey(Dog, null=True, on_delete=models.SET_NULL)
    transaction_id = models.DecimalField(max_digits=20, decimal_places=0)
    purpose = models.CharField(max_length=250, default='')
