# Generated by Django 5.0.7 on 2024-09-27 20:11

import django.core.validators
import django.db.models.deletion
import profiles.models
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('core', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='CompanyProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=255)),
                ('about', models.TextField(blank=True, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to=profiles.models.upload_profile_image)),
                ('contact_email', models.EmailField(blank=True, max_length=254, null=True)),
                ('facebook_url', models.URLField(blank=True, null=True, validators=[django.core.validators.URLValidator])),
                ('twitter_url', models.URLField(blank=True, null=True, validators=[django.core.validators.URLValidator])),
                ('linkedin_url', models.URLField(blank=True, null=True, validators=[django.core.validators.URLValidator])),
                ('website', models.URLField(blank=True, null=True, validators=[django.core.validators.URLValidator])),
                ('slug', models.SlugField(blank=True, unique=True)),
                ('founded_at', models.DateField(blank=True, null=True)),
                ('country', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.country')),
                ('industries', models.ManyToManyField(blank=True, null=True, to='core.industry')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='%(class)s_profile', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Education',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('degree', models.CharField(choices=[('Associate', 'Associate'), ('Bachelor', 'Bachelor'), ('Master', 'Master'), ('MBA', 'MBA'), ('PhD', 'PhD'), ('Certificate', 'Certificate'), ('Diploma', 'Diploma'), ('Other', 'Other')], max_length=100)),
                ('institution_name', models.CharField(max_length=255)),
                ('field_of_study', models.CharField(max_length=255)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='educations', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-end_date'],
            },
        ),
        migrations.CreateModel(
            name='Experience',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('job_title', models.CharField(max_length=255)),
                ('company_name', models.CharField(max_length=255)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField(blank=True, null=True)),
                ('is_current', models.BooleanField(default=False)),
                ('job_category', models.ManyToManyField(blank=True, null=True, to='core.industry')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='experiences', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-start_date'],
            },
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=255)),
                ('about', models.TextField(blank=True, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to=profiles.models.upload_profile_image)),
                ('contact_email', models.EmailField(blank=True, max_length=254, null=True)),
                ('facebook_url', models.URLField(blank=True, null=True, validators=[django.core.validators.URLValidator])),
                ('twitter_url', models.URLField(blank=True, null=True, validators=[django.core.validators.URLValidator])),
                ('linkedin_url', models.URLField(blank=True, null=True, validators=[django.core.validators.URLValidator])),
                ('website', models.URLField(blank=True, null=True, validators=[django.core.validators.URLValidator])),
                ('date_of_birth', models.DateField(blank=True, null=True)),
                ('gender', models.CharField(blank=True, choices=[('Male', 'Male'), ('Female', 'Female')], max_length=20, null=True)),
                ('military_status', models.CharField(blank=True, choices=[('Not Applicable', 'Not Applicable'), ('Exempted', 'Exempted'), ('Completed', 'Completed'), ('Postponed', 'Postponed')], max_length=20, null=True)),
                ('country', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.country')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='%(class)s_profile', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='UserSkill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('skill', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.skill')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='skills', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'unique_together': {('user', 'skill')},
            },
        ),
    ]