from django import forms
from .models import Uploadvmpatchdb

class UploadvmpatchForm(forms.ModelForm):
    class Meta:
        model = Uploadvmpatchdb
        #fields = ('hypervisorIP', 'script', )
        fields = ('script', )