from django import forms

class ContactForm(forms.Form):
    from_email = forms.EmailField(required=True)
    #subject = forms.CharField(required=True)
    name = forms.CharField(required=True)
    phone_number =forms.IntegerField()
    # current_home = forms.CharField( required=True)
    # new_home= forms.CharField( required=True)
    # bedrooms=forms.IntegerField( required=True)
    # moving_date=forms.DateTimeField() 