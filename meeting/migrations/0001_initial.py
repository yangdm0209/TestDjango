# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Meeting',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=255, verbose_name=b'\xe4\xbc\x9a\xe8\xae\xae\xe6\xa0\x87\xe9\xa2\x98')),
            ],
        ),
        migrations.CreateModel(
            name='MeetingRoom',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(default=b'', max_length=255, verbose_name=b'\xe4\xbc\x9a\xe8\xae\xae\xe5\xae\xa4\xe5\x90\x8d\xe7\xa7\xb0')),
                ('channel_name', models.CharField(default=b'', max_length=128, verbose_name=b'\xe9\xa2\x91\xe9\x81\x93\xe5\x90\x8d\xe7\xa7\xb0')),
                ('ice_host', models.CharField(default=b'', max_length=128, verbose_name=b'ICE\xe5\x9c\xb0\xe5\x9d\x80')),
                ('ice_port', models.IntegerField(default=b'80', verbose_name=b'ICE\xe7\xab\xaf\xe5\x8f\xa3')),
                ('ice_mount', models.CharField(default=b'', max_length=128, verbose_name=b'ICE Mount')),
            ],
        ),
        migrations.CreateModel(
            name='OutuptServer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('url', models.CharField(default=b'', max_length=255, verbose_name=b'\xe8\xbe\x93\xe5\x87\xba\xe5\x9c\xb0\xe5\x9d\x80')),
                ('mroom', models.ForeignKey(verbose_name=b'\xe4\xbc\x9a\xe8\xae\xae\xe5\xae\xa4', to='meeting.MeetingRoom')),
            ],
        ),
        migrations.AddField(
            model_name='meeting',
            name='mroom',
            field=models.ForeignKey(verbose_name=b'\xe4\xbc\x9a\xe8\xae\xae\xe5\xae\xa4', to='meeting.MeetingRoom'),
        ),
    ]
