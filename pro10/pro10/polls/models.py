
from django.db import models

class Question (models.Model):
    question_=models.CharField(max_length=200);
    models.DateTimeField('data published');
    
    
class choice(models.Model):
    question=models.ForeignKey(Question,on_delete=models.CASCADE)
                            
    choice_text = models.CharField(max_length=200)
   
    votes = models.IntegerField(default=0)