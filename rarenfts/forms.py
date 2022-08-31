from django import forms
from django.forms import ModelForm
from .models import NFT, Collection

class NFTForm(ModelForm):
    class Meta:
        model = NFT
        fields = '__all__'

class CollectionForm(ModelForm):
    # name = forms.CharField(max_length=255)
    # network = forms.CharField(max_length=255)
    # floor_price = forms.DecimalField(max_digits=)
    # # volume = request.POST['volume']
    # date = request.POST['date']
    # discord = request.POST['discord']
    # twitter = request.POST['twitter']
    # website = request.POST['website']
    # listing_type = request.POST['listing_type']
    # image_f = request.FILES.get('image', '')
    # image = request.POST.get('image', '')

    class Meta:
        model = Collection
        fields = '__all__'
        exclude = ['created_on', 'updated_on', 'volume', 'featured', 'verification']

