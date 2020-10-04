from django.contrib import admin

# Register your models here.
from polls.models import Question, Choice


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = (
        "question_text",
        "pub_date"
    )
    list_per_page = 2


admin.site.register(Choice)
