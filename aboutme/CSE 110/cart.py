action = ""
shopping_list=[] 
price_list=[]
while action != "5":
    print("""Please select one of the following: 
    1. Add item
    2. View cart
    3. Remove item
    4. Compute total
    5. Quit """)
    
    action = input("Please enter an action: ")
    if action == "1": 
        item=  input("what item would you like to add?")
        price= float(input("what is the price of the item?$"))
        
        print(f"the item is {item}")
        shopping_list.append(item)
        price_list.append(price)
        print(shopping_list)
        
    elif action == "2":
        for content in shopping_list:
            print (content)
        
        for i in range(len(shopping_list)):
            print (f"{i+1}.{shopping_list[i]} - {price_list[i]}")
            
    elif action == "4":
        total = 0
        for price in price_list:
            total = price + total
        print(f"the total price of the items in the shopping cart is {total}")
    elif  action == "3":
        remove = int(input("which item would you like to remove"))
        if len(shopping_list)> remove:
            shopping_list.pop(remove-1)
            price_list.pop(remove-1)
        else :
            print("sorry that is not a valid item number")

                
