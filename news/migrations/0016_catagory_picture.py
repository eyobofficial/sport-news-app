# Generated by Django 2.0.5 on 2018-06-02 17:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0015_auto_20180530_1838'),
    ]

    operations = [
        migrations.AddField(
            model_name='catagory',
            name='picture',
            field=models.ImageField(blank=True, upload_to='catagory/pictures/'),
        ),
    ]