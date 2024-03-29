# Generated by Django 2.2.1 on 2019-06-07 09:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('HrSurvey', '0012_responses'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='responses',
            name='option_id',
        ),
        migrations.AddField(
            model_name='responses',
            name='answer',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='responses',
            name='option',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='option_id', to='HrSurvey.Option'),
        ),
    ]
