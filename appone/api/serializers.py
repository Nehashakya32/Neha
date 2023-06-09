from rest_framework import serializers
from appone.models import Teacher,Student


class Studentserializer(serializers.ModelSerializer):
    class Meta:
        model=Teacher
        fields='__all__'

class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model=Student
        fields='__all__'