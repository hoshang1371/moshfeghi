from django import forms

class UserNewOrderForm(forms.Form):
    product_id = forms.IntegerField(
        widget=forms.HiddenInput(),
    )

    count = forms.IntegerField(
        widget= forms.TextInput(attrs={
            'min':"1",'name':"quantity",
            'id':'quantity','value':'۱',
            'class':'form-control input-small ToPersianValue',
            }),
        initial=1
    )