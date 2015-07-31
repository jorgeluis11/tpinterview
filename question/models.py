from django.db import models


# Create your models here.
class Language(models.Model):
    language = models.CharField(max_length=55, unique=True, blank=False)

    def __unicode__(self):
        return self.language


# Create your models here.
class Exam(models.Model):
    name = models.CharField(max_length=55, unique=True, blank=False)
    language = models.ForeignKey(Language)

    def __unicode__(self):
        return self.name


# Create your models here.
class Question(models.Model):
    question = models.CharField(max_length=255, blank=False)
    exam = models.ForeignKey(Exam)
    order = models.IntegerField()

    def __unicode__(self):
        return self.question


# Create your models here.
class Candidate(models.Model):
    first_name = models.CharField(max_length=55, blank=False)
    last_name = models.CharField(max_length=55, blank=False)

    def __unicode__(self):
        return self.question


# Create your models here.
class Answer(models.Model):
    answer = models.CharField(max_length=255, blank=False)
    question = models.ForeignKey(Question)
    candidate = models.ForeignKey(Candidate)
    order = models.IntegerField()

    def __unicode__(self):
        return self.answer
