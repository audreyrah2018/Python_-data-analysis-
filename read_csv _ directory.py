import csv

f = open("csv_files\\50000 Sales Records.csv", 'rt')
w = open("csv_files\\filtered.csv", 'w', newline="")
reader = csv.reader(f)
writer = csv.writer(w)



next(reader)

step1 = []  #make a list
total_profit_counter = 0

temp_list = [] , []
for row in reader:

   temp_list =[]

   temp_list.append(row[0])
   temp_list.append(row[1])
   temp_list.append(row[13])
   print(temp_list)
#writer.writerow(temp_list)


country_choice = (input("Which country : or region you would like to choose"))

for row in temp_list:
    for j in range(0,3):

        if temp_list[row][j] == country_choice:
            print(temp_list[row][j])
            found = True


if found:
    print('region: ', temp_list[0])
    print('country: ', temp_list[1])
    print('Total Profit: ', temp_list[13])


else:
    print('it is not fond', country_choice)
    print(temp_list[1][2])

#if country_choice in temp_list
   # print("jjjjjjjjjjjjjjjjjjjj")
#else :
  # print("noooo")




#for r1 in (row[1]):
   #group1 = temp_list.groupby(row[1])(row[13]).sum()[r1]
       # have dictationary index then get series for ll of total profit then filter it by index particular country  we are reading

#print(group1)
"""This function get a country as an argument and return the total profit in that country"""




f#or r1 in step1:
  #  if r1[0] == "Europe":
     #   Europe_counter += 1

    #total_profit_counter +=1

#print("Total records which apply to Europe{}".format(Europe_counter))
#print("Total records which apply to Europe{}".format(total_profit_counter))