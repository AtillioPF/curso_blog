# Generated by Django 3.2.5 on 2021-07-29 23:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='subtitle',
            field=models.CharField(default='', max_length=300),
        ),
    ]
