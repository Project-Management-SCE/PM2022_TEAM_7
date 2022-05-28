from django import forms

PAYMENT_CHOICES=(
    ('S', 'Stripe'),
    ('P', 'Paypal')
)

class CheckoutForm(forms.Form):
    street_address=forms.CharField()
    apartment_address = forms.CharField(required=False)
    city_address = forms.CharField()
    country_address = forms.CharField()
    zip_address = forms.CharField()
    save_info = forms.BooleanField(required=False)
    payment_option = forms.ChoiceField(widget=forms.RadioSelect(), choices=PAYMENT_CHOICES)