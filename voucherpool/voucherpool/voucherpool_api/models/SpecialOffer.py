from django.db import models


class SpecialOffer(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=180)
    discount = models.IntegerField(default=0)

    def __str__(self) -> str:
        return self.name
