# Generated by Django 2.0.5 on 2018-05-27 13:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0006_auto_20180527_1332'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='is_featured',
            new_name='featured',
        ),
        migrations.AddField(
            model_name='post',
            name='published_at',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
