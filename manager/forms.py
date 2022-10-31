from django import forms
from business import models

class RegisterForm_Manager(forms.Form):
    job_company = forms.CharField(max_length = 50, label = 'The Company:',
        widget = forms.TextInput(attrs = {'placeholder': 'company name', 'class':'form-control'}))
    username = forms.CharField(max_length = 50, label = 'Username:',
        widget = forms.TextInput(attrs = {'placeholder': 'username', 'class':'form-control'}))
    email = forms.EmailField(max_length = 50, label = 'E-mail:',
        widget = forms.EmailInput(attrs = {'placeholder': 'e-mail', 'class':'form-control'}))
    password = forms.CharField(max_length = 20, label = 'Password',
        widget = forms.PasswordInput(attrs = {'placeholder': 'password', 'class':'form-control'}))
    confirm = forms.CharField(max_length = 20, label = 'Password Confirm:',
        widget = forms.PasswordInput(attrs = {'placeholder': 'password confirm', 'class':'form-control'}))

    def clean(self):
        username = self.cleaned_data.get('username')
        email = self.cleaned_data.get('email')
        password = self.cleaned_data.get('password')
        confirm = self.cleaned_data.get('confirm')
        
        if password and confirm and password != confirm:
            raise forms.ValidationError('Passwords do not match!')

        values = {
            'username': username,
            'email': email,
            'password': password
        }
        return values

class LoginForm_Manager(forms.Form):
    username = forms.CharField(max_length = 50, label = 'Username:',
        widget = forms.TextInput(attrs = {'placeholder': 'username'}))
    password = forms.CharField(max_length = 20, label = 'Password:',
        widget = forms.PasswordInput(attrs = {'placeholder': 'password'}))

class BusinessForm(forms.ModelForm):
    class Meta:
        model = models.Business
        fields = ["company", "position", "location", "qualifications"]
