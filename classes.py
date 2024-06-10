# class mcasem3:
#     classrep1 = "Revathi"
#     classrep2 = "Sivanand"
#     placementrep = "Gracen"
    
#     def duties():
#         print("Attendance")

# # Creating objects of the class mcasem3
# rep1 = mcasem3()
# rep2 = mcasem3()
# print("Class Rep 1 : ",rep1.classrep1)
# print("Class Rep 2 : ",rep2.classrep2)
# print("Placement Rep  : ",rep1.placementrep)
# rep1.duties()


# class sem3:
#     classrep="revathi"
#     placementrep="merin"
#     def duties(self):
#         print("Attendance")
    
#     rep1=sem3()
#     rep2=sem3()
#     print(rep1.classrep)
#     rep1.duties()
#     print(rep1.placementrep)
#     rep1.duties()
    
    
class sem3:
        def __init__(self,name) :
            self.name=name
        def duties(self):
            print("Attendence")
            
classrep=sem3("Revathi")
placementrep=sem3("Gracen")
classrep.duties()
print(placementrep.name)
    
    