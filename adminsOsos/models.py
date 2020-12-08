from django.db import models
from usersOsos.models import User

# Create your models here.

class Admin(models.Model):
    admin_id            = models.AutoField(primary_key=True)
    first_name          = models.CharField(max_length = 30, null = False)
    last_name           = models.CharField(max_length = 60, null = False)
    phone_number        = models.CharField(max_length = 13, null = True)
    user                = models.OneToOneField(User, on_delete = models.CASCADE)    # * OK