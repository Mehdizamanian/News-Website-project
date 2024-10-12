from django import forms


class ContactForm(forms.Form):
  name=forms.CharField(max_length=200, required=True)
  email=forms.EmailField(required=True)
  phone=forms.IntegerField(required=True)
  subject=forms.CharField(max_length=200)
  message=forms.CharField(widget=forms.Textarea)
    

    
# class ContactForm(forms.ModelForm):
#   class Meta:
#     model=Contact
#     field=['name','email','phone','subject','message']
#     exclude=