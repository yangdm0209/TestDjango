#!/usr/bin/env python
# coding: utf-8

from django.contrib import admin
from models import Question, Choice


# Register your models here.

class ChoiceInline(admin.StackedInline):
    model = Choice
    extra = 3

@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ['pk', 'question_text', 'pub_date']
    fields = ['question_text', 'pub_date']
    # fieldsets = [
    #     ('Question Text', {'fields': ['question_text']}),
    #     ('Date information', {'fields': ['pub_date']}),
    # ]
    # 在创建Question对象的同时可以直接添加一组Choice
    inlines = [ChoiceInline]


@admin.register(Choice)
class ChoiceAdmin(admin.ModelAdmin):
    list_display = ('pk', 'question', 'choice_text', 'votes')
    fields = ('question', 'choice_text', 'votes')
