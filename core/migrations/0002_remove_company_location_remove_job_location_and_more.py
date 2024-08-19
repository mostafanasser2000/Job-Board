# Generated by Django 5.0.7 on 2024-08-19 20:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='company',
            name='location',
        ),
        migrations.RemoveField(
            model_name='job',
            name='location',
        ),
        migrations.AddIndex(
            model_name='job',
            index=models.Index(fields=['title', 'company'], name='core_job_title_c40e5c_idx'),
        ),
        migrations.DeleteModel(
            name='Location',
        ),
    ]