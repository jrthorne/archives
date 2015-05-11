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
class loginForm(forms.Form):
    username        = forms.CharField(widget=forms.Textarea(\
        attrs={'rows':'1', 'cols':'50', 'autofocus':''}), max_length=20, required=True)
    password        = forms.CharField(widget=forms.PasswordInput, max_length=20, required=True)
# end loginForm

###############################################################
class relicForm(forms.ModelForm):
	class Meta:
		model			= relic
		fields			= ['historical_site', 'latitude', 'longitude', 'name', \
						'photo', 'media_file', 'media_link', 'description']						 
	# end Meta
	
	description = forms.CharField(widget=forms.Textarea(\
		attrs={'rows':'10', 'cols':'30'}), required=False)
				
# end relicForm