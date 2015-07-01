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
