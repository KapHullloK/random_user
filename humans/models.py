from django.db import models

NULLABLE = {
    "null": True,
    "blank": True,
}


class Human(models.Model):
    gender = models.CharField(max_length=40, **NULLABLE, verbose_name='gender')
    first_name = models.CharField(max_length=50, verbose_name='first name')
    last_name = models.CharField(max_length=50, **NULLABLE, verbose_name='last name')
    phone_number = models.CharField(max_length=40, **NULLABLE, verbose_name='phone number')
    email = models.EmailField(**NULLABLE, verbose_name='email')
    avatar = models.URLField(**NULLABLE, verbose_name='avatar')
    street = models.CharField(max_length=80, **NULLABLE, verbose_name='street')
    city = models.CharField(max_length=60, **NULLABLE, verbose_name='city')
    country = models.CharField(max_length=60, **NULLABLE, verbose_name='country')
    link_to_details = models.URLField(**NULLABLE, verbose_name='details')

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
