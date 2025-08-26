from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('signup/',views.SignUpView.as_view(),name='signup'),
    path('book/<int:travel_id>/',views.book_travel,name='book_travel'),
    path('my-bookings/',views.my_bookings,name='my_bookings'),
    path('my-bookings/cancel/<int:booking_id>/',views.cancel_booking,name='cancel_booking')
]