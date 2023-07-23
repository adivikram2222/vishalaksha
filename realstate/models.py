# from tkinter import CASCADE
# from django.db import models

# # Create your models here.

# class Category(models.Model):
#     name = models.CharField(max_length=100)
#     slug = models.SlugField()
    
#     def __str__(self): 
#         return self.name

# class Property(models.Model):
#     Catrgory = models.ForeignKey(Category, on_delete=CASCADE)
#     total_flat_in_property = models.IntegerField()
#     city = models.CharField(max_length=100)
#     name_of_property = models.CharField(max_length=100)
#     number_of_bedrooms = models.IntegerField()
#     total_floor = models.IntegerField()
#     floor_number = models.IntegerField()
#     furnished_status = models.CharField(max_length=100)
#     number_of_bathroom = models.IntegerField()
#     super_area = models.CharField(max_length=100) 
#     build_up_area = models.CharField(max_length=100)
#     carpet_area = models.CharField(max_length=100)
#     trasaction_type = models.CharField(max_length=100)
#     available_from = models.DateTimeField()
#     expected_price = models.IntegerField()
#     maintanance_charge_per_month = models.IntegerField()
#     image = models.ImageField(upload_to='media')
#     slug = models.SlugField()


#     def __str__(self): 
#         return self.name_of_property
