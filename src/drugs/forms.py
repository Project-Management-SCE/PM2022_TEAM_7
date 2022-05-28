from django import forms

class CheckoutForm(forms.Form):
    street_address=forms.CharField()
    apartment_address=forms.charField(required=False)
    city_address=form.charField()
    country_address = form.charField()
    zip_address = form.charField()
    save_info=forms.BooleanField(widget=forms.CheckboxInput())
    payment_option=forms.BooleanField(widget=forms.RadioSelect())