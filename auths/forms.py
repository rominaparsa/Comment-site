from django import forms

class Login(forms.Form):
    def __init__(self,*args,**kwargs):
        super(Login,self).__init__(*args,**kwargs)
        for item in Login.visible_fields(self):
            item.field.widget.attrs["class"]= "form-control"


    UserName = forms.CharField(required=True,label="نام کاربری")
    Password = forms.CharField(required=True, label="رمزعبور",widget=forms.PasswordInput)

class Register(forms.Form):
    def __init__(self,*args,**kwargs):
        super(Register,self).__init__(*args,**kwargs)
        for item in Login.visible_fields(self):
            item.field.widget.attrs["class"]= "form-control"

    Name = forms.CharField(required=True, label="نام شما")
    Family = forms.CharField(required=True, label="نام خانوادگی شما")
    UserName = forms.CharField(required=True,label="نام کاربری")
    Password = forms.CharField(required=True, label="رمزعبور",widget=forms.PasswordInput)