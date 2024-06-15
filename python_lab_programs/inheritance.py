# inheritance
class CS:
    def __init__(self, course, subject):
        self.coursename = course
        self.subjectname = subject 

    def printname(self):
        print(self.coursename, self.subjectname)
 
class Commerce(CS):
    def __init__(self, course, subject):
        super().__init__(course, subject) 
        # CS.__init__(self, course, subject)

x = Commerce("MCA", "Python")
x.printname()
