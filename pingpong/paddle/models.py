from django.db import models

# Create your models here.
class Grade(models.Model):
    Grades = (
        ('FR', 'Freshman'),
        ('SO', 'Sophomore'),
        ('JR', 'Junior'),
        ('SR', 'Senior')
    )
    name = models.CharField(choices=Grades, default=Grades[0], max_length=2)
    
    def greater(self, grade2, grades=Grades):
        grades = [grade for grade in grades]
        return grades.index(self.name) < grades.index(self.name)

class PointsCounter(models.Model):
    points = models.IntegerField()

class Rotation(models.Model):
    """A, A1, A2, B, B1, B2"""
    name = models.CharField(max_length=5)

class Period(models.Model):
    number = models.IntegerField()
    rotation = models.ForeignKey("paddle.Rotation", on_delete=models.DO_NOTHING)

class Schedule(models.Model):
    classes = models.ManyToManyField("paddle.Section")

class Teacher(models.Model):
    name = models.CharField(max_length=50)

class Department(models.Model):
    name = models.CharField(max_length=50)

class Section(models.Model):
    seats = models.IntegerField()
    course = models.ForeignKey("paddle.Course", on_delete=models.DO_NOTHING)
    period = models.ManyToManyField("paddle.Period")

class Student(models.Model):
    schedule = models.ForeignKey("paddle.Schedule", on_delete=models.DO_NOTHING)
    grade = models.ForeignKey("paddle.Grade", on_delete=models.DO_NOTHING)
    graduationrequirements = models.ForeignKey("paddle.GraduationRequirements", on_delete=models.DO_NOTHING)
    reportCard = models.ForeignKey("paddle.ReportCard", on_delete=models.DO_NOTHING)
    classWeights = models.ForeignKey("paddle.WeightedCourseList", on_delete=models.DO_NOTHING)
    points = models.ForeignKey("paddle.PointsCounter", on_delete=models.DO_NOTHING)
    def hasPassed(self, course):
        pass
    def isTaking(self, course):
        pass

class ReportCard(models.Model):
    grades = models.ManyToManyField("paddle.GradedCourse")

class Subject(models.Model):
    name = models.CharField(max_length=15)

class Course(models.Model):
    course_id = models.CharField(max_length=50)
    # Related class Section has superclass Course and can relate to it
    prefs = models.ForeignKey("paddle.Prefrences", on_delete=models.DO_NOTHING)
    department = models.ForeignKey("paddle.Department", on_delete=models.DO_NOTHING)
    subject = models.ForeignKey("paddle.Subject", on_delete=models.DO_NOTHING)
    permissions = models.ForeignKey("paddle.PermissionsList", on_delete=models.DO_NOTHING)
    syllabus = models.FileField()
    description = models.TextField()
    course_group = models.ForeignKey("paddle.CourseGroup", on_delete=models.DO_NOTHING)
    def qualifies(self, student):
        pass

class Prefrences(models.Model):
    def scoreStudent(self, student):
        pass

class WeightedCourse(models.Model):
    course = models.ForeignKey("paddle.Course", on_delete=models.DO_NOTHING)
    weight = models.IntegerField()

class WeightedCourseList(models.Model):
    courses = models.ManyToManyField("paddle.WeightedCourse")

class GradedCourse(models.Model):
    course = models.ForeignKey("paddle.Course", on_delete=models.DO_NOTHING)
    grade = models.FloatField()

class CourseGroup(models.Model):
    name = models.CharField(max_length=50)
    fulfilling_courses = models.ForeignKey("paddle.Course", on_delete=models.DO_NOTHING)

class GraduationRequirements(models.Model):
    pass

# create class Operator 
class Permission(models.Model):
    OPERATORS = (("OR", "or"), ("AND", "and"))
    conditions = models.ManyToManyField("paddle.Condition")
    operator = models.CharField(choices=OPERATORS, max_length=5)

class PermissionsList(models.Model):
    pass

class Condition(models.Model):
    name = models.CharField(max_length=20)
    def applyCondition(self, delegate):
        pass
class Defaults(models.Model):
    pass
