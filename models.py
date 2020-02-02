class Schedule():
    def __init__(self):
        self.classList = {"1_a1": None, "2_a1": None}

class Student():
    def __init__(self, grade):
        self.schedule = Schedule()
        self.grade = grade
        self.gradRequirements
        self.reportCard
    def hasPassed(self, course):
        pass
    def isTaking(self, course):
        return course in self.schedule


class Course():
    def __init__(self, seats, prefs=None):
        self.course_id
        self._periods = []
        self.prefs = prefs
        self.department
        self.subject
        self.permissions = []
        self.gradReqs = []
        self.syllabus
        self.description
        self.courseGroup
    def qualifies(self):
        pass

class CourseGroup():
    def __init__(self):
        self.courses = []

class Class():
    def __init__(self):
        self.studentList = []
        self.seats
        self.period
        self.cycle
        self.section
        self.teacher

class Permission():
    def __init__(self):
        self.operator
        self.conditions

class Condition():
    def __init__(self):
        pass
    def applyCondition(self, student):
        pass

class HasPassedCondition(Condition):
    def __init__(self):
        self.course
    def applyCondition(self, student):
        return student.hasPassed(self.course)

class TakingCondition(Condition):
    def __init__(self):
        self.course
    def applyCondition(self, student):
        return student.isTaking(course)

class QualifyForCondition(Condition):
    def __init__(self):
        self.course
    def applyCondition(self, student):
        return self.course.qualifies(student)

class GradeCondition(Condition):
    def __init__(self):
        self.course
        self.grade
        self.coursePreReq
    def applyCondition(self, student):
        pass

class GraduationRequirements():
    def __init__(self):
        self.coursegroupList = []
    pass

class GraduationRequriementsPath():
    def __init__(self):
        self.grades_reqs_dict

class Defaults():
    def __init__(self):
        self.defaultGraduationRequirementPath
