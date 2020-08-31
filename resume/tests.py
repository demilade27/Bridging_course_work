from django.test import TestCase
from resume.views import resume
from django.urls import resolve
from blog.views import post_list
from django.template.loader import render_to_string


# Create your tests here.

class ResumeTest(TestCase):
    def test_resume_url_resolves_to_resume_view(self):
        found = resolve('/cv/resume/')
        self.assertEqual(found.func,resume)
    def test_resume_returns_correct_html(self):
        response = self.client.get('/cv/resume/')
        self.assertTemplateUsed(response,'resume/resume.html')


