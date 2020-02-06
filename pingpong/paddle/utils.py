import models.py



##student picked 5 choices and ranked them with how many point's they're willing to spend
##error function is going to spit out a number
class studentBot():
    def __init__(self, st):
        #s is the student
        self.s = st
        self.pointsTotal = s.points


    def errorFunction(self):
        pointsSpent = 0
        for i in s.schedule:
            pointsSpent += i.cost
            return pointsSpent

    def shouldTrade(self, fellowStudent, mySection, theirSection):
        ##first make sure that all the requirements are fulfulled on your end, since they will be doing the same
        tempSched = s.schedule
        for i in range(len(s.schedule)):
            if tempSched[i] == mySection:
                tempSched[i] = theirSection


        return True
        #ok the swap has been performed

        ##after that, then execute the trade
