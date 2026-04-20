
contacts = []

class Contact_Book:
    def __init__(self):
       pass
        
    def add_contact(self):
        
        name = input("Enter the name : ").lower()
        number = input("Enter the number : ").strip()
        length = len(number)
        
        
        if length!=10:
            print("number should be 10 digits")
            self.add_contact()
       
        
        try:
            number = int(number)
        except:
             number = input("it should only contain number :")
        if type(int(number)) != int :
            print("only enter numbers")
            self.add_contact()
        num_str = str(number)
        
        
        email = input("Enter the email : ")
        
        
        whatsapp = input(" Is number connected to whatsapp  choose 1 or 23 ? \n1.yes\n2.no\n").lower()
        
        
        
        insta_id = input("Enter your insta Id : ")
        linkdin_id = input("Enter your linkdin_id : ")
       
            
        
        contact = {
            "name" : name,
            "number" :number,
            "email" : email,
            "whatsapp" :whatsapp,
            "insta_id" :insta_id,
            "linkdin_id":linkdin_id
        }
        contacts.append(contact)
        
    def show_contact(self):
        if contacts == []:
            print("empty contact book")
            return
        name = input("Enter the name : ").lower()
        for contact in contacts:
            if name == contact["name"]:
               print("=============================")
               print(f"contact holder name = {name}\ncontact holder number = {contact["number"]}\ncontact holder email = {contact["email"]}\ncontact holder insta_id = {contact["insta_id"]}\ncontact holder linkdin_id = {contact["linkdin_id"]}")
               print("=============================")
               return 
        print("contact not found")
        print("=============================")
        
    def show_all(self):
        if contacts == []:
            print("empty contact book")
            return
        for contact in contacts:
            print("=============================")
            print(f"contact holder name = {contact["name"]}\ncontact holder number = {contact["number"]}\ncontact holder email = {contact["email"]}\ncontact holder insta_id = {contact["insta_id"]}\ncontact holder linkdin_id = {contact["linkdin_id"]}")
            print("=============================")
        print("printed all contacts")
        print("=============================")
            
    def delete_contact(self):
        if contacts == []:
            print("empty contact book")
            return
        print("=============================")
        name = input("Enter the name : ").lower()
        for contact in contacts:
            if contact['name'] == name:
                contacts.remove(contact)
                print(f"contact of {name} is successfully removed")
                return
        print("contact not found to delete")
        print("=============================")
        
    def check_whatsapp(self):
        if contacts == []:
            print("empty contact book")
            return
        
        print("=============================")
        name = input("Enter the name : ")
        for contact in contacts :
            if contact["whatsapp"] == "1":
                print("number has whatsapp")
                print("=============================") 
                return
            elif contact["whatsapp"] == "2":
                print("no whatsapp connectes")
                print("=============================")
                return
        print(f"contact not found with the name {name}")
        print("=============================")
        
    
    
    def update_contact(self):
        if contacts == []:
            print("empty contact book")
            return
        print("=============================")
        name = input("Enter the contact name which you want to updats : ")
        for contact in contacts:
            if contact["name"] == name:
                
                new_number = input("Enter new number")
                length = len(new_number)
                if length!=10:
                    print("number should be 10 digits")
                    self.update_contact()
                try :
                    new_number = int(new_number)
                except:
                    new_number = int(input("only keep numbers with 10 digits :"))
                if(type(new_number) != int):
                    print("must have only numbers , try again :")
                    self.update_contact
                
        
                contact["number"] = new_number # update the value
                print("Contact updated successfully")
                print("=============================")
                return
        print("contact not found")
        print("=============================")
        
    def update_name(self):
        if contacts == []:
            print("empty contact book")
            return
        print("=============================")
        name = input("Enter the contach holder name which you want to change : ")
        for contact in contacts:
            if contact["name"] == name:
                old_name = name
                new_name = input("Enter new Name")
                contact["name"] = new_name
                print(f"{old_name} is changes to new one {new_name} successfully ")
                return
        print(f"{name} is not found in the contact book")
        print("=============================")
        
    def update_email(self):
        if contacts == []:
            print("empty contact book")
            return
        print("=============================")
        name = input("Enter the contact holder name which you want to change : ")
        for contact in contacts:
            if name == contact["name"]:
                old_email = contact["email"]
                new_email = input("Enter the new mail")
                contact["email"] = new_email
                print(f"{old_email} is changes to new one {new_email} successfully ")
                print("=============================")
                return
        print(f"{name} is not found in the contact book")
        print("=============================")
                
        
    #user controls
    
b1 = Contact_Book()
    
while True:
    print("===================")
    print("1.Add contact \n2.Show  contact \n3.show all contacts \n4.Delete contact \n5.update contact number \n6.update_name\n7.update_email\n8.check_whatsapp\n9.Exit \n " )
    print("===================")
    
    choice = input("enter your choice : ")
    
    if choice == "1":
        b1.add_contact()
    elif choice == "2":
        b1.show_contact()
        
    elif choice =="3":
        b1.show_all()
    
    elif choice == "4":
        b1.delete_contact()
        
    elif choice == "5":
        b1.update_contact()
        
    elif choice == "6":
        b1.update_name()
        
    elif choice == "7":
        b1.update_email()
        
    elif choice == "8":
        b1.check_whatsapp()
        
    elif choice =="9":
        break
    
    else:
        print("Invallied input")
            


        

