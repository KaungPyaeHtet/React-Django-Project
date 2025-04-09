#   Q6

#   Structure of sales record is
#   StaffID, First name, Last name, January sales, February sales,
#   March sales, April sales, May sales, June sales

staffSales = [
["101TGY" , "George" , "Taylor" , 6009 , 5262 , 3745 , 7075 , 1943 , 4432],
["103FCY" , "Fehlix" , "Chayne" , 8717 , 2521 , 5777 , 6189 , 5089 , 6957],
["102SBY" , "Sumren" , "Bergen" , 5012 , 1063 , 7937 , 9560 , 1115 , 5499],
["104SBK" , "Samira" , "Beckle" , 1140 , 9206 , 3898 , 8544 , 5937 , 8705],
["105NBT" , "Nellie" , "Bogart" , 3017 , 3342 , 5939 , 2479 , 3374 , 2297],
["106CGT" , "Cheryl" , "Grouth" , 9620 , 7160 , 5113 , 4803 , 5492 , 2195],
["107DGT" , "Danuta" , "Graunt" , 1583 , 7450 , 1026 , 7463 , 2390 , 6509],
["108JDN" , "Jaiden" , "Deckle" , 4064 , 4978 , 2984 , 3159 , 1464 , 4858],
["109JCK" , "Jimran" , "Caliks" , 6253 , 7962 , 2732 , 7504 , 2771 , 5193],
["110DDN" , "Deynar" , "Derran" , 6305 , 8817 , 5200 , 3647 , 3365 , 1256]
]

#--------------------------------------------------------------------------
#   Write your code below this line
first = ""
second = ""
first_sale = 0
second_sale = 0
sale_whole = 0
for index in range(len(staffSales)):
    staff_length = len(staffSales[index])
    sale_each = 0
    for j in range(3, staff_length):
        sale_each += staffSales[index][j]
    sale_whole += sale_each
    print(staffSales[index][1], staffSales[index][2], ":", sale_each)
    if first_sale < sale_each:
        second_sale = first_sale
        second = first
        first_sale = sale_each
        first = staffSales[index][1] + " " + staffSales[index][2]
    elif second_sale < sale_each:
        second = staffSales[index][1] + " " + staffSales[index][2]
        second_sale = sale_each

print("The team made", sale_whole)

print("Highest:", first)
print("Second Highest:", second)
