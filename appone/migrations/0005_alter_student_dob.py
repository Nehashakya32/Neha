# Generated by Django 4.1.1 on 2023-06-09 10:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appone', '0004_alter_student_dob'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='dob',
            field=models.DateField(null=True),
        ),
    ]
