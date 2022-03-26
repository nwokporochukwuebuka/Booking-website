from django.db import models

# Create your models here.
class Appointment(models.Model):

    # FIRST NAME 
    first_name = models.CharField(max_length=50)

    # LAST NAME 
    last_name = models.CharField(max_length=50)

    # EMAIL 
    email = models.CharField(max_length=50)

    # PHONE NUMBER 
    phone = models.CharField(max_length=15)

    # REQUEST / MESSAGE
    request_message = models.TextField(blank=True, null=True)

    # SENT DATE 
    sent_date = models.DateField(auto_now_add=True)

    accepted = models.BooleanField(default=False)

    # ACCEPTED DATE 
    accepted_date = models.DateField(auto_now=True)

    def __str__(self):
        return self.first_name

    class Meta:

        # ORDERING THE DATA ACCORDING TO THE SENT DATE 
        ordering = ["-sent_date"]