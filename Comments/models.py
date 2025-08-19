from django.db import models

# Create your models here.

class User(models.Model):
    Id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=250)
    family=models.CharField(max_length=250)
    age=models.IntegerField(null=False)


class ContactUs(models.Model):
    Id = models.AutoField(primary_key=True)
    FullName = models.CharField( max_length=200,verbose_name="نام کامل")
    Phones = models.CharField(max_length=50,null=True,verbose_name="شماره تماس")
    Ip = models.CharField(max_length=100, null=True,verbose_name="ایپی کاربر")
    Email = models.EmailField(max_length=200,verbose_name="ایمیل کاربر")
    Message = models.TextField(max_length=200,verbose_name="متن ارسالی")

    class Meta:
        verbose_name="نظر"
        verbose_name_plural="نظرات"




"""
    def __str__ (self):
        return f"{self.FullName}|{self.Email}|{self.Phones}"
"""