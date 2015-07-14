from django. shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.template import RequestContext
from django.contrib.auth.models import User
from django.contrib import auth
import string # for use in filtering non printing characers
from django.conf import settings
from django.contrib.auth.decorators import login_required

from archives.models import *
from archives.forms import *

import datetime

# Create your views here.
#########################################
# login taken from http://www.djangobook.com/en/beta/chapter12/
def login(request):    
    
    # r90 check to see if already logged on
    if request.user.is_authenticated():
        return HttpResponseRedirect('/')
    # end if 
    
    usernameKey                = 'username'
    passwordKey                = 'password'

    # If we submitted the form
    if request.method == 'POST':
        # get the posted data
        form        = loginForm(request.POST)
        if form.is_valid():
            cd        = form.cleaned_data
            # I need some logic to check username/password
            myUser        = auth.authenticate(username=cd[usernameKey], password=cd[passwordKey])
            if myUser is not None and myUser.is_active:
                # Log them in
                auth.login(request, myUser)
                # login_required sets the next URL parameter.
                if 'next' in request.GET and request.GET['next']:
                    nextURL = request.GET['next']
                else:
                    nextURL = reverse('siteList')
                # end if
                return HttpResponseRedirect(nextURL) 
            else:
                return HttpResponse('Login failed <a href="/archives/login/">Try again</a>')
            # end if
        # end if
        
    else:
        form                = loginForm()
    # end if
    
    return render_to_response('archives/login_form.html', locals(), \
            context_instance=RequestContext(request))
# end login


#########################################
def logout(request):
    auth.logout(request)
    # delete the user
    request.user            = None
    return HttpResponseRedirect(reverse('siteList'))
# end logout

#################################################################
def siteList(request):
    user = request.user
    # used in context
    BING_KEY        = settings.BING_KEY
    siteList        = historical_site.objects.all()
    
    return render_to_response('archives/index.html', locals())
# end siteList    

#################################################################
# all the relics for the given historical site (hsite_id)
def relicList(request, hsite_id):
    # used in context
    BING_KEY        = settings.BING_KEY
    theSite            = historical_site.objects.get(pk=hsite_id)
    relicSet        = theSite.relic_set.all()
    for r in relicSet:
        r.name        = filter(lambda x: x in string.printable, r.name)
        r.description        = filter(lambda x: x in string.printable, r.description)

    return render_to_response('archives/relic_list.html', locals())

# end relicList

##################################################################
@login_required()
def relicAdd(request, h_siteID):
    # used in context
    BING_KEY        = settings.BING_KEY
    # add the relic now
    rightNow            = datetime.datetime.now()
    # get rid of the microseconds
    rightNow            -= datetime.timedelta(microseconds = rightNow.microsecond)
    theSite                = historical_site.objects.get(pk=h_siteID)
    relicSet            = theSite.relic_set.all()
    u                    = User.objects.get(first_name="Manolya")
    a                    = archeologist.objects.get(user=u)
    newRelic            = relic(entered=rightNow, historical_site=theSite,
                        latitude=theSite.latitude, longitude=theSite.longitude,
                        archeologist=a)
    
    errors                    = []
    if request.method == 'POST':
        form                = relicForm(request.POST, request.FILES, instance=newRelic)
        if form.is_valid():        
            form.save()
            return HttpResponseRedirect('/archives/' + h_siteID + '/')
        # end if
    else:
        form    = relicForm(instance=newRelic) 
    # end if
    
    form.fields['latitude'].widget     = forms.HiddenInput()
    form.fields['longitude'].widget = forms.HiddenInput()
    
    return render_to_response('archives/relic_form.html', locals(), \
            context_instance=RequestContext(request))
            
# end relicAdd

##################################################################
@login_required()
def relicMod(request, relicID):
    # used in context
    BING_KEY        = settings.BING_KEY
    theRelic            = get_object_or_404(relic, pk=relicID)
    theSite                = theRelic.historical_site
    h_siteID            = str(theSite.id)
    relicSet            = theSite.relic_set.all()
    
    
    errors                    = []
    if request.method == 'POST':
        form                = relicForm(request.POST, request.FILES, instance=theRelic)
        if form.is_valid():            
            form.save()
            return HttpResponseRedirect('/archives/' + h_siteID + '/')
        # end if
    else:
        form    = relicForm(instance=theRelic) 
    # end if
    
    form.fields['latitude'].widget     = forms.HiddenInput()
    form.fields['longitude'].widget = forms.HiddenInput()
    
    return render_to_response('archives/relic_form.html', locals(), \
            context_instance=RequestContext(request))
            
# end relicMod