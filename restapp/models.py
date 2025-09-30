from django.db import models

# Create your models here.
class ProductTable(models.Model):
    id=models.AutoField(primary_key=True)
    product_name=models.TextField(max_length=100)
    product_price=models.IntegerField()

    def __str__(self):
        return self.product_name
    