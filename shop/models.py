from django.db import models

# Create your models here.

class MainCategory(models.Model):
    main_name=models.CharField(max_length=200)
    class Meta:
        db_table="MainCat"


class Category(models.Model):
    cat_id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=200)
    description=models.CharField(max_length=300)
    main_category=models.ForeignKey(MainCategory, on_delete=models.CASCADE, null=True)

    class Meta:
        db_table="Catagory"

class Product(models.Model):
    name=models.CharField(max_length=200)
    price=models.FloatField()
    stock=models.PositiveIntegerField()
    category=models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    product_image = models.ImageField(upload_to='images',null=True)
    class Meta:
        db_table="Products"

