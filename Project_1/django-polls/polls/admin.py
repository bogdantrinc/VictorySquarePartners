from django.contrib import admin

from .models import Question, QuestionAdmin, Choice

admin.site.register(Question, QuestionAdmin)

# Register your models here.
