FileName		= 'forms.py'
# By:			Jason Thorne
# Date:			13-07-2014
# Description: 	The archeologist project
##################################################################
from django import forms
from django.forms.fields import DateField, ChoiceField, MultipleChoiceField
from django.forms.widgets import RadioSelect, CheckboxSelectMultiple, HiddenInput
from django.forms.extras.widgets import SelectDateWidget
from django.core.exceptions import ObjectDoesNotExist
from django.utils.safestring import mark_safe

from archives.models import *
import datetime

###############################################################
class relicForm(forms.ModelForm):
	class Meta:
		model			= relic
		fields			= ['historical_site', 'latitude', 'longitude', 'name', \
						'photo', 'description']						 
	# end Meta
				
# end relicForm