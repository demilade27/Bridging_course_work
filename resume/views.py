from django.shortcuts import render

from django.utils import timezone

from .models import  Resume

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from .forms import ResumeForm,ProfessionalSkillsForm,EducationForm,LangaugesForm,IntrestForm

from django.shortcuts import render, get_object_or_404

from django.shortcuts import redirect

def resume(request):
    resume = Resume.objects.all()
    return render(request, 'resume/resume.html',{'resume':resume})


def edit_resume(request):
    resume = Resume.objects.all()
    return render(request, 'resume/edit_resume.html', {'resume': resume})


def add_resume(request):
    if request.method == "POST":
        form = ResumeForm(request.POST)
        skillsForm = ProfessionalSkillsForm(request.POST)
        intrestForm=IntrestForm(request.POST)
        langaugesForm= LangaugesForm(request.POST)
        educationForm= EducationForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
        if skillsForm.is_valid():
            skillsForm.save()
        if intrestForm.is_valid():
            intrestForm.save()
        if langaugesForm.is_valid():
            langaugesForm.save()
        if educationForm.is_valid():
            educationForm.save()
        return redirect('resume')

        
    else:
        form = ResumeForm()
        skillsForm = ProfessionalSkillsForm()
        intrestForm=IntrestForm()
        langaugesForm= LangaugesForm()
        educationForm= EducationForm()
    return render(request, 'resume/add_resume.html', {
                                                    'form':ResumeForm(),
                                                    'skillsForm':ProfessionalSkillsForm(),
                                                    'intrestForm':IntrestForm(),
                                                    'langaugesForm':LangaugesForm(),
                                                    'educationForm':EducationForm()
                                                    }
                                                        )

