from django.db import models
from django.urls import reverse

from news.models import Tag

from django_countries.fields import CountryField


class Base(models.Model):
    created_at = models.DateTimeField(
        'Created date',
        null=True, blank=True,
        auto_now_add=True,
        help_text='Record created date',
    )
    updated_at = models.DateTimeField(
        'Modified date',
        null=True, blank=True,
        auto_now=True,
        help_text='Record last updated date',
    )

    class Meta:
        abstract = True


class Team(Base):
    TEAM_TYPE_OPTIONS = (
        ('CLUB', 'Club'),
        ('NATIONAL', 'National Team'),
        ('EXHIBITION', 'Exhibition Team'),
    )
    team_type = models.CharField(max_length=10, choices=TEAM_TYPE_OPTIONS)
    country = CountryField()
    name = models.CharField(max_length=60)
    translation = models.CharField(max_length=100)
    slug = models.SlugField()
    nickname = models.CharField(max_length=60, blank=True)
    logo = models.ImageField(upload_to='teams/logo/', blank=True, null=True)
    description = models.TextField(blank=True)

    class Meta:
        ordering = ['team_type', 'name', ]

    def __str__(self):
        return self.name

    def get_absolute_url(self, *args, **kwargs):
        return reverse('news:team-detail', args=[str(self.pk), self.slug])


class Competition(Base):
    COMPETITION_TYPE_CHOICES = (
        ('LEAGUE', 'League'),
        ('PLAYOFF', 'Playoffs'),
        ('TOURNAMENT', 'Tournament'),
        ('FRIENDLY', 'Friendly'),
    )
    name = models.CharField(max_length=60)
    translation = models.CharField(max_length=100)
    slug = models.SlugField()
    competition_type = models.CharField(
        max_length=10,
        choices=COMPETITION_TYPE_CHOICES,
    )
    logo = models.ImageField(upload_to='teams/logo/', blank=True, null=True)
    start_date = models.DateField()
    end_date = models.DateField()
    description = models.TextField(blank=True)
    is_featured = models.BooleanField(default=False)

    class Meta:
        ordering = ['competition_type', 'name', ]

    def __str__(self):
        return self.name

    def get_absolute_url(self, *args, **kwargs):
        return reverse('news:competition-detail', args=[str(self.pk), self.slug])


class Match(Base):
    STATUS_CHOICE_OPTIONS = (
        ('UPCOMING', 'Upcoming'),
        ('PLAYED', 'Played'),
        ('SUSPENDED', 'Suspended'),
    )
    competition = models.ForeignKey(
        Competition,
        related_name='matches',
        on_delete=models.CASCADE
    )
    title = models.CharField(
        max_length=60,
        null=True,
        help_text='Title of the match'
    )
    translation = models.CharField(max_length=100)
    slug = models.SlugField()
    description = models.TextField('Short match summary', blank=True)
    match_status = models.CharField(
        max_length=10,
        choices=STATUS_CHOICE_OPTIONS,
        default='UPCOMING',
    )
    match_date = models.DateTimeField()
    venue = models.CharField(max_length=100)
    first_team = models.ForeignKey(
        Team,
        related_name='home_matches',
        on_delete=models.CASCADE,
    )
    first_team_score = models.PositiveIntegerField(null=True, blank=True)
    second_team = models.ForeignKey(
        Team,
        related_name='away_matches',
        on_delete=models.CASCADE,
    )
    second_team_score = models.PositiveIntegerField(null=True, blank=True)
    tags = models.ManyToManyField(Tag, related_name='matches')
    is_featured = models.BooleanField(default=False)

    class Meta:
        ordering = ['is_featured', 'title', ]

    def __str__(self):
        return '{} vs {} - {}'.format(
            self.first_team,
            self.second_team,
            self.title
        )

    def get_absolute_url(self, *args, **kwargs):
        return reverse('competitions:match-detail', args=[str(self.pk), self.slug])


