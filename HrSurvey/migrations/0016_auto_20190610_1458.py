# Generated by Django 2.2.1 on 2019-06-10 09:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('HrSurvey', '0015_auto_20190610_1438'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='responses',
            name='employee',
        ),
        migrations.DeleteModel(
            name='Employee',
        ),
    ]
