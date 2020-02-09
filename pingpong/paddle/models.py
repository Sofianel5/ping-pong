from django.db import models 
from . import functions 

# Create your models here.
class Grade(models.Model):
    Grades = (
        ('FR', 'Freshman'),
        ('SO', 'Sophomore'),
        ('JR', 'Junior'),
        ('SR', 'Senior'),
    )
    name = models.CharField(choices=Grades, default=Grades[0], max_length=2)
    
    def greater(self, grade2, grades=Grades):
        grades = [grade for grade in grades]
        return grades.index(self.name) < grades.index(self.name)
    def __str__(self):
        return self.name

class PointsCounter(models.Model):
    points = models.IntegerField(default=0)

class Rotation(models.Model):
    """A, A1, A2, B, B1, B2"""
    name = models.CharField(max_length=5)
    def __str__(self):
        return self.name
    

class Period(models.Model):
    number = models.IntegerField()
    rotation = models.ForeignKey("paddle.Rotation", on_delete=models.DO_NOTHING)
    def __str__(self):
        return "Period "+str(self.number) + ", "+str(self.rotation)

class Semester(models.Model):
    SEMESTER_CHOICES = (
        (1, "first"),
        (2, "second"),
    )
    grade = models.ForeignKey("paddle.Grade", on_delete=models.DO_NOTHING)
    number = models.IntegerField(choices=SEMESTER_CHOICES)

class Schedule(models.Model):
    semester = models.ForeignKey("paddle.Semester", on_delete=models.DO_NOTHING, blank=True, null=True)
    classes = models.ManyToManyField("paddle.Section")

class Teacher(models.Model):
    name = models.CharField(max_length=50)

class Department(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self):
        return self.name
    
class Section(models.Model):
    seats = models.IntegerField()
    course = models.ForeignKey("paddle.Course", on_delete=models.DO_NOTHING)
    period = models.ManyToManyField("paddle.Period")
    def __str__(self):
        return self.course

class Student(models.Model):
    schedule = models.ForeignKey("paddle.Schedule", on_delete=models.DO_NOTHING)
    grade = models.ForeignKey("paddle.Grade", on_delete=models.DO_NOTHING)
    graduationrequirements = models.ForeignKey("paddle.GraduationRequirements", on_delete=models.DO_NOTHING)
    reportCard = models.ForeignKey("paddle.ReportCard", on_delete=models.DO_NOTHING)
    classWeights = models.ForeignKey("paddle.WeightedCourseList", on_delete=models.DO_NOTHING)
    points = models.ForeignKey("paddle.PointsCounter", on_delete=models.DO_NOTHING)
    courses_taken = models.ForeignKey("paddle.CourseCompletionList", on_delete=models.DO_NOTHING, blank=True, null=True)
    name = models.CharField(max_length=50, default="Unnamed")
    osis = models.IntegerField(blank=True, null=True)
    def hasPassed(self, course):
        pass
    def isTaking(self, course):
        pass
    def __str__(self):
        return self.name
    
class CourseCompletionList(models.Model):
    schedules = models.ManyToManyField("paddle.Schedule")

class ReportCard(models.Model):
    grades = models.ManyToManyField("paddle.GradedCourse")

class Subject(models.Model):
    name = models.CharField(max_length=15)
    def __str__(self):
        return self.name
    

class Course(models.Model):
    course_id = models.CharField(max_length=10)
    name = models.CharField(max_length=50)
    # Related class Section has superclass Course and can relate to it
    prefs = models.ForeignKey("paddle.Prefrences", on_delete=models.DO_NOTHING)
    department = models.ForeignKey("paddle.Department", on_delete=models.DO_NOTHING)
    subject = models.ForeignKey("paddle.Subject", on_delete=models.DO_NOTHING)
    permissions = models.ManyToManyField("paddle.Permission")
    syllabus = models.FileField(blank=True, null=True)
    description = models.TextField(default="There is no description for this course.")
    course_group = models.ForeignKey("paddle.CourseGroup", on_delete=models.DO_NOTHING)
    def qualifies(self, student):
        # Apply permissions
        pass
    def __str__(self):
        return self.name
    

class Prefrences(models.Model):
    # will return a number [0,1] where 1 is preferred and 0 is not allowed
    pref_func = models.CharField(max_length=15)
    def scoreStudent(self, student):
        return eval("functions."+self.pref_func+"(student)")
    def __str__(self):
        return self.pref_func
    

class WeightedCourse(models.Model):
    course = models.ForeignKey("paddle.Course", on_delete=models.DO_NOTHING)
    weight = models.IntegerField()
    def __str__(self):
        return self.course

class WeightedCourseList(models.Model):
    courses = models.ManyToManyField("paddle.WeightedCourse")

class GradedCourse(models.Model):
    course = models.ForeignKey("paddle.Course", on_delete=models.DO_NOTHING)
    grade = models.FloatField()
    def __str__(self):
        return self.course

class CourseGroup(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self):
        return self.name

class GraduationRequirements(models.Model):
    pass

# create class Operator 
class Permission(models.Model):
    OPERATORS = (("OR", "or"), ("AND", "and"))
    conditions = models.ManyToManyField("paddle.Condition")
    operator = models.CharField(choices=OPERATORS, max_length=5)
    def __str__(self):
        return (" "+self.operator+" ").join([conditon for conditon in self.conditions])

class Condition(models.Model):
    name = models.CharField(max_length=20)
    condition_func = models.CharField(max_length=20, default="no_condition")
    def applyCondition(self, delegate):
        pass
    def __str__(self):
        return self.name
    
class Defaults(models.Model):
    pass
