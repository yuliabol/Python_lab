from django.db import models


class Group(models.Model):
    name = models.CharField(max_length=10)
    year = models.IntegerField()

    def __str__(self):
        return f"{self.name} - {self.year}"


class GroupSubjectTeacher(models.Model):
    group = models.OneToOneField(Group, models.DO_NOTHING)
    subject = models.ForeignKey('Subject', models.DO_NOTHING)
    teacher = models.ForeignKey('Teacher', models.DO_NOTHING)
    type_lesson = models.CharField(max_length=15)
    day = models.CharField(max_length=15)
    time = models.TimeField()
    location = models.CharField(max_length=60)
    id = models.IntegerField(primary_key=True)

    class Meta:
        unique_together = (('group', 'subject', 'teacher', 'type_lesson'),)


class Student(models.Model):
    first_name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40)
    group = models.ForeignKey(Group, models.DO_NOTHING)


class Subject(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(blank=True, null=True)


class Teacher(models.Model):
    first_name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40)
    group_subjects = models.ManyToManyField(GroupSubjectTeacher, related_name='teachers')
