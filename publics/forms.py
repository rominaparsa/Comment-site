from django import forms

class askedForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super(askedForm, self).__init__(*args, **kwargs)
        for item in askedForm.visible_fields(self):
            item.field.widget.attrs["class"] = "form-control mr-0 ml-auto"

    title = forms.CharField(max_length=200, required=True, label='عنوان سوال')
    caption = forms.CharField(required=True, label='متن سوال', widget=forms.Textarea())  # تغییر 'text' به 'caption'
    ask_id = forms.IntegerField(widget=forms.HiddenInput(), initial=0)