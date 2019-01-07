from django.db import models

# Create your models here.
class Person(models.Model):
    def __str___(self):
        return self.name
    name = models.CharField(max_length=200)
    want = models.CharField(max_length=200)
    email = models.EmailField()
    group = models.IntegerField()
    pub_date = models.DateTimeField('date published')
    

# class Choice(models.Model):
#     question = models.ForeignKey(Question, on_delete=models.CASCADE)
#     choice_text = models.CharField(max_length=200)
#     votes = models.IntegerField(default=0)
#     def __str___(self):
#         return self.choice_text