from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import DetailView 
from .models import ProjectImageUpload, Summary, Skill, Education, Project, Work, Profile, Certification, Service
# Create your views here.


class ProjectDetailView(DetailView):
    model = Project
    context_object_name = 'project'



def index(request):
    summary = Summary.objects.all()
    skills = Skill.objects.all()
    education = Education.objects.filter().order_by("-start_date")
    work = Work.objects.all()
    profile = Profile.objects.all()
    certification = Certification.objects.all()
    project = Project.objects.all()
    services = Service.objects.all()
    

    skills_list_1 = skills[:3]
    skills_list_2 = skills[4:]
   
    context = {
        "summary": summary,
        "skills_1": skills_list_1,
        "skills_2": skills_list_2,
        "education": education,
        "work": work,
        "profile":profile,
        "certification": certification,
        "project":project,
        "services":services,
    
    }

    return render(request, "portfolio/home.html", context)

def project(request, id):
    project = get_object_or_404(Project, id=id)
    photos = ProjectImageUpload.objects.filter(project=project)
    context = {
        "project": project,
        "photos": photos
    }
    return render(request, "portfolio/project_detail.html", context)
