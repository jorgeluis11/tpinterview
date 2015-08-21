from django.db import models

from core.models import TimeStampedModel
from autoslug import AutoSlugField


class Language(TimeStampedModel):
    name = models.CharField(max_length=55, unique=True, blank=False)
    slug = AutoSlugField(populate_from='name', unique=True, max_length=50)
    status = models.BooleanField(default=True)

    def __unicode__(self):
        return self.name


# Create your models here.
class Test(TimeStampedModel):
    language = models.ForeignKey(Language)
    name = models.CharField(max_length=55, unique=True, blank=False)
    slug = AutoSlugField(populate_from='name', unique=True, max_length=50)
    status = models.BooleanField(default=True)

    def __unicode__(self):
        return self.name


# Create your models here.
class Question(TimeStampedModel):
    test = models.ForeignKey(Test)
    question = models.CharField(max_length=255, blank=False)
    order = models.IntegerField()

    def __unicode__(self):
        return self.question


# Create your models here.
class Candidate(TimeStampedModel):
    test = models.ForeignKey(Test)
    name = models.CharField(max_length=55, blank=False)
    slug = AutoSlugField(populate_from='name', unique=True, max_length=50)

    def __unicode__(self):
        return self.name


# Create your models here.
class Answer(TimeStampedModel):
    question = models.ForeignKey(Question)
    candidate = models.ForeignKey(Candidate)
    answer = models.TextField(blank=True)

    def __unicode__(self):
        return self.answer
