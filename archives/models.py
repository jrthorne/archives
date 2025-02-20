##################################################################
FileName        = 'models.py'
# By:            Jason Thorne
# Date:            11-03-2012
# Description:     The archeologist project
##################################################################
from django.db import models
from django.contrib.auth.models import User
from sorl.thumbnail import ImageField

import archeologist.settings
#####################################################################
# Create your models here.
#####################################################################
###############################################################
# This class extends the user class. 
##############################################################
class archeologist(models.Model):
    # one to one with django user. You can select any user to be a participant 
    # this way, and I don't have to worry about authentication etc
    user            = models.OneToOneField(User)
    # r46
    postcode        = models.CharField(max_length=80, blank=True)
    country            = models.CharField(max_length=80, blank=True)
    communication_agree = models.BooleanField(help_text="Do you agree to recieve communications from CEDD?")
    
    # r34
    telephone        = models.CharField(max_length=80, help_text="Enter telephone contact details", \
                    blank=True)
    
    def __unicode__(self):
        return self.user.first_name + " " + self.user.last_name 
    # end __unicode
    
# end archeologist

##############################################################
class period(models.Model):
    name                = models.CharField(max_length=255)
    start                = models.IntegerField()
    finish                = models.IntegerField()
    description            = models.TextField(blank=True)
    
    def __unicode__(self):
        return self.name
    # end __unicode__
# end period

##############################################################
class historical_site(models.Model):
    name                = models.CharField(max_length=255)
    country                = models.CharField(max_length=255, blank=True)
    city                = models.CharField(max_length=255, blank=True)
    area                = models.FloatField(null=True, blank=True)
    latitude            = models.FloatField(null=True, blank=True)
    longitude            = models.FloatField(null=True, blank=True)
    #point                 = LocationField(based_fields=[street, suburb, postcode],\
    #                    zoom=12, null=True, suffix='Istanbul')
    
    def __unicode__(self):
        return self.name
    # end __unicode__
# end historical_site

##############################################################
class relic_type(models.Model):
    name                = models.CharField(max_length=255)
    description            = models.TextField(blank=True)
    
    def __unicode__(self):
        return self.name
    # end __unicode__
# end relic_type

##############################################################
class relic(models.Model):
    # person who entered the data
    archeologist        = models.ForeignKey(archeologist, null=True, blank=True)            
    latitude            = models.FloatField(null=True, blank=True)
    longitude            = models.FloatField(null=True, blank=True)
    
    photo                 = ImageField(upload_to='photo', blank=True, null=True)
    media_file            = models.FileField(upload_to='%Y%m%d', \
                        null=True, blank=True)
    media_link            = models.CharField(max_length=255, blank=True, null=True,\
                        help_text="URL to media")
    
    
    # Related relics, the nature of relation could be determined by the through table, eg parent
    related_to            = models.ManyToManyField("self", null=True, blank=True)
    
    entered                = models.DateTimeField() # default of now
    type                = models.ForeignKey(relic_type, null=True, blank=True)
    
    name                = models.CharField(max_length=255)
    historical_site        = models.ForeignKey(historical_site, null=True, blank=True)
    description            = models.TextField(blank=True, null=True)
    period                = models.ForeignKey(period, null=True, blank=True)
    
    def __unicode__(self):
        return self.name
    # end __unicode__
    
# end relic

