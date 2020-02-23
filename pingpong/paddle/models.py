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
    schedule = models.ForeignKey("paddle.Schedule", on_delete=models.DO_NOTHING, blank=True, null=True)
    grade = models.ForeignKey("paddle.Grade", on_delete=models.DO_NOTHING)
    graduationrequirements = models.ForeignKey("paddle.GraduationRequirements", on_delete=models.DO_NOTHING, blank=True, null=True)
    reportCard = models.ForeignKey("paddle.ReportCard", on_delete=models.DO_NOTHING, blank=True, null=True)
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
    permissions = models.ManyToManyField("paddle.Permission", blank=True)
    syllabus = models.FileField(blank=True, null=True)
    description = models.TextField(default="There is no description for this course.")
    course_group = models.ForeignKey("paddle.CourseGroup", on_delete=models.DO_NOTHING)
    def qualifies(self, student):
        # Apply permissions
        for permission in self.permissions:
            if not permission.apply(student):
                return False 
        return True
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
        return self.course.name

class WeightedCourseList(models.Model):
    courses = models.ManyToManyField("paddle.WeightedCourse")

class GradedCourse(models.Model):
    course = models.ForeignKey("paddle.Course", on_delete=models.DO_NOTHING)
    grade = models.FloatField()
    def __str__(self):
        return self.course.name

class CourseGroup(models.Model):
    name = models.CharField(max_length=50)
    level = models.IntegerField()
    def __str__(self):
        return self.name + " " +str(self.level)

class GraduationRequirements(models.Model):
    pass


class Permission(models.Model):
    """
    Right now this doesnt allow for recursive permissions, 
    update in future by creating a subclass of permission as BasePermission
     to replace condition and change manyToMany("paddle.Permission") so it can refer to full sub permissions or simple conditions
    """
    OPERATORS = (("OR", "or"), ("AND", "and"))
    conditions = models.ManyToManyField("paddle.Condition")
    operator = models.CharField(choices=OPERATORS, max_length=5)
    def apply(self, student):
        if self.operator == "OR":
            for condition in self.conditions:
                if condition.applyCondition(student):
                    return True 
            return False
        else:
            for condition in self.conditions:
                if not condition.applyCondition(student):
                    return False 
            return True
    def __str__(self):
        return (" "+self.operator+" ").join([conditon for conditon in self.conditions])

class Condition(models.Model):
    name = models.CharField(max_length=20)
    condition_func = models.CharField(max_length=20, default="no_condition")
    def applyCondition(self, student):
        return exec(self.name+"(student)")
    def __str__(self):
        return self.name
    
class Defaults(models.Model):
    pass
