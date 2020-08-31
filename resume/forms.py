from django import forms
from .models import  Resume,ProfessionalSkills,Education,Interest,Langauges,WorkExperience

class ResumeForm(forms.ModelForm):
    class Meta:
        model = Resume
        fields = ('full_name', 'address', 'email',
                  'phone_number', 'personal_profile')

class ProfessionalSkillsForm(forms.ModelForm):

    class Meta:
        model = ProfessionalSkills
        fields = ('skill',)

class EducationForm(forms.ModelForm):

    class Meta:
        model = Education
        fields = ('level','degree', 'course','name','start_year','end_year','result')

class IntrestForm(forms.ModelForm):
    class Meta:
        model=Interest
        fields = ('intrest',)

class LangaugesForm(forms.ModelForm):
    class Meta:
        model=Langauges
        fields = ('Language',)
class WorkForm(forms.ModelForm):
    class Meta:
        model=WorkExperience
        fields = ('job','company','position','start_year','end_year','description')