FileName		= 'forms.py'
# By:			Jason Thorne
# Date:			13-07-2014
# Description: 	The archeologist project
##################################################################
from django import forms
from django.forms.fields import DateField, ChoiceField, MultipleChoiceField
from django.forms.widgets import RadioSelect, CheckboxSelectMultiple
from django.forms.extras.widgets import SelectDateWidget
from django.core.exceptions import ObjectDoesNotExist
from django.utils.safestring import mark_safe

from archives.models import *
import datetime

###############################################################
class relicForm(forms.ModelForm):
	class Meta:
		model			= relic
		fields			= ['historical_site', 'latitude', 'longitude', \
						'archeologist', 'entered', 'name', \
						'type', 'related_to','photo', 'description', 'period' ]
						 
	# end Meta
	
	entered				= forms.DateTimeField(widget=forms.DateTimeInput(\
						attrs={ 'size' : 25, 'autocomplete': 'off'}),\
						required=True)
				
	"""photo				= forms.FileField( \
						label='Select a photo', \
						required=False
						)"""
# end relicForm