# Generated by Django 3.0.2 on 2020-01-15 12:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('academic', '0004_classregistration'),
        ('result', '0005_auto_20190807_0908'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subjectregistration',
            name='select_class',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='academic.ClassRegistration'),
        ),
    ]