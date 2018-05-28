from django.db import models
from django.urls import reverse
from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractUser
from django.conf import settings


class PostManager(models.Manager):
    def draft(self):
        return self.filter(status=0)

    def published(self):
        return self.filter(status=1)

    def featured(self):
        return self.published().filter(featured=True)

    def breaking(self):
        return self.published().filter(breaking=True)

    def popular(self):
        return self.published().order_by('read_count')


def handle_deleted_user():
    return get_user_model().objects.get_or_create(username='Unkown User')[0]


def handle_deleted_catagory():
    return Catagory.objects.get_or_create(title='Uncatagorized')[0]


class CustomUser(AbstractUser):
    avatar = models.ImageField(
        upload_to='users/avatar/',
        null=True, blank=True,
    )


class Base(models.Model):
    created_at = models.DateTimeField(
        'Created date',
        auto_now_add=True,
        help_text='Record created date',
    )
    updated_at = models.DateTimeField(
        'Modified date',
        auto_now=True,
        help_text='Record last updated date',
    )

    class Meta:
        abstract = True


class Catagory(Base):
    title = models.CharField(max_length=120)
    translation = models.CharField(max_length=60)
    slug = models.SlugField()

    class Meta:
        verbose_name = 'News Catagory'
        verbose_name_plural = 'News Catagories'
        ordering = ['title', '-updated_at', ]

    def __str__(self):
        return self.title

    def get_absolute_url(self, *args, **kwargs):
        return reverse('news:catagory-detail', args=[str(self.pk)])


class Tag(Base):
    title = models.CharField(max_length=120)
    translation = models.CharField(max_length=60)
    slug = models.SlugField()

    class Meta:
        ordering = ['title', '-updated_at', ]

    def __str__(self):
        return self.title


class Post(Base):
    STATUS_OPTIONS = (
        (0, 'Draft'),
        (1, 'Published'),
    )
    catagory = models.ForeignKey(
        Catagory,
        related_name='posts',
        on_delete=models.SET(handle_deleted_catagory)
    )
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name='posts',
        null=True, blank=True,
        on_delete=models.SET_NULL,
    )
    tags = models.ManyToManyField(Tag, blank=True, related_name='posts')
    title = models.CharField(max_length=120)
    translation = models.CharField(max_length=60)
    slug = models.SlugField()
    thumbnail = models.ImageField(upload_to='posts/', null=True, blank=True)
    body = models.TextField(blank=True)
    status = models.PositiveSmallIntegerField(
        choices=STATUS_OPTIONS,
        default=0,
    )
    published_at = models.DateTimeField(null=True, blank=True)
    featured = models.BooleanField(default=False)
    breaking = models.BooleanField(default=False)
    read_count = models.PositiveIntegerField(default=1)

    objects = PostManager()

    class Meta:
        ordering = ['-updated_at', '-status', ]
        get_latest_by = ['-published_at', ]

    def __str__(self):
        return self.title

    def get_absolute_url(self, *args, **kwargs):
        return reverse('news:post-detail', args=[str(self.pk)])


class Comment(Base):
    post = models.ForeignKey(
        Post,
        related_name='comments',
        on_delete=models.CASCADE
    )
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name='comments',
        on_delete=models.SET(handle_deleted_user)
    )
    body = models.TextField('Comment')
    upvotes = models.PositiveIntegerField()
    downvotes = models.PositiveIntegerField()
    published = models.BooleanField(default=True)

    class Meta:
        ordering = ['post', '-updated_at', ]

    def __str__(self):
        return 'Comment by {} on {} at {}'.format(
            self.user,
            self.post,
            self.updated_at
        )


class Reply(Base):
    comment = models.ForeignKey(
        Comment,
        related_name='replies',
        on_delete=models.CASCADE
    )
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name='replies',
        on_delete=models.SET(handle_deleted_user)
    )
    body = models.TextField('Reply')
    upvotes = models.PositiveIntegerField()
    downvotes = models.PositiveIntegerField()
    published = models.BooleanField(default=True)

    class Meta:
        ordering = ['comment', '-updated_at', ]

    def __str__(self):
        return 'Reply by {} at {}'.format(
            self.user,
            self.updated_at
        )


# class League(Base):
#     name = models.CharField(max_length=60)
#     full_name = models.CharField(max_length=100, blank=True)
#     logo = models.ImageField(upload_to='leages/', blank=True, null=True)
#     description = models.TextField(blank=True)
#     country = CountryField()
#     featured = models.BooleanField(default=False)

#     class Meta:
#         ordering = ['-featured', 'name', ]

#     def __str__(self):
#         return self.name

#     def get_absolute_url(self, *args, **kwargs):
#         return reverse('news:league-detail', args=[str(self.pk)])


# class Player(Base):
#     PLAYING_POSITION_OPTIONS = (
#         ('GK', 'Goal Keeper'),
#         ('RB', 'Right Back'),
#         ('RWB', 'Right Wing Back'),
#         ('CB', 'Center Back'),
#         ('LB', 'Left Back'),
#         ('RWB', 'Right Wing Back'),
#         ('DM', 'Defensive Mid-fielder'),
#         ('CM', 'Central Mid-fielder'),
#         ('ACM', 'Attacking Center Mid-fielder'),
#         ('LW', 'Left Wing'),
#         ('RW', 'Right Wing'),
#         ('CF', 'Center Forward'),
#     )
#     first_name = models.CharField(max_length=60)
#     last_name = models.CharField(max_length=60)
#     nickname = models.CharField(max_length=60, blank=True)
#     position = models.CharField(max_length=3, choices=PLAYING_POSITION_OPTIONS)
#     bio = models.TextField('Short bio', blank=True)
#     picture = models.ImageField(upload_to='players/')
#     birthdate = models.DateField(blank=True, null=True)
#     country = CountryField()

#     class Meta:
#         ordering = ['last_name', 'first_name', ]

#     def __str__(self):
#         return self.last_name

#     def get_absolute_url(self, *args, **kwargs):
#         return reverse('news:player-detail', args=[str(self.pk)])


# class Team(Base):
#     TEAM_TYPE_OPTIONS = (
#         ('C', 'Club'),
#         ('N', 'National Team'),
#         ('E', 'Exhibition Team'),
#     )
#     team_type = models.CharField(max_length=1, choices=TEAM_TYPE_OPTIONS)
#     league = models.ForeignKey(
#         League,
#         related_name='teams',
#         null=True, on_delete=models.SET_NULL
#     )
#     country = CountryField()
#     name = models.CharField(max_length=60)
#     full_name = models.CharField(max_length=120, blank=True)
#     nickname = models.CharField(max_length=60, blank=True)
#     logo = models.ImageField(upload_to='teams/logo/', blank=True, null=True)
#     description = models.TextField(blank=True)
#     players = models.ManyToManyField(Player, related_name='teams', blank=True)

#     class Meta:
#         ordering = ['team_type', 'league', 'name', ]

#     def __str__(self):
#         return self.name

#     def get_absolute_url(self, *args, **kwargs):
#         return reverse('news:team-detail', args=[str(self.pk)])


# class Competition(Base):
#     COMPETITION_TYPE_CHOICES = (
#         ('LEAGUE', 'League'),
#         ('PLAYOFF', 'Playoffs'),
#         ('TOURNAMENT', 'Tournament'),
#         ('FRIENDLY', 'Friendly'),
#     )
#     name = models.CharField(max_length=60)
#     league = models.ForeignKey(
#         League,
#         related_name='competitions',
#         null=True, on_delete=models.SET_NULL,
#     )
#     competition_type = models.CharField(
#         max_length=10,
#         choices=COMPETITION_TYPE_CHOICES,
#     )
#     logo = models.ImageField(upload_to='teams/logo/', blank=True, null=True)
#     start_date = models.DateField()
#     end_date = models.DateField()
#     description = models.TextField(blank=True)

#     class Meta:
#         ordering = ['competition_type', ]

#     def __str__(self):
#         return self.name

#     def get_absolute_url(self, *args, **kwargs):
#         return reverse('news:competition-detail', args=[str(self.pk)])


# class Match(Base):
#     competition = models.ForeignKey(
#         Competition,
#         related_name='matches',
#         on_delete=models.CASCADE
#     )
#     name = models.CharField(max_length=60, help_text='Title of the match')
