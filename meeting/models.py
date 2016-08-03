#!/usr/bin/env python
# coding: utf-8

from django.db import models


# Create your models here.

class MeetingRoom(models.Model):
    """
    会议室
    """
    title = models.CharField(max_length=255, verbose_name="会议室名称", default="")
    channel_name = models.CharField(max_length=128, verbose_name="频道名称", default="")
    ice_host = models.CharField(max_length=128, verbose_name="ICE地址", default="")
    ice_port = models.IntegerField(verbose_name="ICE端口", default="80")
    ice_mount = models.CharField(max_length=128, verbose_name="ICE Mount", default="")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "会议室"  # 对象名字的复数
        verbose_name = "会议室"  # 该对象的一个可读性更好的唯一名字


class OutuptServer(models.Model):
    """
    输出服务器
    """
    mroom = models.ForeignKey("MeetingRoom", verbose_name='会议室')
    url = models.CharField(max_length=255, verbose_name="输出地址", default="")

    def __str__(self):
        return self.mroom.title

    class Meta:
        verbose_name = "输出服务器"
        verbose_name_plural = "输出服务器"


class Meeting(models.Model):
    """
    会议
    """
    mroom = models.ForeignKey("MeetingRoom", verbose_name="会议室")
    title = models.CharField(max_length=255, verbose_name="会议标题")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "云会议"
        verbose_name_plural = "云会议"
