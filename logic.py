from person import Person
import pickle

try:
   with open('personSave.pickle', 'rb') as f:
       people = pickle.load(f)
except Exception as e:
   print ('Error:' + str(e) + '\nPogram will create file at closure.')
   people = []

def print_people():
   ''' Iterates through the people lists and prints out the details '''

   for person in people:
       print ('{0} {1} is {2} years old'.format(person.firstname, person.surname, person.age))

def Inputation():
  ''' User can input their own details '''
      
  inp_firstname = input("What is your first name? ")
  inp_surname = input("What is your surname? ")
  inp_dob = input("What is your date of birth? Please enter in the form MMM DD YYYY ")
  P = Person(inp_firstname, inp_surname, inp_dob)
  people.append(P)

def Closure():
   '''Writes pickle file'''

   with open('personSave.pickle', 'wb') as f:
       pickle.dump(people,f,protocol=pickle.HIGHEST_PROTOCOL)
       
