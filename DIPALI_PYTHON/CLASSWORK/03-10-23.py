# product manager
product_menu={}  
menu="""
               press 1 for product manager
               press 2 for customer
               press 3 for exit 
              
    """ 
status=True
p_status=True
while status:
     print(menu)
     choice=int(input("Enter your choice: "))
     if choice==1:
         while p_status:
             spec={}
             print("WELCOME TO PRODUCT MANGER")
             product_name=input("Enter product name: ")
             qty=int(input("Enter qty: "))
             amount=int(input("Enter amount: "))
             if product_name in product_menu.keys():
                 spec['qty']=product_menu[product_name]['qty']+qty
                 spec['amount']=amount
             else:
                 spec['qty']=qty
                 spec['amount']=amount
             product_menu[product_name]=spec
             print(product_menu)
             p_choice=input("DO YOU WANT TO ADD MORE PRODUCT? (y/n) ")
             if p_choice=='n':
                 p_status=False
     elif choice==2:
         print("customer")
     else:
         print("THANK YOU FOR USING THIS APPICATION")
         status=False