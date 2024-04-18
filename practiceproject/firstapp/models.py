from django.db import models
class User(models.Model):
    name=models.CharField(max_length=30)
    phone=models.IntegerField(null=True)
    email=models.EmailField(max_length=30,unique=True)
    password=models.CharField(max_length=20,default="")

    class  Meta:
        db_table="user"


        