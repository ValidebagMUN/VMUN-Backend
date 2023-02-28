# Generated by Django 4.0.10 on 2023-02-28 01:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('conferences', '0002_alter_committee_slug_alter_conference_slug_and_more'),
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='committee',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='conferences.committee'),
        ),
        migrations.AddField(
            model_name='user',
            name='institution',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='conferences.institution'),
        ),
        migrations.AddField(
            model_name='user',
            name='phone',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='type',
            field=models.CharField(choices=[('DEL', 'Delegate'), ('CHA', 'Chair'), ('ADV', 'Advisor'), ('ADM', 'Admin')], default='DEL', max_length=3),
        ),
    ]