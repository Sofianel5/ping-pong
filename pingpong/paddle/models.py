from django.db import models

# Create your models here.
class Grade(models.Model):
    class Grades(models.TextChoices):
        FRESHMAN = 'FR', 'Freshman'
        SOPHOMORE = 'SO', 'Sophomore'
        JUNIOR = 'JR', 'Junior'
        SENIOR = 'SR', 'Senior'
        GRADUATE = 'GR', 'Graduate'
    name = models.CharField(choices=Grades.choices, default=Grades.FRESHMAN)
    def greater(self, grade2, grades=Grades.choices):
        grades = [grade for grade in grades]
        return grades.index(self.name) < grades.index(self.name)

class PointsCounter(models.Model):
    points = models.IntegerField()

class Rotation(models.Model):
    """A, A1, A2, B, B1, B2"""
    name = models.CharField(max_length=5)

class Period(models.Model):
    number = models.IntegerField()
    rotation = models.ForeignKey("paddle.models.Rotation", on_delete=models.DO_NOTHING)

class Schedule(models.Model):
    classes = models.ManyToManyField("paddle.models.Section")

class Teacher(models.Model):
    name = models.CharField(max_length=50)

class Section(models.Model):
    seats = models.IntegerField()
    course = models.ForeignKey("paddle.models.Course", on_delete=models.DO_NOTHING)
    period = models.ManyToManyField("paddle.models.Period", on_delete=models.DO_NOTHING)

class Student(models.Model):
    schedule = models.ForeignKey("paddle.models.Schedule", on_delete=models.DO_NOTHING)
    grade = models.ForeignKey("paddle.models.Grade", on_delete=models.DO_NOTHING)
    graduationrequirements = models.ForeignKey("paddle.models.GraduationRequirements", on_delete=models.DO_NOTHING)
    reportCard = models.ForeignKey("paddle.models.ReportCard", on_delete=models.DO_NOTHING)
    classWeights = models.ForeignKey("paddle.models.WeightedClassList", on_delete=models.DO_NOTHING)
    points = models.ForeignKey("paddle.models.PointsCounter", on_delete=models.DO_NOTHING)
    def hasPassed(self, course):
        pass
    def isTaking(self, course):
        pass

class Course(models.Model):
    course_id = models.CharField(max_length=50)
    # Related class Section has superclass Course and can relate to it
    prefs = models.ForeignKey("paddle.models.Prefrences", on_delete=models.DO_NOTHING)
    department = models.ForeignKey("paddle.models.Department", on_delete=models.DO_NOTHING)
    subject = models.ForeignKey("paddle.models.Subject", on_delete=models.DO_NOTHING)
    permissions = models.ForeignKey("paddle.models.PermissionsList", on_delete=models.DO_NOTHING)
    reqsFulfilled = models.ForeignKey("paddle.models.Requirements", on_delete=models.DO_NOTHING)
    syllabus = models.FileField()
    description = models.TextField()
    course_group = reqsFulfilled = models.ForeignKey("paddle.models.CourseGroup", on_delete=models.DO_NOTHING)
    def qualifies(self, student):
        pass

class CourseGroup(models.Model):
    name = models.CharField(max_length=50)

# create class Operator 

class Permission(models.Model):
    OPERATORS = (("OR", "or"), ("AND", "and"))
    conditions = models.ManyToManyField("paddle.models.Condition", on_delete=models.DO_NOTHING)
    operator = models.CharField(choices=OPERATORS, max_length=5)

class Condition(models.Model):
    name = models.CharField(max_length=20)
    def applyCondition(self, delegate):
        pass
class Defaults(models.Model):
    pass
