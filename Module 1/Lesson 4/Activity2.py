# Taking total amount as imput from user
Amount =int(input("Please Enter Amount for withdraw :"))
# Calculating the number of notes of different denominations 
note_1 = Amount//100
note_2 =(Amount%100)//50
note_3 =((Amount%100)%50)//10
print( "notes of 100 rupees" , note_1)
print("notes of rupees" , note_2)
print("notes of 10 rupees" ,note_3)
               