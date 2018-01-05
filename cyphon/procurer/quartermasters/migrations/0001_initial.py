# -*- coding: utf-8 -*-
# Copyright 2017 Dunbar Cybersecurity.
#
# This file is part of Cyphon Engine.
#
# Cyphon Engine is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Cyphon Engine is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Cyphon Engine. If not, see <http://www.gnu.org/licenses/>.
#
# Generated by Django 1.11.2 on 2017-11-02 20:21
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('requisitions', '0001_initial'),
        ('visas', '0001_initial'),
        ('passports', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Quartermaster',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40, unique=True)),
                ('endpoints', models.ManyToManyField(related_name='emissaries', related_query_name='emissary', to='requisitions.Requisition', verbose_name='requisition')),
                ('passport', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='passports.Passport')),
                ('visa', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='visas.Visa')),
            ],
            options={
                'verbose_name': 'quartermaster',
                'verbose_name_plural': 'quartermasters',
            },
        ),
    ]
