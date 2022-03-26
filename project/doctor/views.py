from django.core.mail import EmailMessage
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from django.conf import settings
from doctor.models import Appointment
import datetime
from django.template.loader import render_to_string, get_template
from django.template import Context

# Create your views here.


class HomeTemplateView(TemplateView):
    '''This view is responsible for receiving the posted information on the 
    homepage otherwise known as index.'''

    template_name = 'index.html'

    def post(self, request):
        name = request.POST.get("name")
        email = request.POST.get("email")
        message = request.POST.get("message")

        email = EmailMessage(
            subject= f"{name} from doctor family.",
            body=message,
            from_email=settings.EMAIL_HOST_USER,
            to=[settings.EMAIL_HOST_USER],
            reply_to=[email]
        )
        email.send()
        return HttpResponse("Email sent successfully!")

class AppointmentTemplateView(TemplateView):
    template_name = 'book_appointment.html'

    def post(self, request):
        '''This is responsible for receiving informations when we post or immediately
        we hit the submit button.'''

        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        email = request.POST.get('email')
        mobile = request.POST.get('mob')
        message = request.POST.get('ans')

        # next we create an appointment object and store in our database with a special id
        appointment = Appointment.objects.create(
            first_name=fname,
            last_name=lname,
            email=email,
            phone=mobile,
            request_message=message,
        )

        appointment.save()

        '''After filling the form and clicking the submit button, we acknowledge that
        the email has been sent and response will be received shortly'''

        messages.add_message(request, messages.SUCCESS, f'Thanks {fname}, \nYour appointment has been sent. You will receive a date shortly.')
        return HttpResponseRedirect(request.path)

        '''After this the user wil be redirected to the same page'''


class ManageAppointmentTemplateView(ListView):
    template_name = 'manage_appointments.html'
    model = Appointment

    context_object_name = 'appointments'

    login_required = True
    paginate_by = 2


    def post(self, request):
        date = request.POST.get("date")
        appointment_id = request.POST.get("appointment-id")

        appointment = Appointment.objects.get(id=appointment_id)
        appointment.accepted = True
        appointment.accepted_date = datetime.datetime.now()
        appointment.save()

        data = {
            'fname': appointment.first_name,
            'date': date
        }

        message = get_template('email.html').render(data)

        email = EmailMessage(
            "About your appointment",
            message,
            settings.EMAIL_HOST_USER,
            [appointment.email],
        )
        email_content_subtype = 'html'
        email.send()

        messages.add_message(request, messages.SUCCESS, f"You accepted the appointment of {appointment.first_name}")
        return HttpResponseRedirect(request.path)


    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        appointments = Appointment.objects.all()
        context.update({'title': 'Manage Appointments'})
        return context