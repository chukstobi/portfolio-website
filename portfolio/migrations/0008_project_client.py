# Generated by Django 3.2.3 on 2022-02-27 10:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0007_project_project_pic'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='client',
            field=models.CharField(default=None, max_length=1000),
        ),
    ]