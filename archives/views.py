from django. shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.template import RequestContext

from archives.models import *
from archives.forms import *

import datetime

# Create your views here.
def relicAdd(request, h_siteID):
	# add the relic now
	rightNow				= datetime.datetime.now()
	# get rid of the microseconds
	rightNow				-= datetime.timedelta(microseconds = rightNow.microsecond)
	theSite				= historical_site.objects.get(pk=h_siteID)
	newRelic			= relic(entered=rightNow, historical_site=theSite,
						latitude=theSite.latitude, longitude=theSite.longitude)
	
	errors					= []
	if request.method == 'POST':
		form				= relicForm(request.POST, instance=newRelic)
		if form.is_valid():		
			
			form.save()
			return HttpResponseRedirect('/archives/')
		# end if
	else:
		form	= relicForm(instance=newRelic) 
	# end if
	
	return render_to_response('archives/relic_form.html', locals(), \
			context_instance=RequestContext(request))
			
# end add_relic