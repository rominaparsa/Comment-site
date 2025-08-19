from django.core.exceptions import ValidationError
from .models import ContactUs

class Validation():

    def CheckEmpaty(self, value):
        if value == "":
            raise ValidationError("مقدار خالی است")


    def CheckLenPhone(self, value):
        if len(value) < 11:
            raise ValidationError("شماره تماس کوتاه است")
        if not value.isnumeric():
            raise ValidationError("شماره تماس فقط میتواند شامل اعدادباشد")

    def ChechAlpha(self, value):
        if not value.isalpha():
            raise ValidationError("مقدار فقط کارکتر باید باشد")

    def CheckEmailExist(self ,value):
        result = ContactUs.objects.filter(Email=value).all()
        if len(result)>0:
            raise ValidationError("مقدار ایمیل"+ value + "تکراری است")