from django.db import models


class Customer(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=180)
    email = models.CharField(max_length=300, unique=True)

    def __str__(self) -> str:
        return self.name
