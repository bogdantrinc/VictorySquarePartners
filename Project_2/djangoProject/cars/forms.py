from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class RegisterUser(UserCreationForm):
	first_name = forms.CharField(
		max_length=12, min_length=4, required=True,
		widget=forms.TextInput(
			attrs={'class': 'form-control', 'placeholder': 'John'}))
	last_name = forms.CharField(
		max_length=12, min_length=4, required=True,
		widget=(forms.TextInput(
			attrs={'class': 'form-control', 'placeholder': 'Doe'})))
	address = forms.CharField(
		max_length=12, min_length=4,
		widget=(forms.TextInput(
			attrs={'class': 'form-control'})))
	email = forms.EmailField(
		max_length=50,
		widget=(forms.TextInput(
			attrs={'class': 'form-control', 'placeholder': 'john.doe@email.com'})))
	password1 = forms.CharField(
		label='Password',
		widget=forms.PasswordInput(
			attrs={'class': 'form-control'}))
	password2 = forms.CharField(
		label='Password confirmation',
		help_text='Enter the same password as before, for verification.',
		widget=forms.PasswordInput(
			attrs={'class': 'form-control'}))

	class Meta:
		model = User
		fields = ('username', 'first_name', 'last_name', 'address', 'email', 'password1', 'password2')

	def save(self, commit=True):
		user = super(RegisterUser, self).save(commit=False)
		user.email = self.cleaned_data['email']
		if commit:
			user.save()
		return user

	def clean(self):
		super(RegisterUser, self).clean()
		email = self.cleaned_data.get('email')
		if User.objects.filter(email=email).exists():
			raise ValidationError("Email exists!")
		return self.cleaned_data
