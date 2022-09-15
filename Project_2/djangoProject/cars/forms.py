from django import forms
from django.utils.translation import gettext_lazy as _
from cars.models import Order



class CheckoutForm(forms.ModelForm):

	class Meta:
		model = Order
		exclude = ['status']
		widgets = {
			'customer': forms.Select(attrs={'class': 'form-control', 'readonly': 'readonly'}),
			'product': forms.SelectMultiple(attrs={'class': 'form-control', 'readonly': 'readonly'}),
			'quantity': forms.NumberInput(attrs={'class': 'form-control', 'readonly': 'readonly'}),
			'price': forms.NumberInput(attrs={'class': 'form-control', 'readonly': 'readonly'}),
			'address': forms.TextInput(attrs={'class': 'form-control'}),
		}
		labels = {
			'customer': _('User'),
			'product': _('Products'),
			'address': _('Delivery address'),
		}
		help_texts = {
			'address': _('Enter the address you want your products to be shipped.'),
		}
		error_messages = {
			'customer': {
				'max_length': _("This address is too long."),
			},
		}
