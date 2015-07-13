from django.db import models
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator
import archeologist.settings

class Survey(models.Model):
	name = models.CharField(max_length=400)
	description = models.TextField(blank=True, null=True,)

	def __unicode__(self):
		return (self.name)

	def questions(self):
		if self.pk:
			return Question.objects.filter(survey=self.pk)
		else:
			return None

class Category(models.Model):
    name            = models.CharField(max_length=400)
    description     = models.TextField(blank=True, null=True,)
    survey          = models.ForeignKey(Survey)

    def __unicode__(self):
		return (self.name)

def validate_list(value):
	'''takes a text value and verifies that there is at least one comma '''
	values = value.split(',')
	if len(values) < 2:
		raise ValidationError("The selected field requires an associated list of choices. Choices must contain more than one item.")

class Question(models.Model):
	TEXT = 'text'
	RADIO = 'radio'
	SELECT = 'select'
	SELECT_MULTIPLE = 'select-multiple'
	INTEGER = 'integer'

	QUESTION_TYPES = (
		(TEXT, 'text'),
		(RADIO, 'radio'),
		(SELECT, 'select'),
		(SELECT_MULTIPLE, 'Select Multiple'),
		(INTEGER, 'integer'),
	)

	text = models.TextField()
	required = models.BooleanField()
	category = models.ForeignKey(Category, blank=True, null=True,)
	survey = models.ForeignKey(Survey)
	question_type = models.CharField(max_length=200, choices=QUESTION_TYPES, default=TEXT)
	# the choices field is only used if the question type 
	choices = models.TextField(blank=True, null=True,
		help_text='if the question type is "radio," "select," or "select multiple" provide a comma-separated list of options for this question .')

	def save(self, *args, **kwargs):
		if (self.question_type == Question.RADIO or self.question_type == Question.SELECT 
			or self.question_type == Question.SELECT_MULTIPLE):
			validate_list(self.choices)
		super(Question, self).save(*args, **kwargs)

	def get_choices(self):
		''' parse the choices field and return a tuple formatted appropriately
		for the 'choices' argument of a form widget.'''
		choices = self.choices.split(',')
		choices_list = []
		for c in choices:
			c = c.strip()
			choices_list.append((c,c))
		choices_tuple = tuple(choices_list)
		return choices_tuple

	def __unicode__(self):
		return (self.text)

class Response(models.Model):
	TASK_CHOICE = (('1','Adding landmarks'),('2','Visiting landmarks'))
	SITE_CHOICE = (('1','The Rocks'),('2','Manly Quarantine Station'))


	registerNumber  = models.CharField(validators=[RegexValidator(regex='^(?!9999)[0-9]{4}$',message='The register number has 4 figures',code='nomatch')],max_length=4)
	site  = models.CharField(max_length=400,choices=SITE_CHOICE)
	task= models.CharField(max_length=400,choices=TASK_CHOICE)
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)
	survey = models.ForeignKey(Survey)
    
        
	def __unicode__(self):
		return ("response %s" % self.registerNumber)

class AnswerBase(models.Model):
    question = models.ForeignKey(Question)
    response = models.ForeignKey(Response)
    created = models.DateTimeField(auto_now_add=True)

# these type-specific answer models use a text field to allow for flexible
# field sizes depending on the actual question this answer corresponds to. any
# "required" attribute will be enforced by the form.
class AnswerText(AnswerBase):
	body = models.TextField(blank=True, null=True)

class AnswerRadio(AnswerBase):
	body = models.TextField(blank=True, null=True)

class AnswerSelect(AnswerBase):
	body = models.TextField(blank=True, null=True)

class AnswerSelectMultiple(AnswerBase):
	body = models.TextField(blank=True, null=True)

class AnswerInteger(AnswerBase):
	body = models.IntegerField(blank=True, null=True)








