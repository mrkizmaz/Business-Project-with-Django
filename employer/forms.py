from django import forms
from employer import models

class RegisterForm_Employer(forms.Form):
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

class LoginForm_Employer(forms.Form):
    username = forms.CharField(max_length = 50, label = 'Username:',
        widget = forms.TextInput(attrs = {'placeholder': 'username'}))
    password = forms.CharField(max_length = 20, label = 'Password:',
        widget = forms.PasswordInput(attrs = {'placeholder': 'password'}))

class EmployerForm(forms.ModelForm):
    class Meta:
        model = models.Employer
        fields = ["username", "position_int", "location", "skills", "resume"]
