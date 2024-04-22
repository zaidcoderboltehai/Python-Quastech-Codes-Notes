from django.db import models
from firstapp.models import User
class Blog(models.Model):
    title=models.CharField(max_length=30)
    description=models.CharField(max_length=40)
    blog_image=models.ImageField(upload_to="blogs")
    user=models.ForeignKey(User,on_delete=models.CASCADE)

    class Meta:
        db_table="blog"
