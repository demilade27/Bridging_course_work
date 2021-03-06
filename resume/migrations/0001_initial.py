# Generated by Django 2.2.15 on 2020-08-31 21:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Resume',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=30)),
                ('address', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=254)),
                ('phone_number', models.CharField(max_length=15)),
                ('personal_profile', models.TextField()),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='WorkExperience',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('job', models.CharField(max_length=50)),
                ('company', models.CharField(max_length=100)),
                ('position', models.CharField(max_length=100)),
                ('start_year', models.CharField(max_length=4)),
                ('end_year', models.CharField(max_length=4)),
                ('description', models.TextField()),
                ('resume', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='resume.Resume')),
            ],
        ),
        migrations.CreateModel(
            name='ProfessionalSkills',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('skill', models.CharField(max_length=60)),
                ('resume', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='resume.Resume')),
            ],
        ),
        migrations.CreateModel(
            name='Langauges',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Language', models.CharField(max_length=15)),
                ('resume', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='resume.Resume')),
            ],
        ),
        migrations.CreateModel(
            name='Interest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('intrest', models.TextField()),
                ('resume', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='resume.Resume')),
            ],
        ),
        migrations.CreateModel(
            name='Education',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('level', models.CharField(max_length=50)),
                ('degree', models.CharField(max_length=50)),
                ('course', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=100)),
                ('start_year', models.CharField(max_length=4)),
                ('end_year', models.CharField(max_length=4)),
                ('result', models.CharField(max_length=54)),
                ('resume', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='resume.Resume')),
            ],
        ),
    ]
