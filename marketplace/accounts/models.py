from django.db import models


class Client(models.Model):
    id = models.BigAutoField(primary_key=True, editable=False, null=False)
    full_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=100)
    email = models.EmailField(max_length=100, unique=True)

    objects = models.Manager()

    def __str__(self):
        return f'{self.full_name}'

    class Meta:
        verbose_name = 'client'
        verbose_name_plural = 'clients'
