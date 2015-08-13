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
class Exam(TimeStampedModel):
    language = models.ForeignKey(Language)
    name = models.CharField(max_length=55, unique=True, blank=False)
    slug = AutoSlugField(populate_from='name', unique=True, max_length=50)
    status = models.BooleanField(default=True)

    def __unicode__(self):
        return self.name


# Create your models here.
class Question(TimeStampedModel):
    exam = models.ForeignKey(Exam)
    question = models.CharField(max_length=255, blank=False)
    order = models.IntegerField()

    def __unicode__(self):
        return self.question


# Create your models here.
class Candidate(TimeStampedModel):
    exam = models.ForeignKey(Exam)
    first_name = models.CharField(max_length=55, blank=False)
    last_name = models.CharField(max_length=55, blank=False)

    def __unicode__(self):
        return self.fist_name

    def fullname(self):
        return self.first_name + " " + self.last_name


# Create your models here.
class Answer(TimeStampedModel):
    question = models.ForeignKey(Question)
    candidate = models.ForeignKey(Candidate)
    answer = models.CharField(max_length=255, blank=False)
    order = models.IntegerField()

    def __unicode__(self):
        return self.answer
