from survey.models import Question, Category, Survey, Response, AnswerText, AnswerRadio, AnswerSelect, AnswerInteger, AnswerSelectMultiple
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

class QuestionInline(admin.TabularInline):
    model = Question
    ordering = ('category',)
    extra = 0

class CategoryInline(admin.TabularInline):
    model = Category
    extra = 0

class SurveyAdmin(admin.ModelAdmin):
    inlines = [CategoryInline, QuestionInline]

class AnswerBaseInline(admin.TabularInline):
    fields = ('question', 'body')
    readonly_fields = ('question',)
    extra = 0

class AnswerTextInline(AnswerBaseInline):
    model= AnswerText  

class AnswerRadioInline(AnswerBaseInline):
    model= AnswerRadio 

class AnswerSelectInline(AnswerBaseInline):
    model= AnswerSelect 

class AnswerSelectMultipleInline(AnswerBaseInline):
    model= AnswerSelectMultiple

class AnswerIntegerInline(AnswerBaseInline):
    model= AnswerInteger 

class ResponseAdmin(admin.ModelAdmin):
    list_display = ('registerNumber', 'created') 
    inlines = [AnswerTextInline, AnswerRadioInline, AnswerSelectInline, AnswerSelectMultipleInline, AnswerIntegerInline]
    # specifies the order as well as which fields to act on 
    readonly_fields = ('survey', 'created', 'updated', 'registerNumber',)

#admin.site.register(Question, QuestionInline)
#admin.site.register(Category, CategoryInline)
admin.site.register(Survey, SurveyAdmin)

admin.site.register(Response, ResponseAdmin)
