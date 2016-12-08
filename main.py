
from logic import print_people, Inputation, Closure

def Main():
  ''' Menu '''
  choice = input("Would like to enter your details, view currently entered details or close the program? [Enter/Current/Close] ")
  if choice == "Enter":
      Inputation()
  elif choice == "Current":
      print_people()
  else:
     Closure()
     exit()

  
if __name__ == '__main__':
  while True:
     Main()
