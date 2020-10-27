from django.db import models
from ckeditor.fields import RichTextField

class Category(models.Model):
    title = models.CharField(max_length=200)
    description = RichTextField()
    actives = [
        ('0', 'Inactive'),
        ('1', 'Active')
    ]    
    active = models.CharField(max_length=1, choices=actives, default='1')
    def __str__(self):
        return '%s : %s' % (self.title, self.active)       

class Tableone(models.Model):
    id_cat = models.ForeignKey(Category, on_delete=models.CASCADE)
    tipe = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    description = RichTextField()
    other = models.CharField(max_length=200)
    actives = [
        ('0', 'Inactive'),
        ('1', 'Active')
    ]    
    active = models.CharField(max_length=1, choices=actives, default='1')
    def __str__(self):
        return '%s : %s' % (self.title, self.active)

class Tabletwo(models.Model):
    id_cat = models.ForeignKey(Category, on_delete=models.CASCADE)
    tipe = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    description = RichTextField()
    other = models.CharField(max_length=200)
    actives = [
        ('0', 'Inactive'),
        ('1', 'Active')
    ]    
    active = models.CharField(max_length=1, choices=actives, default='1')
    def __str__(self):
        return '%s : %s' % (self.title, self.active)