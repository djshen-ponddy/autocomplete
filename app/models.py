from django.db import models
from django.conf import settings

class Classroom(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

class Book(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

class Member(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    classroom = models.ForeignKey(Classroom)
    books = models.ManyToManyField(Book, blank=True)

    def __str__(self):
        return 'Classroom: %d, User: %d' % (self.classroom_id, self.user_id)
