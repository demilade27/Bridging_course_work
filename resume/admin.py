from django.contrib import admin
from .models import Resume,ProfessionalSkills,Interest,Education,Langauges

# Register your models here.
admin.site.register(Resume)
admin.site.register(ProfessionalSkills)
admin.site.register(Interest)
admin.site.register(Education)
admin.site.register(Langauges)
