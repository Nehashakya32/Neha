# Generated by Django 4.1.1 on 2023-06-09 10:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appone', '0003_signup'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='dob',
            field=models.DateField(auto_now_add=True, null=True),
        ),
    ]
