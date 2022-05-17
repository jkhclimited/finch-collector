from django.forms import ModelForm
from .models import Owned

class OwnedForm(ModelForm):
  class Meta:
    model = Owned
    fields = ['set', 'copies']
