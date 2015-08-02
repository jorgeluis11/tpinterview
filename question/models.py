from django.db import models

from core.models import TimeStampedModel

# Create your models here.
class Language(TimeStampedModel):
    language = models.CharField(max_length=55, unique=True, blank=False)
    status = models.BooleanField(default=True)

    def __unicode__(self):
        return self.language


# Create your models here.
class Exam(TimeStampedModel):
    name = models.CharField(max_length=55, unique=True, blank=False)
    language = models.ForeignKey(Language)
    status = models.BooleanField(default=True)

    def __unicode__(self):
        return self.name


# Create your models here.
class Question(TimeStampedModel):
    question = models.CharField(max_length=255, blank=False)
    exam = models.ForeignKey(Exam)
    order = models.IntegerField()

    def __unicode__(self):
        return self.question


# Create your models here.
class Candidate(TimeStampedModel):
    first_name = models.CharField(max_length=55, blank=False)
    last_name = models.CharField(max_length=55, blank=False)

    def __unicode__(self):
        return self.question


# Create your models here.
class Answer(TimeStampedModel):
    answer = models.CharField(max_length=255, blank=False)
    question = models.ForeignKey(Question)
    candidate = models.ForeignKey(Candidate)
    order = models.IntegerField()

    def __unicode__(self):
        return self.answer
