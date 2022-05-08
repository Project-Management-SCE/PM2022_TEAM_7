from django import forms


class CreateNewPrescription(forms.Form):
    Patient_name = forms.CharField(Label="Name", max_Length=200)
    Drug_name = forms.CharField(Label="Name", max_Length=200)
    instructions = forms.CharField(Label="Name", max_Length=200)
