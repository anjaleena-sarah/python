list1=[1.0,2,3,4,5.5,('a','b','c')]
list2=["albin","alfia","anjaleena",[11,12,13,14,(1,2)]]
list3= list((2,4,6,8,10)) #double parenthesis is needed to run without errors
print("The type of list1", type(list1)) 
print("The type of list2", type(list2))
print("The type of list3", type(list3))  

#concatenation of dictionary
d={
    "student1":{
    "name":"sarah",
    "age":"22",
    "city":"banglore",
    "marks":{
        'maths':90,
        'science': 80
    }    
    },
"student2":{
    "name":"alfia",
    "age":"22",
    "city":"banglore",
    "marks":{
        'maths':95,
        'science': 99
    }    
    }
}
print(d.get('student1').get('marks'))
d['student1']
# d.popitem()
list1[0]='apple'
print(list1[0])
print(len(list1[0])) #to find the length - len

#Copy List
l1 = ["apple", "banana", "cherry"]
l1.append(8)
l2 = l1.copy()
l1.append(7)
print(l2)
print(l1)