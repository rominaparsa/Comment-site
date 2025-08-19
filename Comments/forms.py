from django import forms
from .models import ContactUs


class ContactUsModel(forms.Form):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)  # خط اصلاح‌شده
        for item in self.visible_fields():
            item.field.widget.attrs["class"] = "form-control"

    FullName = forms.CharField(
        required=True,
        min_length=3,
        help_text="مثال:میلادمرادیان",
        max_length=200,
        label="نام کامل",
        error_messages={"required": "نام خودرا صحیح واردکنید"}
    )

    Phones = forms.CharField(
        required=True,
        min_length=3,
        help_text="مثال:شماره تماس",
        max_length=200,
        label="شماره تماس",
        error_messages={"required": "شماره خودرا صحیح واردکنید"}
    )

    Email = forms.EmailField(
        required=True,
        label="ایمیل",
        widget=forms.EmailInput
    )
    Message = forms.CharField(
        widget=forms.Textarea,
        label="متن پیام",
        max_length=500
    )
    Id = forms.CharField(
        widget=forms.HiddenInput,
        required=True,
        initial="0",
        label=""
    )



class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactUs
        fields = ['FullName', 'Phones', 'Email', 'Message']


class CommentForm(forms.Form):
    name = forms.CharField( max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))

