import json
import os

# function that parses the json file and returns the json object
def parseJson(filename):
   with open (os.getcwd() + "\\Resources\\" + filename + ".json") as jsonFile:
      data = json.load(jsonFile)
      return data

#function that allows the user to pick a nationality of choice and returns it
def pick_nationality(nationality):
   print("Please choose your nationality:")
   # nationality = data['Exam Fee']
   # since dict is not indexed, converting it to list allows the use of indexes for serial#
   # display the list of available nationalities from the json
   for i in range(len(list(nationality))):
      print(i+1 , list(nationality)[i])
   nationality_chosen = int(input())
   #check for invalid input
   if(nationality_chosen < 1 or nationality_chosen > len(list(nationality))):
      return -1
   return nationality_chosen

#function that allows the user to pick a course of choice and returns it
def pick_course(courses):
   # since dict is not indexed, converting it to list allows the use of indexes for serial#
   if(len(list(courses)) == 1 and list(courses)[0] == 'ALL_COURSES'):
      print('Choose a course from the below options:\n1 Medical \n2 Dental \n3 Ayurveda')   
      course_chosen = int(input())
      # check for invalid input
      if(course_chosen < 1 or course_chosen > 3):
         return -1
      course_chosen = 1 #overwrites the user input when it is for all courses
   else:
      for i in range(len(list(courses))):
         print(i+1, list(courses)[i])
      course_chosen = int(input())
      # check for invalid input
      if(course_chosen <1 or course_chosen > len(list(courses))):
         return -1
   return course_chosen
   
#function that allows the user to pick a course level and returns it
def pick_level(levels):
   if(len(list(levels)) == 1 and list(levels)[0] == 'ALL_LEVEL'):
      print('Please choose from the list of levels below:\n1 UG \n2 PG \n3 DIPLOMA \n4 Ph.D')
      level_chosen = int(input())
      # check for invalid input
      if(level_chosen <1 or level_chosen > 4):
         return -1
   else:
      for i in range(len(list(levels))):
         print(i+1, list(levels)[i])
      level_chosen = int(input())
      # check for invalid input
      if(level_chosen < 1 or level_chosen>len(list(levels))):
         return -1
   return level_chosen
   

def main():
   while True:
      data = parseJson("fee")
      print("Please choose from the following options:")
      for i in range(len(list(data))):
         print(i+1 , list(data)[i])
      fee_chosen = int(input())
      if(fee_chosen<1 or fee_chosen>len(list(data))):
         print('INVALID OPTION!! \nPlease review the available options and try again ')
         continue
      nationality = data[list(data)[fee_chosen-1]]
      nationality_chosen = pick_nationality(nationality)
      if(nationality_chosen == -1):
         print("You chose an invalid option for nationality. \nPlease review the available options and try again")
         continue
      
      courses = nationality[list(nationality)[nationality_chosen-1]]
      # print(courses)
      # print(list(courses), len(list(courses)))
      course_chosen = pick_course(courses)
      
      if(course_chosen == -1):
         print('You chose an invalid option for the list of available courses. \nPlease review the available options and try again')
         continue
      levels = courses[list(courses)[course_chosen-1]]
      # print(levels)
      # print(list(levels), len(list(levels)))
      level_chosen = pick_level(levels)
         
      if(level_chosen == -1):
         print('You chose an invalid option for the list of available course levels. \nPlease review the available options and try again')
         continue
      if(list(levels)[0] == 'ALL_LEVEL'):
         amount  = levels[list(levels)[1-1]]['amount'];
      else:
         amount = levels[list(levels)[level_chosen-1]]['amount']
         
      if(list(levels)[0] == 'ALL_LEVEL'):
         gst = levels[list(levels)[1-1]]['gst'];
      else:
         gst = levels[list(levels)[level_chosen-1]]['gst'];
      # print(amount)
      # print(gst)
      amount += amount * (gst/100)
      
      data2 = parseJson("student")
      # for i in range(len(list(data2))):
      #    print(i+1 , list(data2)[i])
         
      # print (list(nationality)[nationality_chosen-1])
      
      chosen_nationality = list(nationality)[nationality_chosen-1]
      chosen_fee = list(data)[fee_chosen -1]
      levels_dict = {1: "UG" , 2: "PG" , 3:"DIPLOMA" , 4:"Ph.D"}
      chosen_level = levels_dict[level_chosen]
      
      # for i in data2:
      #    # print(i)
      #    # print(i['name'.
      #    # print(len(i['type']) ,  len(chosen_fee))
      #    if(course_chosen == -1):
      #       if(i['country'] == chosen_nationality and i['type'] == chosen_fee  ):
      #          print(i['name'] , end = " ")
      #    else:
      #       if(i['country'] == chosen_nationality and i['type'] == chosen_fee and i['course'] == chosen_course  ):
      #          print(i['name'], end = " ")
      # for i in data2:
      #    print(i['country'] , chosen_nationality)
      #    print(i['type'] ,  chosen_fee)
      #    print(i['course'] , chosen_level)
      #    print("---------------------------------------")
         
      for i in data2:
         if(i['country'] == chosen_nationality and i['type'] == chosen_fee and i['course'] == chosen_level  ):
               print(i['name'], end = " ")
      
      print("Your cost of fee (inc gst) is : " , amount)
      break

main()
   
   