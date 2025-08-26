from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Booking

class CustomUserCreationUserForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        fields = UserCreationForm.Meta.fields + ('email',)

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['num_of_seats']

    def __init__ (self,*args,**kwargs):
        self.travel_option = kwargs.pop('travel_option',None)
        super().__init__(*args,**kwargs)

    def clean_num_of_seats(self):
        num_of_seats = self.cleaned_data.get('num_of_seats')
        if num_of_seats > self.travel_option.available_seats:
            raise forms.ValidationError("Not enough available seats.")
        return num_of_seats
    



