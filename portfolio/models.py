from email.policy import default
from django.db import models
from django.contrib.auth.models import User
from PIL import Image
# Create your models here.


class Summary(models.Model):
    description = models.TextField()


class Skill(models.Model):
    skill = models.CharField(max_length=1000, default=None)
    level = models.IntegerField(default=0)

    def __str__(self):
        return self.skill


class Education(models.Model):
    school_name = models.CharField(max_length=1000)
    course = models.CharField(max_length=1000)
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return f"{self.school_name} - {self.course}"


class Project(models.Model):
    title = models.CharField(max_length=1000)
    client = models.CharField(max_length=1000, default=None, null=True)
    category = models.CharField(max_length=1000, default=None)
    description = models.TextField()
    project_pic = models.ImageField(default='default.jpg', upload_to='project_pics')
    project_link = models.URLField(blank=True)
    github_link = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.title


class ProjectImageUpload(models.Model):
    project = models.ForeignKey(Project, default=None, on_delete=models.CASCADE)
    image_upload = models.ImageField(default="default.jpg", upload_to='project_pics')

    def __str__(self):
        return f"{self.project.title} Pictures"


class Work(models.Model):
    company = models.CharField(max_length=1000)
    job_title = models.CharField(max_length=1000)
    job_description = models.TextField()
    key_achievements = models.TextField(null=True)
    start_date = models.DateField()
    end_date = models.DateField(null=True)

    def __str__(self):
        return f"{self.job_title} - {self.company}"

class Profile(models.Model):
    email = models.EmailField()
    mobile = models.CharField(max_length=15)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user

class Service(models.Model):
    title = models.CharField(max_length=500)
    description = models.TextField(default=None)

    
    def __str__(self):
        return self.title

class Certification(models.Model):
    course_name = models.CharField(max_length=1000)
    institution = models.CharField(max_length=1000)
    description = models.TextField(default=None)
    end_date = models.DateField()
    cert_link = models.URLField()

    def __str__(self):
        return self.course_name

class Contact(models.Model):
    name = models.CharField(max_length=1000)
    email = models.EmailField()
    subject = models.CharField(max_length=1000)
    message = models.TextField()

    def __str__(self):
        return f"{self.name} - {self.subject}"