# Generated by Django 2.0.5 on 2018-05-27 12:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import news.models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0004_auto_20180527_1202'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, help_text='Record created date', verbose_name='Created date')),
                ('updated_at', models.DateTimeField(auto_now=True, help_text='Record last updated date', verbose_name='Modified date')),
                ('body', models.TextField(verbose_name='Comment')),
                ('upvotes', models.PositiveIntegerField()),
                ('downvotes', models.PositiveIntegerField()),
                ('published', models.BooleanField(default=True)),
            ],
            options={
                'ordering': ['post', '-updated_at'],
            },
        ),
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ['-updated_at', '-status']},
        ),
        migrations.AddField(
            model_name='comment',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='news.Post'),
        ),
        migrations.AddField(
            model_name='comment',
            name='user',
            field=models.ForeignKey(on_delete=models.SET(news.models.handle_deleted_user), related_name='comments', to=settings.AUTH_USER_MODEL),
        ),
    ]
