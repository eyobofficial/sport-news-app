# Generated by Django 2.0.5 on 2018-05-27 10:07

from django.db import migrations, models
import django.db.models.deletion
import django_countries.fields


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Competition',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, help_text='Record created date', verbose_name='Created date')),
                ('updated_at', models.DateTimeField(auto_now=True, help_text='Record last updated date', verbose_name='Modified date')),
                ('name', models.CharField(max_length=60)),
                ('competition_type', models.CharField(choices=[('LEAGUE', 'League'), ('PLAYOFF', 'Playoffs'), ('TOURNAMENT', 'Tournament'), ('FRIENDLY', 'Friendly')], max_length=10)),
                ('logo', models.ImageField(blank=True, null=True, upload_to='teams/logo/')),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('description', models.TextField(blank=True)),
            ],
            options={
                'ordering': ['competition_type'],
            },
        ),
        migrations.CreateModel(
            name='League',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, help_text='Record created date', verbose_name='Created date')),
                ('updated_at', models.DateTimeField(auto_now=True, help_text='Record last updated date', verbose_name='Modified date')),
                ('name', models.CharField(max_length=60)),
                ('full_name', models.CharField(blank=True, max_length=100)),
                ('logo', models.ImageField(blank=True, null=True, upload_to='leages/')),
                ('description', models.TextField(blank=True)),
                ('country', django_countries.fields.CountryField(max_length=2)),
                ('featured', models.BooleanField(default=False)),
            ],
            options={
                'ordering': ['-featured', 'name'],
            },
        ),
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, help_text='Record created date', verbose_name='Created date')),
                ('updated_at', models.DateTimeField(auto_now=True, help_text='Record last updated date', verbose_name='Modified date')),
                ('first_name', models.CharField(max_length=60)),
                ('last_name', models.CharField(max_length=60)),
                ('nickname', models.CharField(blank=True, max_length=60)),
                ('position', models.CharField(choices=[('GK', 'Goal Keeper'), ('RB', 'Right Back'), ('RWB', 'Right Wing Back'), ('CB', 'Center Back'), ('LB', 'Left Back'), ('RWB', 'Right Wing Back'), ('DM', 'Defensive Mid-fielder'), ('CM', 'Central Mid-fielder'), ('ACM', 'Attacking Center Mid-fielder'), ('LW', 'Left Wing'), ('RW', 'Right Wing'), ('CF', 'Center Forward')], max_length=3)),
                ('bio', models.TextField(blank=True, verbose_name='Short bio')),
                ('picture', models.ImageField(upload_to='players/')),
                ('birthdate', models.DateField(blank=True, null=True)),
                ('country', django_countries.fields.CountryField(max_length=2)),
            ],
            options={
                'ordering': ['last_name', 'first_name'],
            },
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, help_text='Record created date', verbose_name='Created date')),
                ('updated_at', models.DateTimeField(auto_now=True, help_text='Record last updated date', verbose_name='Modified date')),
                ('team_type', models.CharField(choices=[('C', 'Club'), ('N', 'National Team'), ('E', 'Exhibition Team')], max_length=1)),
                ('country', django_countries.fields.CountryField(max_length=2)),
                ('name', models.CharField(max_length=60)),
                ('full_name', models.CharField(blank=True, max_length=120)),
                ('nickname', models.CharField(blank=True, max_length=60)),
                ('logo', models.ImageField(blank=True, null=True, upload_to='teams/logo/')),
                ('description', models.TextField(blank=True)),
                ('league', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='teams', to='news.League')),
                ('players', models.ManyToManyField(blank=True, related_name='teams', to='news.Player')),
            ],
            options={
                'ordering': ['team_type', 'league', 'name'],
            },
        ),
        migrations.AddField(
            model_name='customuser',
            name='avatar',
            field=models.ImageField(blank=True, null=True, upload_to='users/avatar/'),
        ),
        migrations.AddField(
            model_name='competition',
            name='league',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='competitions', to='news.League'),
        ),
    ]
