from django import forms 
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

class LoginForm(AuthenticationForm):
   username= forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Your Username', 'style': 'max-width: 450px; margin-bottom: 15px;'})) 

   password= forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'Your Password', 'style': 'max-width: 450px; margin-bottom: 15px;'}))

class SignUpForm(UserCreationForm):
    class Meta:
        # configurations
        # using the user model from django and the the fields 
        model = User
        fields = ('username', 'email', 'password1', 'password2')
    
    username= forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Your Username', 'style': 'max-width: 450px; margin-bottom: 15px;'}))

    email= forms.CharField(widget=forms.EmailInput(attrs={'placeholder':'Your Email Address', 'style': 'max-width: 450px; margin-bottom: 15px;'}))

    password1= forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'Your Password', 'style': 'max-width: 450px; margin-bottom: 15px;'}))

    password2= forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'Repeat Password', 'style': 'max-width: 450px; margin-bottom: 15px;'}))



class ContactForm(forms.Form):
    name = forms.CharField(max_length=50)
    email = forms.EmailField()
    message = forms.CharField(widget=forms.Textarea)

    def clean_name(self):
        name = self.cleaned_data['name']
        if not name.replace(" ", "").isalpha():
            raise forms.ValidationError("Name must contain only letters.")
        return name

    def clean_message(self):
        message = self.cleaned_data['message']
        if len(message) < 10:
            raise forms.ValidationError("Message must be at least 10 characters long.")
        return message


