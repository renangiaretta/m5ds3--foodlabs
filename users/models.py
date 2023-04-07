from django.db import models

# Create your models here.


class Seasons(models.TextChoices):
    SPRING = 'Primavera'
    SUMMER = 'Verão' 
    AUTUMN = 'Outono'
    WINTER = 'Winter'
    DEFAULT = 'Não informado'


class User(models.Model):
    first_name = models.CharField(max_length=10)
    last_name = models.CharField(max_length=10)
    email = models.EmailField()
    favorite_season = models.CharField(
        max_length=30,
        choices=Seasons.choices,
        default=Seasons.DEFAULT,
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __repr__(self) -> str:
        return f'<User ({self.id}) - {self.email}>'
