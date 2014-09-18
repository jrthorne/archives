from django. shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.template import RequestContext
from django.contrib.auth.models import User
import string # for use in filtering non printing characers

from archives.models import *
from archives.forms import *

import datetime

# Create your views here.
#################################################################
def siteList(request):
	siteList		= historical_site.objects.all()
	
	return render_to_response('archives/index.html', locals())
# end siteList	

#################################################################
# all the relics for the given historical site (hsite_id)
def relicList(request, hsite_id):
	print hsite_id
	theSite			= historical_site.objects.get(pk=hsite_id)
	relicSet		= theSite.relic_set.all()
	for r in relicSet:
		r.name		= filter(lambda x: x in string.printable, r.name)
		r.description		= filter(lambda x: x in string.printable, r.description)

	return render_to_response('archives/relic_list.html', locals())

# end relicList

##################################################################
def relicAdd(request, h_siteID):
	# add the relic now
	rightNow			= datetime.datetime.now()
	# get rid of the microseconds
	rightNow			-= datetime.timedelta(microseconds = rightNow.microsecond)
	theSite				= historical_site.objects.get(pk=h_siteID)
	relicSet			= theSite.relic_set.all()
	u					= User.objects.get(first_name="Manolya")
	a					= archeologist.objects.get(user=u)
	newRelic			= relic(entered=rightNow, historical_site=theSite,
						latitude=theSite.latitude, longitude=theSite.longitude,
						archeologist=a)
	
	errors					= []
	if request.method == 'POST':
		form				= relicForm(request.POST, request.FILES, instance=newRelic)
		if form.is_valid():		
			form.save()
			return HttpResponseRedirect('/archives/' + h_siteID + '/')
		# end if
	else:
		form	= relicForm(instance=newRelic) 
	# end if
	
	form.fields['latitude'].widget 	= forms.HiddenInput()
	form.fields['longitude'].widget = forms.HiddenInput()
	
	return render_to_response('archives/relic_form.html', locals(), \
			context_instance=RequestContext(request))
			
# end relicAdd

##################################################################
def relicMod(request, relicID):
	theRelic			= get_object_or_404(relic, pk=relicID)
	theSite				= theRelic.historical_site
	h_siteID			= str(theSite.id)
	relicSet			= theSite.relic_set.all()
	
	
	errors					= []
	if request.method == 'POST':
		form				= relicForm(request.POST, request.FILES, instance=theRelic)
		if form.is_valid():			
			form.save()
			return HttpResponseRedirect('/archives/' + h_siteID + '/')
		# end if
	else:
		form	= relicForm(instance=theRelic) 
	# end if
	
	form.fields['latitude'].widget 	= forms.HiddenInput()
	form.fields['longitude'].widget = forms.HiddenInput()
	
	return render_to_response('archives/relic_form.html', locals(), \
			context_instance=RequestContext(request))
			
# end relicMod