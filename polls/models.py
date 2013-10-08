from django.db import models
import datetime

# Create your models here.

class Poll(models.Model):
    question = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    list_display = ('question', 'pub_date', 'fue_publicado_hoy')

    def __str__(self):
        return self.question

    def was_published_today(self):
        return self.pub_date.date() == datetime.date.today()




class Choice(models.Model):
    poll = models.ForeignKey(Poll)
    choice = models.CharField(max_length=200)
    votes = models.IntegerField()

    def __str__(self):
        return self.choice