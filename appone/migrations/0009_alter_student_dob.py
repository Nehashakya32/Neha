# Generated by Django 4.1.1 on 2023-06-09 11:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appone', '0008_alter_student_dob'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='dob',
            field=models.DateField(auto_created=True, null=True),
        ),
    ]
