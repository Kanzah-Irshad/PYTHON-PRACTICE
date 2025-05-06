

#-------------------------------------FOR SHOWING GRADES ----------------------------------------------
# marks = int(input("ENTER YOUR MARKS:"))

# if marks>90:
#     print ("GRADE A😍")
# elif marks>80:
#     print("GRADE B😉")   
# elif marks>70:
#     print("GRADE C😘")
# elif marks>60:
#     print("GRADE D😊")
# else:
#     print("FAILED🤦‍♀️")

#--------------------------------------------- GRADES DECLEAR ------------------------------------------
# #  I have taken 5 marks in the input here
# marks1 = int(input("Enter your Subject1 marks:")) 
# marks2 = int(input("Enter your Subject2 marks:"))
# marks3 = int(input("Enter your Subject3 marks:"))
# marks4 = int(input("Enter your Subject4 marks:"))
# marks5 = int(input("Enter your Subject5 marks:"))

# # for obtainedmarks, we will collect marks by asking user
# obtainedMarks = marks1 + marks2 + marks3 + marks4 + marks5
# # calculate percentage
# percentage = (obtainedMarks/500)*100
# # condition
# if(percentage >=90):
#     print("PERFECT, YOU'RE GRADE IS AA😍", obtainedMarks)
# elif(percentage >=80):
#     print("EXELLENT, YOU'RE GRADE IS B😉", obtainedMarks)
# elif(percentage >=70):
#     print("GOOD, YOU'RE GRADE IS C😘", obtainedMarks)
# elif(percentage >=60):
#     print("OKAY, YOU'RE GRADE IS D😊", obtainedMarks)
# else:
#     print("SORRY!, YOU'RE FAILED🤦‍♀️", obtainedMarks)    

############################################## DAY:04 5/6/2025 ###################################################
# CLASS TASK [DECLEAR EVEN OR ODD NUMBER]
# #user se input mein num lenge (int = integer)
# user = int(input("ENTER YOUR NUMBER:"))
# # condition lagayenge 
# #if the number is divisible by 2 then the num is even otherise the num is odd
# if user % 2 == 0 :
#     print("your number is even.")
# else :
#     print("your number is odd.")    


#---------------------------------------------SYNTAX "for" LOOP--------------------------------------------------
# for variable_count in range(startnumber,endnumber,step)

# #PRACTICE # 01: [SIMPLE "for" LOOP CODE]
# for i in range(1,10,2):
#     print(i)
#     name1 = input("ENTER YOUR NAME:")

# #PRACTICE # 02: [TAKING INPUT FROM USER TO PRINT A TABLE]
# tablenumber = int(input("ENTER THE NUMBER FOR THE TABLE:"))
# for i in range(1,11,1):
#     print( tablenumber,"x",i, "=",tablenumber*i)

# #PRACTICE # 03: [TAKING START AND STOP NUMBER FROM USER]
# startnumber = int(input("ENTER THE NUMBER WHERE YOU WANT TO START:"))
# endnumber = int(input("ENTER THE NUMBER WHERE YOU WANT TO STOP:"))
# for i in range(startnumber,endnumber,1):
#     print(i)

# #PRACTICE # 04:  [TAKING STOPNUMBER FROM USER]
# stopnumber = int(input("ENTER THE TOTAL NUMBER OF STUDENT:"))
# for i in range(1,stopnumber+1,1):

#  marks1 = int(input("Enter your Subject1 marks:")) 
#  marks2 = int(input("Enter your Subject2 marks:"))
#  marks3 = int(input("Enter your Subject3 marks:"))
#  marks4 = int(input("Enter your Subject4 marks:"))
#  marks5 = int(input("Enter your Subject5 marks:"))

#  obtainedMarks = marks1 + marks2 + marks3 + marks4 + marks5
# # calculate percentage
#  percentage = (obtainedMarks/500)*100
#     # condition
#  if(percentage >=90):
#      print("PERFECT, YOU'RE GRADE IS AA😍", obtainedMarks)
#      print("EXELLENT, YOU'RE GRADE IS B😉", obtainedMarks)
#  elif(percentage >=70):
#      print("GOOD, YOU'RE GRADE IS C😘", obtainedMarks)
#  elif(percentage >=60):
#      print("OKAY, YOU'RE GRADE IS D😊", obtainedMarks)
#  else:
#         print("SORRY!, YOU'RE FAILED🤦‍♀️", obtainedMarks) 

# #PRACTICE # 05: [END-LINE]
# name =input("ENTER YOR NAME:")
# for i in name:
#     print(i, end = "_")

# #PRACTICE # 06: [REVERSED METHOD]
# name = input("enter your name:")
# reversed = ""
# for i in name :
#     reversed = i + reversed
# print(reversed)

# #PRACTICE # 07: [PYRAMID]
# n = int(input("ENTER THE NUMBER OF ROWS:"))
# for i in range(1,n+1): # iske syntax mein no.ofsteps mentioned nhi kye cz ye bydefalt 1 hota hai
#  print("*" * i) 

# #PRACTICE # 08: [PYRAMID IN REVERSE ORDER]
# n = int(input("ENTER THE NUMBER OF ROWS:"))
# for i in range(n,0,-1):
#  print("*" * i) 

# #PRACTICE # 09: [A RIGHT HAND HALR PYRAMID, BOTH STRAIGHT AND REVERSED FORM]
# n = int(input('enter the number of rows'))
# for i in range(1,n+1,1):
#  print(' ' * (n-i) + '*' * i)