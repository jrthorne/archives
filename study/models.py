##################################################################
FileName        = 'models.py'
# By:              Nan JIN
# Date:            30-06-2015
# Description:     The archeologist project - Usability Testing
##################################################################
from django.db import models
from django.contrib.auth.models import User
from sorl.thumbnail import ImageField
from django.core.validators import RegexValidator

import archeologist.settings

##############################################################
class FixedCharField(models.Field):
    def __init__(self, max_length, *args, **kwargs):
        self.max_length = max_length
        super(FixedCharField, self).__init__(max_length=max_length, *args, **kwargs)
    
    def db_type(self):
        return 'char(%s)' % self.max_length

##############################################################
class survey(models.Model):
    name            = models.CharField(max_length=80)
    description     = models.TextField(blank=True)
    
    def __unicode__(self):
        return self.name
    # end __unicode__

#end survey

##############################################################
TYPE_CHOICE = (('MCQ','Multiple-choice Questions'),('FREE QUESTION','Free Questions'),('MAP','Map'))

class questionType(models.Model):
    type    = models.CharField(max_length=200,choices=TYPE_CHOICE)
    
    def __unicode__(self):
        return self.type
# end __unicode__

#end questionType

##############################################################
class question(models.Model):
    questionText    = models.CharField(max_length=300)
    
    survey          = models.ForeignKey(survey,null=True,blank=True)
    type            = models.ForeignKey(questionType,null=True,blank=True)
    
    def __unicode__(self):
        return self.questionText
# end __unicode__

#end question


##############################################################
class choice(models.Model):
    choiceText  = models.CharField(max_length=300)
    
    survey          = models.ForeignKey(survey,null=True,blank=True)
    question        = models.ForeignKey(question,null=True,blank=True)
    
    def __unicode__(self):
        return self.choiceText
# end __unicode__

#end choice

##############################################################
TASK_CHOICE = (('ADDING LANDMARKS','Adding landmarks'),('VISTING LANDMARKS','Visiting landmarks'))
SITE_CHOICE = (('THE ROCKS','The Rocks'),('MAINLY QUARANTINE STATION','Mainly Quarantine Station'))

class participant(models.Model):
    registerNumber  = models.IntegerField(validators=[RegexValidator(regex='^.{4}$', message='Length has to be 4', code='nomatch')])
    entered         = models.DateTimeField()
    
    historicalSite  = models.CharField(max_length=80,choices=TASK_CHOICE)
    task            = models.CharField(max_length=80,choices=SITE_CHOICE)
    
    def __unicode__(self):
        return str(self.registerNumber)
# end __unicode__

#end participant

##############################################################
class choiceAnswer(models.Model):
    registerNumber  = models.ForeignKey(participant,null=True,blank=True)
    survey          = models.ForeignKey(survey,null=True,blank=True)
    question        = models.ForeignKey(question,null=True,blank=True)
    questionChoice  = models.ForeignKey(choice,null=True,blank=True)
    
    def __unicode__(self):
        return str(self.registerNumber)+" "+self.questionChoice
# end __unicode__

#end choiceAnswer

##############################################################
class freeAnswer(models.Model):
    answerText      = models.TextField(blank=True)
   
    registerNumber  = models.ForeignKey(participant,null=True,blank=True)
    survey          = models.ForeignKey(survey,null=True,blank=True)
    question        = models.ForeignKey(question,null=True,blank=True)
    
    
    def __unicode__(self):
        return str(self.registerNumber)+" "+self.answerText
# end __unicode__
#end choiceAnswer
##############################################################
class map(models.Model):
    photo           = ImageField(upload_to='photo', blank=True, null=True)
    
    registerNumber  = models.ForeignKey(participant,null=True,blank=True)
        
    def __unicode__(self):
        return str(self.registerNumber)+"Map"
# end __unicode__

#end map


