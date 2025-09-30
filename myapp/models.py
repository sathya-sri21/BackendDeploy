from django.db import models

# Create your models here.
class SampleTable(models.Model):
    id=models.AutoField(primary_key=True)
    user_name=models.CharField(max_length=50)
    user_email=models.CharField(max_length=300)

    def __str__(self):
        return self.user_name
    
class DressCategory(models.Model):
    id=models.AutoField(primary_key=True)
    category_name=models.CharField(max_length=300)

    def __str__(self):
        return self.category_name
    
class DressDetails(models.Model):
    id=models.AutoField(primary_key=True)
    dress_name=models.CharField(max_length=300)
    dress_image=models.URLField(max_length=8000)
    dress_price=models.IntegerField()
    dress_category=models.ForeignKey("DressCategory",on_delete=models.CASCADE)
    
    def __str__(self):
        return self.dress_name
    