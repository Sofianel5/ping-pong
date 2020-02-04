from django.db import models

# Create your models here.
class Grade(models.Model):
    GRADES = (
        ("FR", "Freshman"),
        ("SP", "Sophomore"),
        ("JR", "Junior"),
        ("SR", "Senior"),
    )
    name = models.charField(choices=GRADES)
    def greater(grade1, grade2):
        pass

class Student(models.Model):
    schedule = models.ForeignKey("pingpong.paddle.models.Schedule")
    grade = models.ForeignKey("pingpong.paddle.models.Grade")
    graduationrequirements = models.ForeignKey("pingpong.paddle.models.GraduationRequirements")
    reportCard = models.ForeignKey("pingpong.paddle.models.ReportCard")
    points = models.ForeignKey("pingpong.paddle.models.PointsCounter")
    def hasPassed(self, course):
        pass
    def isTaking(self, course):
        return course in self.schedule

class Course(models.Model):
    course_id = models.CharField(max_length=50)
    # Related class Period has superclass Course and can relate to it
    prefs = models.ForeignKey("pingpong.paddle.models.Prefrences")
    department = models.ForeignKey("pingpong.paddle.models.Department")
    subject = models.ForeignKey("pingpong.paddle.models.Subject")
    permissions = models.ForeignKey("pingpong.paddle.models.PermissionsList")
    reqsFulfilled = models.ForeignKey("pingpong.paddle.models.Requirements")
    syllabus = models.FileField()
    description = models.TextField()
    course_group = reqsFulfilled = models.ForeignKey("pingpong.paddle.models.CourseGroup")
    def qualifies(self, student):
        pass

class CourseGroup(models.Model):
    name = models.CharField(max_length=50)

class Section(models.Model):
    scheduleList = models.ForeignKey("pingpong.paddle.models.Schedule")
    seats = models.IntegerField()
    periods = models.ManyToManyField("pingpong.paddle.models.Periods")
    section = models.CharField(max_length=20)
    teacher = models.ForeignKey("pingpong.paddle.models.Teacher")

class Permission(models.Model):
    OPERATORS = (("OR", "or"), ("AND", "and"))
    conditions = models.ManyToManyField("pingpong.paddle.models.Condition")
    operator = models.CharField(choices=OPERATORS, max_length=5)

class Condition(model.Model):
    name = models.CharField(max_length=20)
    def applyCondition(self, delegate):
        pass
class Defaults(models.Model):
    pass
