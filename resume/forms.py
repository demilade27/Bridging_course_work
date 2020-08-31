from django import forms
from .models import  Resume,ProfessionalSkills,Education,Interest,Langauges

class ResumeForm(forms.ModelForm):
    class Meta:
        model = Resume
        fields = ('full_name', 'address', 'email',
                  'phone_number', 'personal_profile')

class ProfessionalSkillsForm(forms.ModelForm):

    class Meta:
        model = ProfessionalSkills
        fields = ('skill_detail',)
        widgets = {

            'skill_detail': forms.Textarea(attrs={'title': 'Professional Skill'})
        }

class EducationForm(forms.ModelForm):

    class Meta:
        model = Education
        fields = ('degree', 'stream', 'passing_year', 'result')
        widgets = {
            'degree': forms.Select(attrs={'title': 'Degree'}),
            'stream': forms.TextInput(attrs={'title': 'Stream'}),
            'passing_year': forms.DateInput(attrs={'title': 'Passing Date'}),
            'result': forms.TextInput(attrs={'title': 'Result'})
        }
class IntrestForm(forms.ModelForm):
    class Meta:
        model=Interest
        fields = ('area_of_interest_detail',)
        widgets = {
            'area_of_interest_detail': forms.TextInput(attrs={'title': 'Intrest'})
        }
class LangaugesForm(forms.ModelForm):
    class Meta:
        model=Langauges
        fields = ('Language',)
        widgets = {
            'Language': forms.TextInput(attrs={'title': 'Language'})
        }
