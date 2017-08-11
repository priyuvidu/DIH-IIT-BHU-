# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-14 12:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lan_complain', '0003_remove_question_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='hostel',
            field=models.CharField(blank=True, choices=[('0', 'S.N.Bose '), ('1', 'Aryabhatta '), ('2', 'S. Ramanujan '), ('3', 'C. V. Raman'), ('4', 'Morvi'), ('5', 'Dhanrajgiri'), ('6', 'Rajputana'), ('7', 'Limbdi'), ('8', 'S.C. De'), ('9', 'Vishweshvarayya'), ('10', 'Vivekanand'), ('11', 'Vishwakarma'), ('12', 'Gandhi Smriti Mahila Chhatravas'), ('13', 'New Girls GSMC Extn.'), ('14', 'Saluja')], max_length=100),
        ),
    ]