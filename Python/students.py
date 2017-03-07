# students = [
#      {'first_name':  'Michael', 'last_name' : 'Jordan'},
#      {'first_name' : 'John', 'last_name' : 'Rosales'},
#      {'first_name' : 'Mark', 'last_name' : 'Guillen'},
#      {'first_name' : 'KB', 'last_name' : 'Tonel'}
# ]

# def get_name(array):
#         for val in array:
#             print val["first_name"] + " " + val["last_name"]
        

# get_name(students)




users = {
 'Students': [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
  ],
 'Instructors': [
     {'first_name' : 'Michael', 'last_name' : 'Choi'},
     {'first_name' : 'Martin', 'last_name' : 'Puryear'}
  ]
 }


def printPeople(array):
    print "Students"
    i = 1
    j = 1
    for val in array["Students"]:
        print str(i) + " - " + val["first_name"] + " " + val["last_name"] + " - " + str(len(val["first_name"]) + len(val["last_name"]))
        i += 1
    print "Instructors"
    for val in array["Instructors"]:
        print str(j) + " - " + val["first_name"] + " " + val["last_name"] + " - " + str(len(val["first_name"]) + len(val["last_name"]))
        j += 1

printPeople(users)