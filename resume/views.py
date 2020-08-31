from django.shortcuts import render

from django.utils import timezone

from .models import  Resume,ProfessionalSkills,Interest,Langauges,Education,WorkExperience

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from .forms import ResumeForm,ProfessionalSkillsForm,EducationForm,LangaugesForm,IntrestForm,WorkForm

from django.shortcuts import render, get_object_or_404

from django.shortcuts import redirect

def resume(request):
    personal_info = Resume.objects.all()
    skills= ProfessionalSkills.objects.all()
    interest=Interest.objects.all()
    langauges= Langauges.objects.all()
    education= Education.objects.all()
    work =WorkExperience.objects.all()

    return render(request, 'resume/resume.html',{'personal_info':personal_info,
                                                'skills':skills,
                                                'interesti':interest,
                                               'langauges':langauges, 
                                                'education':education,
                                                'work':work
                                                })


def edit_resume(request):
    resume = Resume.objects.all()
    return render(request, 'resume/edit_resume.html', {'resume': resume})


def add_resume(request):
    if request.method == "POST":
        personal_info_form = ResumeForm(request.POST)
        skills_form1 = ProfessionalSkillsForm(request.POST)
        skills_form2 = ProfessionalSkillsForm(request.POST)
        skills_form3 = ProfessionalSkillsForm(request.POST)
        interest_form1=IntrestForm(request.POST)
        interest_form2=IntrestForm(request.POST)
        interest_form3=IntrestForm(request.POST)
        langauges_form1= LangaugesForm(request.POST)
        langauges_form2= LangaugesForm(request.POST)
        langauges_form3= LangaugesForm(request.POST)
        education_form1= EducationForm(request.POST)
        education_form2= EducationForm(request.POST)
        education_form3= EducationForm(request.POST)
        workexperience1= WorkForm(request.POST)
        workexperience2= WorkForm(request.POST)
        workexperience3= WorkForm(request.POST)

        if personal_info_form.is_valid():
            post = personal_info_form.save(commit=False)
            post.author = request.user
            post.save()
        if skills_form1.is_valid():
            skills_form1.save()
        if interest_form1.is_valid():
            interest_form1.save()
        if langauges_form1.is_valid():
            langauges_form1.save()
        if education_form1.is_valid():
            education_form1.save()
        if skills_form2.is_valid():
            skills_form2.save()
        if interest_form2.is_valid():
            interest_form2.save()
        if langauges_form2.is_valid():
            langauges_form2.save()
        if education_form2.is_valid():
            education_form2.save()
        if skills_form3.is_valid():
            skills_form3.save()
        if interest_form3.is_valid():
            interest_form3.save()
        if langauges_form3.is_valid():
            langauges_form3.save()
        if education_form3.is_valid():
            education_form3.save()
        if workexperience1.is_valid():
            workexperience1.save()
        if workexperience2.is_valid():
            workexperience2.save()
        if workexperience3.is_valid():
            workexperience3.save()
        return redirect('resume')
 
    else:
        personal_info_form = ResumeForm()
        skills_form1 = ProfessionalSkillsForm()
        interest_form1=IntrestForm()
        langauges_form1= LangaugesForm()
        education_form1= EducationForm()
        skills_form2 = ProfessionalSkillsForm()
        interest_form2=IntrestForm()
        langauges_form2= LangaugesForm()
        education_form2= EducationForm()
        skills_form3 = ProfessionalSkillsForm()
        interest_form3=IntrestForm()
        langauges_form3= LangaugesForm()
        education_form3= EducationForm()
        workexperience1= WorkForm()
        workexperience2= WorkForm()
        workexperience3= WorkForm()

        
    return render(request, 'resume/add_resume.html',
        context= {                                  'personal_info_form':personal_info_form,
                                                    'skills1':skills_form1,
                                                    'interest1':interest_form1,
                                                    'langauges1':langauges_form1,
                                                    'education1':education_form1, 
                                                    'skills2':skills_form2,
                                                    'interest2':interest_form2,
                                                    'langauges2':langauges_form2,
                                                    'education2':education_form2,
                                                    'skills3':skills_form3,
                                                    'interest3':interest_form3,
                                                    'langauges3':langauges_form3,
                                                    'education3':education_form3,        
                                                    'work1':workexperience1,
                                                    'work2': workexperience2,
                                                    'work3': workexperience3   } )

