#!/usr/bin/env python
# coding: utf-8

import datetime
from django.db import models

from django.utils import timezone


# Create your models here.
class Question(models.Model):
    question_text = models.CharField(max_length=200, verbose_name=u'问题')
    pub_date = models.DateTimeField(verbose_name=u'发布日期')

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

    class Meta:
        verbose_name = u'问题'
        verbose_name_plural = u'问题'


class Choice(models.Model):
    question = models.ForeignKey(Question)
    choice_text = models.CharField(max_length=200, verbose_name=u'选项')
    votes = models.IntegerField(default=0, verbose_name=u'投票')

    def __str__(self):
        return self.choice_text

    class Meta:
        verbose_name = u'选项'
        verbose_name_plural = u'选项'
