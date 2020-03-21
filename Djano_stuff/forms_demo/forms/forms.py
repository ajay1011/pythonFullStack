from django import forms
from forms.models import User

class FormName(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    text = forms.CharField(widget = forms.Textarea)

class NewUserForm(forms.ModelForm):
    class Meta():
        model = User
        fields = '__all__'
