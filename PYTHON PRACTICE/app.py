############################################## DAY:03 /6/2025 ###################################################

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
#                                         X----------------X----------------X

#---------------------------------------------SYNTAX "for" LOOP--------------------------------------------------
# for variable_count in range(startnumber,endnumber,step)

# #PRACTICE # 01: [SIMPLE "for" LOOP CODE]
# for i in range(1,10,2):
#     print(i)
#     name1 = input("ENTER YOUR NAME:")
#                                         X----------------X----------------X

# #PRACTICE # 02: [TAKING INPUT FROM USER TO PRINT A TABLE]
# tablenumber = int(input("ENTER THE NUMBER FOR THE TABLE:"))
# for i in range(1,11,1):
#     print( tablenumber,"x",i, "=",tablenumber*i)
#                                         X----------------X----------------X

# #PRACTICE # 03: [TAKING START AND STOP NUMBER FROM USER]
# startnumber = int(input("ENTER THE NUMBER WHERE YOU WANT TO START:"))
# endnumber = int(input("ENTER THE NUMBER WHERE YOU WANT TO STOP:"))
# for i in range(startnumber,endnumber,1):
#     print(i)
#                                         X----------------X----------------X

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
#                                         X----------------X----------------X

# #PRACTICE # 05: [END-LINE]
# name =input("ENTER YOR NAME:")
# for i in name:
#     print(i, end = "_")
#                                         X----------------X----------------X

# #PRACTICE # 06: [REVERSED METHOD]
# name = input("enter your name:")
# reversed = ""
# for i in name :
#     reversed = i + reversed
# print(reversed)
#                                         X----------------X----------------X

# #PRACTICE # 07: [PYRAMID]
# n = int(input("ENTER THE NUMBER OF ROWS:"))
# for i in range(1,n+1): # iske syntax mein no.ofsteps mentioned nhi kye cz ye bydefalt 1 hota hai
#  print("*" * i) 
#                                         X----------------X----------------X

# #PRACTICE # 08: [PYRAMID IN REVERSE ORDER]
# n = int(input("ENTER THE NUMBER OF ROWS:"))
# for i in range(n,0,-1):
#  print("*" * i) 
#                                         X----------------X----------------X

# #PRACTICE # 09: [A RIGHT HAND HALR PYRAMID, BOTH STRAIGHT AND REVERSED FORM]
# n = int(input('enter the number of rows'))
# for i in range(1,n+1,1):
#  print(' ' * (n-i) + '*' * i)

############################################## DAY:05 8/6/2025 ###################################################

#----------------------------------------------TASK 2----------------------------------------------------------
# CREATE A RIGHT HAND HALR PYRAMID, BOTH STRAIGHT AND REVERSED FORM

# # PRACTICE # 01 [STRAIGHT FORM]
# rows = int(input("ENTER THE NUMBER OF ROWS:"))

# print("Straight Form:")
# # CONDITION : The loop runs from 1 to rows (inclusive)
# for i in range(1, rows + 1):
#     print(" " * (rows - i) + "#" * i)
# # " " * (rows - i): prints the spaces to shift the # to the right
# # "#" * i: prints the hash symbols. The number of hashes equals the row number.
#                                         X----------------X----------------X
# # PRACTICE # 02 [REVERSE FORM]
# rows = int(input("ENTER THE NUMBER OF ROWS:"))
# print("\nReverse Form:")
# # CONDITION : This loop counts down from rows to 1
# for i in range(rows, 0, -1):
#     print(" " * (rows - i) + "#" * i)
#                                         X----------------X----------------X
# # PRACTICE # 03 [REVERSE FORM BY 2nd METHOD]
# rows = int(input("ENTER THE NUMBER OF ROWS:"))
# print('\n\t')
# for i in reversed(range(1,rows+1,1)):
#     print(" " * (rows - i) + "#" * i)
#                                         X----------------X----------------X
# # PRACTICE # 04 [DOUBLE SIDE PYRAMID]
# rows = int(input("ENTER THE NUMBER OF ROWS:"))
# for i in range(0,rows+1,1):
#     print(" " * (rows - i) + "#" * (2 * i + 1))
#                                         X----------------X----------------X

# # PRACTICE # 05 [DIAMOND PYRAMID]
# rows = int(input("ENTER THE NUMBER OF ROWS:"))
# for i in range(1,rows+1,1):
#     print(" " * (rows - i) + "#" * i)
# for i in reversed(range(1,rows+1,1)):
#     print(" " * (rows - i) + "#" * i)
#                                         X----------------X----------------X

# # PRACTICE # 06 [DOUBE DIAMOND PYRAMID]
# rows = int(input("ENTER THE NUMBER OF ROWS:"))
# for i in range(0,rows+1,1):
#     print(" " * (rows - i) + "#" * (2 * i +1))
# for i in reversed(range(0,rows+1,1)):
#     print(" " * (rows - i) + "#" * (2 * i +1))
#                                         X----------------X----------------X

# # PRACTICE # 07 [1/3 DIAMOND PYRAMID]
# rows = int(input("ENTER THE NUMBER OF ROWS:"))
# for i in range(0,rows+1,1):
#     print(" " * (rows - i) + "#" * (2 * i +1))
# for i in reversed(range(0,rows+1,1)):
#     print(" " * (rows - i) + "#" * i)
#                                         X----------------X----------------X

#------------------------------------------ LOGICAL "AND" and "OR" OPERATOR -----------------------------------------
# # PRACTICE # 08 [LOGICAL "AND" OPERATOR]
# age = int(input("ENTER YOUR AGE:"))
# height = float(input("ENTER YOUR HEIGHT:"))
# if age >= 18 and height >= 4.4:
#     print("CONGRACTS, YOU ARE ELIGIBLE!😍")
# else :
#     print("SORRY, YOU'RE NOT ELIGIBLE!😒")
#                                         X------X-------X

# # PRACTICE # 09 [LOGICAL "OR" OPERATOR]
# age = int(input("ENTER YOUR AGE:"))
# height = float(input("ENTER YOUR HEIGHT:"))
# if age >= 18 or height >= 4.4:
#     print("CONGRACTS, YOU ARE ELIGIBLE!😍")
# else :
#     print("SORRY, YOU'RE NOT ELIGIBLE!😒")
#                                         X-------X------X

#                                X----------------X----------------X

# # # PRACTICE # 10 [DATA STRUCTURE {LIST | []}
# #           0         1        2       3       5
# names = ["mehwish","kanazh","kavita","rida","farah"]
# #printing the list
# print(names)
# # accessing element through index/posiyion
# print(names[3])
# # skicing [start:end]
# print(names[0:4])
# # if you don't mentiont starting index it will take zero by default
# print(names[:4])
# # if you don't mentiont ending index it will take zero by default
# print(names[1:])
# # if you don't mentiont starting and ending index it will print the complete list
# print(names[:])
# #           start : end : step
# print(names[  0   :  4  :  2  ])

# # # PRACTICE # 10 [ELEMENT IN THE LIST]
# #            APPEND
# names = ["mehwish","kanazh","kavita","rida","farah"]
# # add an element in the list
# names.append("ayesha")
# print(names)
# #                                         X----------------X----------------X
