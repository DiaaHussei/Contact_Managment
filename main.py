#-------------------------
# This [progarm] is just for practic
#----------------------------
import os 
# I just import os to use "cls" command to claen the screen after every process#
class Contact:
    def __init__(self, name, phone, email):
        self.name = name
        self.phone = phone
        self.email = email
    def __str__(self):
        return f"Name:{self.name}\nNumber:{self.phone}\nEmail:{self.email}" #return a human readable string 
    

class ContactManager:
    # this class who control of the contact class#
     
    def __init__(self, *cont):
        self.member = list(cont)
        
    def  add_contact(self, contect):
        self.member.append(contect)

    def remove_contact(self, name):
        try:
         if name in self.member:
          self.member.remove(name)
          print("Deleteing is Done")
         else:
          print("the name that you entered is not exsist!!!")
        except:
           print(" somthing wornt wrong *__*")

    def showAll(self):
        
        for contact in self.member:
            if contact is not None:
             print(contact)
            else:
               print("The contact is Empty")


def main():
   con = ContactManager()
   falge = None
   
   while True:
      print("----Contact Manager----\n\n")
      print("1.Add contact")
      print("2.Delete contact")
      print("3.Search of contact")
      print("4.Disply contacts")
      print("5.Exsit")
      falge = input()
      if falge == "1" :
         name = input("Enter the name:")
         num = input("Enter the number:")
         mail = input("Enter the email:")

         new_contact = Contact(name, num, mail)
         con.add_contact(new_contact)
         os.system('cls')
      elif falge == "2":
         print("please Enter the name that you want to DELETE:")
         name_to_remove = input()
         con.remove_contact(name_to_remove)

      elif falge == "3":
         pass
         #name = input("Please Enter the name to seaerch for a contact:")

      elif falge == "4": 
         con.showAll()
        
      elif falge  == "5" or "exit":
         print("Goodbye ^__^")
         break
      else:
         print('Sorry Wrong Opastion')         






      
#----------------------------------------------------------


if __name__ == "__main__":
 # ------self test code------------
    # co = Contact("ali", 77772444, "email@email.com")
    # print(co.__str__())
    # t = ContactManager("deay", 252521, "teisa@dasd.com")
   # num = input("prass number 1")

    # t.showAll()
    # t.remove_contact("all")
    # t.showAll()

    main()
        