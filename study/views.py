###################################################################
FileName        = 'views.py'
# By:            Nan JIN
# Date:            30-06-2015
# Description:     The archeologist project - Usability Testing
##################################################################

from django. shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.template import RequestContext
from django.contrib.auth.models import User
from django.contrib import auth
import string # for use in filtering non printing characers
from django.conf import settings
from django.contrib.auth.decorators import login_required

from study.models import *
from study.forms import *

import datetime

##################################################################
def surveyList(request):
    # used in context
    BING_KEY        = settings.BING_KEY
    surveyList      = survey.objects.all()
    
    return render_to_response('study/index.html', locals())
# end siteList

##################################################################
def choiceQuestion(request,survey_id):
    BING_KEY        = settings.BING_KEY
    surveyList      = survey.objects.all()
    theSurvey      = survey.objects.get(pk=survey_id)
    
    return render_to_response('study/choiceQuestion.html', locals())
# end choice_question
##################################################################
def participantReg(request,survey_id):
    context         = RequestContext(request)
    # used in context
    BING_KEY        = settings.BING_KEY
    surveyList      = survey.objects.all()
    theSurvey       = survey.objects.get(pk=survey_id)
    regNum          = request.POST.get('registerNumber',9999)
    site            = request.POST.get('historicalSite')
    theTask         = request.POST.get('task')
    rightNow        = datetime.datetime.now()
    newParticipant  = participant(registerNumber=regNum,historicalSite=site,task=theTask,entered=rightNow)
    
    # Get the context from the request.
    context = RequestContext(request)
    
    errors      = []
    
    if request.method == 'POST':
        form = participantForm(request.POST, instance=newParticipant)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/study/mcq' + survey_id + '/')
            # end if
    else:
        form = participantForm(instance=newParticipant)
    # end if

    return render_to_response('study/participantForm.html', locals(),context)
# end participant_form