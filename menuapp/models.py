from django.db import models

class Menu(models.Model):
    name = models.CharField(max_length=50)
    
class MenuItem(models.Model):
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE)  
    title = models.CharField(max_length=50)
    url = models.CharField(max_length=200)
    parent = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE)