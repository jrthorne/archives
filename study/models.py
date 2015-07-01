##################################################################
FileName        = 'models.py'
# By:              Nan JIN
# Date:            30-06-2015
# Description:     The archeologist project - Usability Testing
##################################################################
from django.db import models
from django.contrib.auth.models import User
from sorl.thumbnail import ImageField

import archeologist.settings
#####################################################################
# Create your models here.
#####################################################################

##############################################################
class survey(models.Model):
    name            = models.CharField(max_length=80)
    description     = models.TextField(blank=True)

    def __unicode__(self):
        return self.name
    # end __unicode__

#end survey

##############################################################
class question(models.Model):
    questionText    = models.CharField(max_length=300)
    
    survey          = models.ForeignKey(survey,null=True,blank=True)
    
    def __unicode__(self):
        return self.questionText
# end __unicode__

#end question


##############################################################
class questionChoice(models.Model):
    questionChoiceText  = models.CharField(max_length=300)
    
    survey          = models.ForeignKey(survey,null=True,blank=True)
    question        = models.ForeignKey(question,null=True,blank=True)
    
    def __unicode__(self):
        return self.questionChoiceText
# end __unicode__

#end questionChoice

##############################################################
class participant(models.Model):
    registerNumber  = models.IntegerField(max_length=4)
    
    historicalSite  = models.CharField(max_length=80)
    task            = models.CharField(max_length=10)
    
    def __unicode__(self):
        return self.registerNumber
# end __unicode__

#end participant

##############################################################
class choiceAnswer(models.Model):
    registerNumber  = models.ForeignKey(participant,null=True,blank=True)
    
    survey          = models.ForeignKey(survey,null=True,blank=True)
    question        = models.ForeignKey(question,null=True,blank=True)
    questionChoice  = models.ForeignKey(questionChoice,null=True,blank=True)
    
    def __unicode__(self):
        return self.registerNumber
# end __unicode__

#end choiceAnswer

##############################################################
class freeAnswer(models.Model):
    registerNumber  = models.ForeignKey(participant,null=True,blank=True)
    
    survey          = models.ForeignKey(survey,null=True,blank=True)
    question        = models.ForeignKey(question,null=True,blank=True)
    answerText      = models.TextField(blank=True)
    
    def __unicode__(self):
        return self.registerNumber
# end __unicode__

