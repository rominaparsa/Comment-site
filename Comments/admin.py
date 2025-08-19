from django.contrib import admin
from .models import ContactUs
from django.core.exceptions import ValidationError
from .customvalidation import Validation
# Register your models here.

class ContactUsAdmin(admin.ModelAdmin):
    list_display = ("FullName","Email","Phones")

    def formfield_for_dbfield(self,db_field,**kwargs):
        validation = Validation()
        formfield = super().formfield_for_dbfield(db_field,**kwargs)
        if db_field.name == "FullName":
            formfield.validators.append(validation.CheckEmpaty)
            formfield.validators.append(validation.ChechAlpha)
        if db_field.name == "Phones":
            formfield.validators.append(validation.CheckLenPhone)
        if db_field.name == "Email":
            formfield.validators.append(validation.CheckEmailExist)
        return formfield

admin.site.register(ContactUs,ContactUsAdmin)
