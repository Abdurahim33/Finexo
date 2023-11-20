from django.db import models

class Home(models.Model):
    title=models.CharField(max_length=200)
    sub_title=models.CharField(max_length=250)
    title2=models.CharField(max_length=100)
    icons=models.ImageField('')


def __str__(self) -> str:
    return self.title


class About(models.Model):
    title=models.CharField(max_length=20)
    main_title=models.CharField(max_length=20)
    sub_title=models.CharField(max_length=400)

def __str__(self) -> str:
    return self.title


class Service(models.Model):
    title=models.CharField(max_length=400)
    icon=models.ImageField('')
    icon_title=models.CharField(max_length=100)

def __str__(self) -> str:
    return self.title

class Why(models.Model):
    title=models.CharField(max_length=20)
    icon=models.ImageField(upload_to='Why/%Y/%m/%d')
    sub_title=models.CharField(max_length=200)

def __str__(self) -> str:
    return self.title


class Team(models.Model):
    image=models.ImageField(upload_to='Team/%Y/%m/%d')
    title=models.CharField(max_length=200)

    
def __str__(self) -> str:
    return self.title


