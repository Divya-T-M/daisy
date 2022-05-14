from django import forms

from .models import Seller, Customer


class AddAddressForm(forms.ModelForm):
    error_css_class = 'error-field'
    required_css_class = 'required-filed'
    name = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control"}))
    mobileno = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}))
    address = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control"}))
    pincode = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}))
    class Meta:
        model = Customer
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['seller'].queryset = Seller.objects.none()

        if 'district' in self.data:
            try:
                district_id = int(self.data.get('district'))
                self.fields['seller'].queryset = Seller.objects.filter(district_id=district_id).order_by('name')
            except (ValueError, TypeError):
                pass
        elif self.instance.pk:
            self.fields['seller'].queryset = self.instance.district.seller_set.all()
