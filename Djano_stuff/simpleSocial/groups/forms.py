from django import forms
from basic_app.models import Referral
class ReferralForm(forms.ModelForm):
    #username = forms.CharField(label='Username',max_length=250)
    #referal_code = forms.CharField(label='Referal_code',max_length=250)
    class Meta():
        fields = ('username','direct_referral_code')
        model = Referral
