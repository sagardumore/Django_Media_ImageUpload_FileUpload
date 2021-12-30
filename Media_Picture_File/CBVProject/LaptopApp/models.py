from django.db import models

class Laptop(models.Model):
    company = models.CharField(max_length=32)
    model_name = models.CharField(max_length=32)
    ram = models.IntegerField()
    rom = models.IntegerField()
    processor = models.CharField(max_length=32)
    price = models.FloatField()
    weight = models.FloatField()
    profile = models.ImageField(upload_to='Images')
    file = models.FileField(upload_to='Files')


    def __str__(self):
        return f"{self.company},{self.model_name},{self.ram},{self.rom},{self.processor},{self.price},{self.weight},{self.profile},{self.file}"
