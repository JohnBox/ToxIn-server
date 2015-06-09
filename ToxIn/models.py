from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, primary_key=True)
    workplace = models.CharField(max_length=80, blank=True)
    position = models.CharField(max_length=40, blank=True)
    hide_email = models.BooleanField(default=False)

    def __str__(self):
        return '%s %s Profile' % (self.user.first_name, self.user.last_name,)

class Contact(models.Model):
    contact = models.OneToOneField(User, primary_key=True, related_name='contact_id')
    user = models.ForeignKey(User)
    creator = models.BooleanField()
    on = models.BooleanField(default=False)

    def __str__(self):
        return '%s %s contact of %s %s' % (self.contact.first_name,
                                           self.contact.last_name,
                                           self.user.first_name,
                                           self.user.last_name,
                                           )
