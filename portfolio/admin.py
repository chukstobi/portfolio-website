from django.contrib import admin
from .models import Summary, Skill, Education, Project, Work, Profile, Service, Certification, ProjectImageUpload, Contact
# Register your models here.

admin.site.register(Summary)
admin.site.register(Skill)
admin.site.register(Education)
admin.site.register(Project)
admin.site.register(Work)
admin.site.register(Profile)
admin.site.register(Certification)
admin.site.register(Contact)

