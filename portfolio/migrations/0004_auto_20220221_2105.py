# Generated by Django 3.2.3 on 2022-02-21 20:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0003_auto_20220221_2049'),
    ]

    operations = [
        migrations.AlterField(
            model_name='work',
            name='end_date',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='work',
            name='key_achievements',
            field=models.TextField(null=True),
        ),
    ]