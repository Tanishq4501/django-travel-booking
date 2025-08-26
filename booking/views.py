from django.shortcuts import render,redirect,get_object_or_404
from django.views.generic import CreateView
from .models import TravelOption,Booking
from django.contrib.auth.models import User
from .forms import CustomUserCreationUserForm,BookingForm
from django.urls import reverse_lazy
from django.db import transaction
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView,LogoutView

# Create your views here.

def home(request):
    travel_options = TravelOption.objects.filter(available_seats__gt=0)

    source = request.GET.get('source')
    destination = request.GET.get('destination')
    travel_type = request.GET.get('type')

    
    # .strip() removes any accidental leading/trailing whitespace from user input
    if source:
        travel_options = travel_options.filter(source__icontains=source.strip())
    
    if destination:
        travel_options = travel_options.filter(destination__icontains=destination.strip())
    
    # Check if a travel_type was selected and it's not empty
    if travel_type:
        # __iexact is a case-insensitive exact match, which is safer
        travel_options = travel_options.filter(type__iexact=travel_type)

    return render(request,'booking/home.html',{'travel_options':travel_options})

class SignUpView(CreateView):
    form_class=  CustomUserCreationUserForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'
    model = User

@login_required
def book_travel(request,travel_id):
    travel_options = get_object_or_404(TravelOption,id =travel_id)

    if request.method == 'POST':
        form = BookingForm(request.POST,travel_option=travel_options)
        if form.is_valid():
            try:
                with transaction.atomic():
                    booking = form.save(commit=False)
                    booking.user = request.user
                    booking.travel_option = travel_options
                    booking.total_price = travel_options.price * booking.num_of_seats

                    travel_options.refresh_from_db()
                    if booking.num_of_seats > travel_options.available_seats:
                        messages.error(request,'Sorry, the requested number of seats are no longer available.')
                        return redirect('home')
                    
                    travel_options.available_seats -= booking.num_of_seats
                    travel_options.save()
                    booking.save()

                    messages.success(request,'Booking confirmed')
                    return redirect('my_bookings')
            except Exception as e:
                messages.error(request,f"An error occured: {e}")

    else:
        form = BookingForm(travel_option = travel_options)
    return render(request,'booking/book_travel.html',{'form':form,'travel_option':travel_options})

@login_required
def my_bookings(request):
    bookings = Booking.objects.filter(user=request.user).order_by('-booking_date')
    return render(request,'booking/my_bookings.html',{'bookings':bookings})

@login_required
def cancel_booking(request,booking_id):
    booking = get_object_or_404(Booking,id=booking_id,user=request.user)

    if booking.status == 'Confirmed':
        with transaction.atomic():
            booking.status = 'Cancelled'
            booking.save()
            booking.travel_options.available_seats += booking.num_of_seats
            booking.travel_options.save()
            messages.success(request,'Booking has been cancelled.')
    else:
        messages.error(request,'This booking cannot be cancelled.')

    return redirect('my_bookings')






