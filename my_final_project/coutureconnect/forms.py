from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
# from .models import Profile

from .models import coutureconnect, Review
class OrderForm(ModelForm):
    class Meta:
        model = coutureconnect
        fields = '__all__'

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields =['username','email','password1','password2']

class ReviewForm(forms.ModelForm):
    stars = forms.ChoiceField(choices=[(i, str(i)) for i in range(1, 6)], widget=forms.RadioSelect())

    class Meta:
        model = Review
        fields = ('stars', 'comment')  

class ThreadForm(forms.Form):
    username = forms.CharField(label='', max_length=100)
class MessageForm(forms.Form):
    message = forms.CharField(label='', max_length=1000)  



# class ProfileForm(forms.ModelForm):
#     class Meta:
#         model = Profile
#         fields = ['bio', 'location', 'birth_date', 'profile_picture']    


class EditProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username','email' ] 






