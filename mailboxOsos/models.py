from django.db import models

# Create your models here.

class Message(models.Model):
    message_id          = models.AutoField(primary_key=True)
    message_title       = models.CharField(max_length = 45, null = False)
    message_content     = models.CharField(max_length = 1000, null = True)      # ? maybe models.TextField() ?
    posting_date        = models.DateField(null = False)
    sender_mail         = models.ForeignKey('Mail', on_delete = models.CASCADE, related_name='sender')      # * OK
    receiver_mail       = models.ForeignKey('Mail', on_delete = models.CASCADE, related_name='receiver')    # * OK

    # https://stackoverflow.com/questions/2606194/django-error-message-add-a-related-name-argument-to-the-definition

    # * e.g. manufacturer = models.ForeignKey('Manufacturer',on_delete=models.CASCADE,)

class Mail(models.Model):
    mail_id             = models.CharField(primary_key=True, max_length = 70, null = False)     # e.g. 248845@student.pwr.edu.pl
