from django import forms

from django.contrib.auth import get_user_model

User = get_user_model()

from .models import UserAddress


class UserAddressForm(forms.ModelForm):
	default = forms.BooleanField(label='Default Address')
	class Meta:
		model = UserAddress
		fields = ["address", 
				"address2", 
				"city", 
				"state", 
				"country",
				"zipcode", 
				"phone",
				"billing"]

class LoginForm(forms.Form):
	
	username = forms.CharField()
	password = forms.CharField(widget=forms.PasswordInput())


	def clean_username(self):
		username = self.cleaned_data.get("username")
		try:
			user = User.objects.get(username=username)
		except User.DoesNotExist:
			raise forms.ValidationError("Invalid username!")

		return username

	def clean_password(self):
		username = self.cleaned_data.get("username")
		password = self.cleaned_data.get("password")

		try:
			user = User.objects.get(username=username)
		except:
			user = None
		if user is not None and not user.check_password(password):
			raise forms.ValidationError("Invalid password!")
		elif user is None:
			pass
		else:
			return password
 
class RegistrationForm(forms.ModelForm):
	email = forms.EmailField(label='Your Email')
	first_name = forms.CharField(label="First Name",max_length=30)
	last_name = forms.CharField(label="Last Name",max_length=30)
	password1 = forms.CharField(label='Password', widget=forms.PasswordInput())	
	password2 = forms.CharField(label='Password Confirmation', widget=forms.PasswordInput())
	
	class Meta:
		model = User
		fields = ['username', 'email', 'first_name', 'last_name']

	def clean_password2(self):
		password1 = self.cleaned_data.get("password1")
		password2 = self.cleaned_data.get("password2")
		if password1 and password2 and password1 != password2:
			raise forms.ValidationError("Password does not match!")
		return password2

	def save(self, commit=True):
		user = super(RegistrationForm, self).save(commit=False)
		user.set_password(self.cleaned_data['password1'])

		if commit:
			user.save()
		return user

















