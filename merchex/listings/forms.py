
from listings.models import Band, Listing
from django import forms


class ContactUsForm(forms.Form):
   name = forms.CharField(required=False)
   email = forms.EmailField()
   message = forms.CharField(max_length=1000)


class BandForm(forms.ModelForm):
   class Meta:
     model = Band
   #   fields = '__all__'
     exclude = ('active', 'official_homepage','like_new')


class ListingForm(forms.ModelForm):
   class Meta:
     model = Listing
   #   fields = '__all__' 
     exclude = ('sold',)