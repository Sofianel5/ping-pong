from .models import Student, Section

def create_initial_setup():
    for section in Section.objects.all():
        students = getStudentsForCourse(section.course)

def getStudentsForCourse(course):
    students = []
    for student in Student.objects.all():
        if course.qualifies(student):
            students.append(student)
    return students

##student picked 5 choices and ranked them with how many point's they're willing to spend
##error function is going to spit out a number
class studentBot():
    def __init__(self, st):
        #s is the student
        self.s = st
        self.pointsTotal = st.points


    def errorFunction(self):
        pointsSpent = 0
        for i in self.s.schedule:
            pointsSpent += i.cost
            return pointsSpent

    def shouldTrade(self, fellowStudent, mySection, theirSection):
        ##first make sure that all the requirements are fulfulled on your end, since they will be doing the same
        tempSched = self.s.schedule
        for i in range(len(self.s.schedule)):
            if tempSched[i] == mySection:
                tempSched[i] = theirSection


        return True
        #ok the swap has been performed

        ##after that, then execute the trade
