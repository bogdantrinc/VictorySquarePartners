from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, AuthenticationForm, PasswordResetForm
from accounts.models import User


class RegisterUser(UserCreationForm):
	email = forms.EmailField(
		max_length=50,
		widget=(forms.TextInput(
			attrs={'class': 'form-control', 'placeholder': 'john.doe@email.com'})))
	first_name = forms.CharField(
		max_length=12, min_length=2, required=True,
		widget=forms.TextInput(
			attrs={'class': 'form-control', 'placeholder': 'John'}))
	last_name = forms.CharField(
		max_length=12, min_length=2, required=True,
		widget=(forms.TextInput(
			attrs={'class': 'form-control', 'placeholder': 'Doe'})))
	address = forms.CharField(
		widget=(forms.TextInput(
			attrs={'class': 'form-control'})))
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
		fields = ('email', 'first_name', 'last_name', 'address', 'password1', 'password2')


class EditUser(UserChangeForm):
	email = forms.EmailField(
		max_length=50,
		widget=(forms.TextInput(
			attrs={'class': 'form-control'})))
	first_name = forms.CharField(
		max_length=12, min_length=2, required=True,
		widget=forms.TextInput(
			attrs={'class': 'form-control'}))
	last_name = forms.CharField(
		max_length=12, min_length=2, required=True,
		widget=(forms.TextInput(
			attrs={'class': 'form-control'})))
	address = forms.CharField(
		widget=(forms.TextInput(
			attrs={'class': 'form-control'})))


	class Meta:
		model = User
		fields = ('email', 'first_name', 'last_name', 'address')


class FormAuthentication(AuthenticationForm):

	def __init__(self, request=None, *args, **kwargs):
		super().__init__(request=request, *args, **kwargs)
		self.fields['username'].widget.attrs.update({'class': 'form-control'})
		self.fields['password'].widget.attrs.update({'class': 'form-control'})


class FormPasswordReset(PasswordResetForm):

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.fields['email'].widget.attrs.update({'class': 'form-control'})
