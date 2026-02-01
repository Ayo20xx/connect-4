class BankAccount:
    def __init__(self,balance=0):
        
        if balance<0:
            raise ValueError("invalid amount")
        self.balance=balance
    def deposit(self,much):
        if much<=0:
             print("invalid figure")
        else:
            self.balance += much
            return("deposited successfully")
       
    def withdraw(self,much):
         if self.balance< much:
             raise ValueError("insufficient balance")
         else:
             self.balance -= much
             return("transaction successful")
             
    def Show_amount(self) :
        return(f"${self.balance}")
    def __str__(self):
         return f"{self.balance}"


   
   
def main():

    bank=BankAccount()
    print (bank)
    while True:
      print("1.Deposit")
      print("2.withdraw")
      print ("3.check balance")
      print("4.exit")
        
      
      try:
            user= int(input("what do you want to do: "))
            if user==1:
                    bank.deposit(int( input("how much: ")))
                    
            elif user ==2:
                    close=(bank.withdraw(int( input("how much: "))))
                    print(close)
            elif user ==3:
                size=( bank.Show_amount())
                print(size)

            elif user==4:
                    break
      except ValueError as e:
        print(e)


if __name__ == "__main__":
    main()
         



class TodoItem:
     def __init__(self,title,done=False):
          self.title=title
          self.done=done
    
     def mark_done(self):
      self.done=True


# class TodoList:
#      def __init__(self,items=[]):
#         self.items=items[TodoItem]

     
#      def add_items(): 
      

#      def complete_item(self,index):





class functionchecker:
     def __init__(self):
          pass