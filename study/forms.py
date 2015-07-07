##################################################################
FileName        = 'forms.py'
# By:            Nan JIN
# Date:            30-06-2015
# Description:     The archeologist project - Usability Testing
##################################################################
from django import forms
from django.forms.fields import DateField, ChoiceField, MultipleChoiceField
from django.forms.widgets import RadioSelect, CheckboxSelectMultiple, HiddenInput
from django.forms.extras.widgets import SelectDateWidget
from django.core.exceptions import ObjectDoesNotExist
from django.utils.safestring import mark_safe

from study.models import *
import datetime


###############################################################
class participantForm(forms.ModelForm):
    class Meta:
        model            = participant
        fields            = ['registerNumber', 'historicalSite', 'task']
    # end Meta
    
# participantForm

###############################################################
class questionForm(forms.ModelForm):
    class Meta:
        model            = participant
        fields            = ['registerNumber', 'historicalSite', 'task']
# end Meta
#    labels = {'name': _('Writer'),}
#    help_texts = {'name': _('Some useful help text.'),}
#    error_messages = {'name': {'max_length': _("This writer's name is too long."),},
#}

# participantForm