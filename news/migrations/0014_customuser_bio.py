# Generated by Django 2.0.5 on 2018-05-30 18:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0013_auto_20180530_1413'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='bio',
            field=models.TextField(blank=True, verbose_name='Author bio'),
        ),
    ]
