#To define a string we can use "" or ''
str1='hello'
str2=" world"

#string as arrays
print(str1[1])

#if we want two characters to be printed
print(str1[0:2])

#from character 3 to end
print(str1[3:])

#printing character from back
print(str1[-1])

#reverse the string
print(str1[::-1])


#concatenate two strings
print(str1 + str2)
print('welcome ' + 'to ' + 'python ' + 'programming')

#we can concatenate two strings without using +
print('welcome ' 'to ' 'python '  'programming') 

#variable concatenation + must
print('hello' + str2)

#we cannot concatenate a string and a number (to do that change the number to string)
s1="Python "
s2=25
# print(s1 + s2) #error
print(s1 + str(s2)) #converting int to string


#multi line string
str3="""Python is a high-level, 
        general-purpose programming language. 
        Its design philosophy emphasizes code readability with the use of significant indentation. 
        Python is dynamically typed and garbage-collected. """
print(str3)


#print length of a string - use len
print("Length = ",len(str3))


#string handling function

#strip function - to remove white spaces
str4 = "          apple            "
print("Fruit :",str4.strip())

#to lowercase
str5="GraPEs"
print("Fruit :",str5.lower())

#to uppercase
print("Fruit :",str5.upper())

#to replace a character
print(str5.replace("a","x"))

#splitting a string and converting to a list (array is called list)
str6 = "apple,banana,pear"
print(str6.split(","))

#to check whether a text is present in the string
x = "banana" in str6
y = "orange" in str6
print(x) #returns a boolean value
print(y)


#strings can be used for formatting
name ="sarah"
txt = "my name is {} and my age is {}" #value will be assigned to {}
txt1 = "my name is {0} and my age is {1}" 
txt2 = "my name is {1} and my age is {0}" 
age = 21
print(txt.format(name,age))
print(txt1.format(name,age))
print(txt2.format(name,age))

msg = "askr\""
print(msg)