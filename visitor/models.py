from django.db import models

# Create your models here.

class Input(models.Model):
    your_name = models.CharField(max_length=50 ,null = False,blank=False) #,choices=('Sharukan','Vijay','Ajith')
    partner_name = models.CharField(max_length=50 ,null = False,blank =False)#,choices=['Deepika','Trisha','Shalini']

    result = models.CharField(max_length=210 , blank = True,null = True)
    
    def __str__(self) -> str:
        return f'---{self.your_name}-----{self.partner_name}---{self.result}----'