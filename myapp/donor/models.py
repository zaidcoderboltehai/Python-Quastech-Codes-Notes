from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Food(models.Model):
    donor=models.ForeignKey(User,on_delete=models.CASCADE)
    name=models.CharField(max_length=100)
    description=models.TextField()
    expiry_date=models.DateField()
    pickup_address=models.TextField()
    image=models.ImageField(upload_to='food_images/')

    class Meta:
        db_table="food"



