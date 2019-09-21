# Generated by Django 2.2.4 on 2019-09-20 17:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0005_auto_20190903_0520'),
    ]

    operations = [
        migrations.AlterField(
            model_name='experience',
            name='OrgName',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='index.OrgBaseInfo'),
        ),
        migrations.AlterField(
            model_name='orgbaseinfo',
            name='Region',
            field=models.CharField(blank=True, choices=[('Addis Adabba', 'ada'), ('Johannesburg', 'jhn'), ('Something', 'smt')], default='ada', help_text='Region of the company', max_length=30),
        ),
    ]
