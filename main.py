import json
import os

def parseJson():
   with open (os.getcwd() + "\Resources\Fee.json") as jsonFile:
      data = json.load(jsonFile)
      return data

def main():
   while True:
      print("Enter a choice:\n1 Exam Fee \n2 Application Fee")
      # print(os.getcwd())
      fee = int(input())
      if(fee==1):
         print("Please choose your nationality:")
         data = parseJson()
         nationality = data['Exam Fee']
         for i in range(len(list(nationality))):
            print(i+1 , list(nationality)[i])
         # for nationality in data['Exam Fee']:
         #    print(nationality)
         nationality_chosen = int(input())
         if(nationality_chosen < 1 or nationality_chosen > len(list(nationality))):
            print("You chose an invalid option for nationality. \nPlease review the available options and try again")
            continue
         courses = data['Exam Fee'][list(nationality)[nationality_chosen-1]]
         # print(courses, type(courses))
         if(len(list(courses)) == 1 and list(courses)[0] == 'ALL_COURSES'):
            print('Choose a course from the below options:\n1 Medical \n2 Dental \n3 Ayurveda')   
            course_chosen = int(input())
            course_chosen = 1
         else:
            for i in range(len(list(courses))):
               print(i+1, list(courses)[i])
            course_chosen = int(input())
         if(course_chosen<1 or course_chosen>len(list(courses))):
            print('You chose an invalid option for the list of available courses. \n Please review the available options and try again')
            continue
         levels = data['Exam Fee'][list(nationality)[nationality_chosen-1]][list(courses)[course_chosen-1]]
         if(len(list(levels)) == 1 and list(levels)[0] == 'ALL_LEVEL'):
            print('Please choose from the list of levels below:\n1 UG \n2 PG \n3 DIPLOMA \n4 Ph.D')
            level_chosen = int(input())
            level_chosen = 1
         else:
            for i in range(len(list(levels))):
               print(i+1, list(levels)[i])
            level_chosen = int(input())
         if(level_chosen <1 or level_chosen>len(list(levels))):
            print('You chose an invalid option for the list of available course levels. \n Please review the available options and try again')
            continue
         print("Your cost of fee is : " , levels[list(levels)[level_chosen-1]]['amount'])
         break
      elif(fee==2):
         print("choice 2")
         break
      else:
         print("please enter a valid input")
         continue
   
main()
   
   