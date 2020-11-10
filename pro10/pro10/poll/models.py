from unittest.util import _MAX_LENGTH
from django.db import models

class Question (models.Model):
    question_=models.CharField(max_length=200);
    models.dateTimeField('data published');
    
    
class choice(models.Model):
    question=models.ForeigKey(Question,on_delete=models.CASCADE)
                            
     choice_text=models.CharFields(max_length=200)
     models.integerField(default=0)