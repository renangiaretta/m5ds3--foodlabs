from django.db import models

# Create your models here.


class Address(models.Model):
    street = models.CharField(max_length=127)
    number = models.IntegerField()

    user = models.OneToOneField(
        'users.User',
        on_delete=models.CASCADE,
        related_name='address',
        null=True
        )

    def __repr__(self) -> str:
        return f'<Address ({self.id}) - {self.street}>'
