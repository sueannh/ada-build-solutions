#optional enhancements: 
  #2) checking for duplicates
  #3) ensuring iflast 3 digits are <100 that student ID number can still be added to e-mail
  #4) account for first names with a space
  #5) read file with list of names to use as names list  - file needs to be saved in same file as code

import random

names = []
id_nums = []
emails = []
last_names = []
first_initials = []
new_id = ""

#read file with student_names
file = open("./student_names", "r")

#for each name in file, append to names list
for line in file:
  # line = line.read()
  names.append(line[:-1])

#close file
file.close()

print(f"{names} \n")

def get_full_name():
  student_name = input("full name: ")
  return student_name

#check whether first name is two words; return the number of spaces in the name
def check_spaces(name):
  count = 0

  for i in range(len(name)):
    if name[i] == " ":
      count += 1
  return count

#return the first initial(s)
def get_first_initial(name, count):
  first_initial = name[0]
  for i in range(len(name)):
    if count == 2:
      if name[i] == " ":
        first_initial += name[i+1]
        count += 1
  return first_initial

#return the last name
def get_last_name(name, count):
  if count == 1:
    for i in range(len(name)):
      if name[i] == " ":
        return name[i+1:]
  
  if count == 2:
    for i in range(len(name)-1, 0, -1):
      if name[i] == " ":
        return name[i+1:]
    
#create list of last names, list of id numbers, list of emails
for i in range(len(names)):
  #create list of first initials
  first_initials.append(get_first_initial(names[i], check_spaces(names[i])))
  
  #create list of last names
  last_names.append(get_last_name(names[i], check_spaces(names[i])))

  #creating a new id number
  new_id = random.randint(111111, 999999)
  
  #checking for duplicates
  while new_id in id_nums:
    # print(f"created a duplicate~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~", new_id)
    new_id = random.randint(111111, 999999)
 
  #adding the new id number to the list of id numbers
  id_nums.append(new_id)
  
  #creating list of emails
  str_idnum = str(id_nums[i])
  email = first_initials[i] + last_names[i] + str_idnum[3:] + "@example.org"
  emails.append(email)


# print(names)
# print(last_names)
# print(id_nums)
# print(emails)

for i in range(len(names)):
  print(f"name: {names[i]}")
  # print(f"first initials: {first_initials[i]}")
  # print(f"last name: {last_names[i]}")
  print(f"id: {id_nums[i]}")
  print(f"email: {emails[i]}\n")

def has_dupes(arr):
  for elem in arr:
    if arr.count(elem) > 1:
      return True
  # else    
  return False    

#asserts to test specific cases
assert has_dupes(id_nums) == False, "Found a duplicate"