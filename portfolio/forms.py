from django import forms
from .models import Summary, Skills, Education, Project, Work


class SummaryForm(forms.ModelForm):
    class Meta:
        model = Summary
        fields = '__all__'


class SkillsForm(forms.ModelForm):
    class Meta:
        model = Skills
        fields = '__all__'


class EducationForm(forms.ModelForm):
    class Meta:
        model = Education
        fields = '__all__'


class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = '__all__'


class WorkForm(forms.ModelForm):
    class Meta:
        model = Work
        fields = '__all__'
