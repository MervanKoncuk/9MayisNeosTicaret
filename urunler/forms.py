from django.forms import ModelForm
from .models import Urun

class UrunForm(ModelForm):
    class Meta:
        model = Urun
        fields = ['isim', 'aciklama', 'fiyat', 'resim']
    def __init__(self, *args, **kwargs):
        super(UrunForm, self).__init__(*args, **kwargs)
        # self.fields['username'].widget.attrs.update({'placeholder': 'Kullanıcı adı giriniz'})
        # self.fields['email'].widget.attrs.update({'class': 'form-control'})
        # self.fields['password1'].widget.attrs.update({'class': 'form-control'})
        # self.fields['password2'].widget.attrs.update({'class': 'form-control'})
        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'form-control'})
            field.help_text = ''