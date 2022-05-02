from django import forms
#from django.contrib.auth.models import User
from users.models import User

class Registro(forms.Form):
    username=forms.CharField(required=True, min_length=5, max_length=40,
    widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Nombre de usuario'}))
    email=forms.EmailField(required=True,
    widget=forms.EmailInput(attrs={'class':'form-control', 'placeholder':'ejemplo@server.com'}))
    password=forms.CharField(required=True,
    widget=forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'contraseña'}))                         

    password2=forms.CharField(label='repita la contraseña', required=True,
    widget=forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'confirmar contraseña'}))                         
    
    def clean_username(self):
        username=self.cleaned_data.get('username')
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError('Usuario ya creado')
        return username  
    def clean_email(self):
        email=self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('Correo ya registrado')
        return email  
    def clean(self):
        cleaned_data = super().clean()
        if cleaned_data.get('password2')!= cleaned_data.get('password'):
            self.add_error('password2', 'las contraseñas no coinciden')
            
    def save(self):
        return User.objects.create_user(
            self.cleaned_data.get('username'),
            self.cleaned_data.get('email'),
            self.cleaned_data.get('password')
            ) 
    