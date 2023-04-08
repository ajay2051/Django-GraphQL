from django.contrib import admin
from .models import Category, Quizzes, Question, Answer


# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']


class QuizAdmin(admin.ModelAdmin):
    list_display = ['id', 'title']


class AnswerInlineModel(admin.TabularInline):
    model = Answer
    fields = [
        'answer_text',
        'is_right'
    ]


class QuestionAdmin(admin.ModelAdmin):
    fields = [
        'title',
        'quiz',
    ]
    list_display = [
        'title',
        'quiz',
    ]
    inlines = [
        AnswerInlineModel,
    ]


class AnswerAdmin(admin.ModelAdmin):
    list_display = [
        'answer_text',
        'is_right',
        'question'
    ]


admin.site.register(Category, CategoryAdmin)
admin.site.register(Quizzes, QuizAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Answer, AnswerAdmin)
