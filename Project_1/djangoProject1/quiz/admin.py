from django.contrib import admin
from .models import Question, QuestionAdmin

admin.site.register(Question, QuestionAdmin)

# Register your models here.
