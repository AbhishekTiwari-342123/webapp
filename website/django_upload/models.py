# Create your models here.
# Create your models here.
from django.db import models
from django.forms import ModelForm


class Theory_Assignment(models.Model):
    Date = models.CharField(max_length=100, default="null")
    Theory_Assignment = models.FileField()
    submit_Date = models.CharField(max_length=100, default="null")

    def __str__(self):
        return self.Theory_Assignment


class Lab_Assignment(models.Model):
    Date = models.CharField(max_length=100, default="null")
    Lab_Assignment = models.FileField()
    Lab_Optional_Assignment = models.FileField()

    def __str__(self):
        return self.Lab_Assignment


class Theory_Lectures(models.Model):
    Date = models.CharField(max_length=100, default="null")
    Theory_Lectures = models.FileField()
    Video_lectures = models.FileField()

    def __str__(self):
        return self.Theory_Lectures


class Lab_Lectures(models.Model):
    Date = models.CharField(max_length=100, default="null")
    Lab_lectures = models.FileField()

    def __str__(self):
        return self.Lab_lectures


# FileUpload form class.
class theory_a(ModelForm):
    class Meta:
        model = Theory_Assignment
        fields = ('Date', 'Theory_Assignment', 'submit_Date')


class lab_a(ModelForm):
    class Meta:
        model = Lab_Assignment
        fields = ('Date', 'Lab_Assignment', 'Lab_Optional_Assignment')


class theory_l(ModelForm):
    class Meta:
        model = Theory_Lectures
        fields = ('Date', 'Theory_Lectures', 'Video_lectures')


class lab_l(ModelForm):
    class Meta:
        model = Lab_Lectures
        fields = ('Date', 'Lab_lectures')

