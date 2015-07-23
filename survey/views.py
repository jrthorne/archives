from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.core import urlresolvers
from django.contrib import messages
import datetime
from django.conf import settings

from survey.models import *
from survey.forms import *

from django.forms import Field
from django.utils.translation import ugettext_lazy

Field.default_error_messages = {
    'required': ugettext_lazy("Please fill out this field."),
}


def Index(request):
    BING_KEY        = settings.BING_KEY
    surveyList      = Survey.objects.all()
    
    return render_to_response('survey/index.html',locals())


def SurveyDetail(request, id):
    survey = Survey.objects.get(id=id)
    category_items = Category.objects.filter(survey=survey)
    #categories = [c.name for c in category_items]
    if request.method == 'POST':
        form = ResponseForm(request.POST, survey=survey)
        if form.is_valid():
            response = form.save()
            if int(id)==1 :
                return HttpResponseRedirect("/survey/confirmPre/"+ response.registerNumber )
            if int(id)==2 :
                return HttpResponseRedirect("/survey/confirmPost/"+ response.registerNumber )
            else:
                return HttpResponseRedirect('/survey/')
    else:
        form = ResponseForm(survey=survey)
        print format
        
    return render(request, 'survey/survey.html', {'response_form': form, 'survey': survey, 'category_items': category_items})

def ConfirmPre(request):
    return render(request, 'survey/confirmPre.html')

def ConfirmPost(request):
    return render(request, 'survey/confirmPost.html')

