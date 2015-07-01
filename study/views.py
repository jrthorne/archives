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

# Create your views here.
##################################################################
def surveyList(request):
    # used in context
    BING_KEY        = settings.BING_KEY
    surveyList      = survey.objects.all()
    
    return render_to_response('study/index.html', locals())
# end siteList

##################################################################
def questionnaire(request,survey_id):
    # used in context
    BING_KEY        = settings.BING_KEY
    surveyList      = survey.objects.all()
    theSurvey      = survey.objects.get(pk=survey_id)
    
    return render_to_response('study/questionnaire.html', locals())
# end questionnaire