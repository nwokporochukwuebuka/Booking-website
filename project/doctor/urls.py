from django.urls import path
from .import views

urlpatterns = [
    path('', views.HomeTemplateView.as_view(), name='home'),
    path('book_appointment/', views.AppointmentTemplateView.as_view(), name='book'),
    path('manage-appointments/', views.ManageAppointmentTemplateView.as_view(), name='manage')
]