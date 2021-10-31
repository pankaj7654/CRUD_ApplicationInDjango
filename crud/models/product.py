from django.db import models
from crud.models.user import User

class Product(models.Model):
    name = models.CharField(max_length = 50)
    description = models.TextField(max_length = 200)
    quantity = models.IntegerField()
    price = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    


    # return user name in admin panel
    def __str__(self):
        return self.name