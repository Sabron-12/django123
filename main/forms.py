from django import forms

class UserForm(forms.Form):
    name = forms.CharField( label=" Ваше имя",   required=True, initial="Максим",min_length=2,max_length=30)
    surname = forms.CharField(  label=" Ваша фамилия",    required=True,  initial="Эллипс",min_length=2,max_length=30)
    age=forms.IntegerField( label="Ваш возраст", required=True,   initial="20",min_value=14,max_value=99)
    login=forms.EmailField( label="Электронный адрес",   required=True, initial="example@mail.ru",min_length=2,max_length=30)
    password = forms.CharField(widget=forms.PasswordInput())

