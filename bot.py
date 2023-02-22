print("Hi there, Welcome to ABC Cafe customer support.How can I help you ?")
i = int(input("Press : 1 for 'Menu'; 2 for location of our nearby store; 3 book our cafe for any celebrations or parties; 4 for other queries"))
if i == 1:
    j = int(input("Press: 1 for Breads; 2 for Momos; 3 for Sandwiches; 0 for exit"))
    if j == 1:
     print("Breads")
    if j == 2:  
     print("Momos")
    if j == 3:
     print("Sandwiches")
    if j == 4:   
     print("Thank You")
    else:
     print("Invaid choise.")    
if i == 2:
    print("Location.....")
if i == 3:
    k = int(input("Press: 1 for Afternoon slot booking; 2 for evening slot booking; 3 for night slot booking"))
    if k  == 1: 
        print("Afternoon slot is from 12 P.M. to 4 P.M., $60 per hour.")
    if k  == 2: 
        print("Evening slot is from 5 P.M. to 8 P.M., $90 per hour.")
    if k  == 3: 
        print("Afternoon slot is from 9 P.M. to 12 A.M., $120 per hour.")
if i == 4:
    x = input("Please decribe you query.")
    print("Sorry we can't resolve your this query. Please call us on our toll-free no. XXXXX. or you can also visit our store.")        
