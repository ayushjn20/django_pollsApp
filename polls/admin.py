from django.contrib import admin
from polls.models  import Choice, Question
# Register your models here.

class ChoiceInline(admin.StackedInline):
	model = Choice
	extra = 3

class QuestionAdmin(admin.ModelAdmin):
	fieldsets = [
		(None,			{'fields': ['question_text']}),
		('Date informaion', {'fields': ['pub_date'],'classes': ['collapse'] }),
	]
	inlines = [ChoiceInline]
	list_display = ('question_text', 'pub_date', 'was_published_recently')
	list_filter = ['pub_date']
	search_fields = ['question_text']
#display each obj as tuple instead of str()

admin.site.register(Question, QuestionAdmin)
