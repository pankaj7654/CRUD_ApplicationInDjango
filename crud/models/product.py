from django.db import models

class Product(models.Model):
    name = models.CharField(max_length = 50)
    description = models.TextField(max_length = 200)
    quantity = models.IntegerField()
    price = models.IntegerField()
    


    # return user name in admin panel
    def __str__(self):
        return self.name