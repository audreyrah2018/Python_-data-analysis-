import pandas as pd
from pandas import *
import sys
import findPrint

#step 1 and step 2
# read the file and take care of any errors may result in reading the file

#d_frame = pd.read_excel(r"C:\Users\Davis\Desktop\Python_assignment 2\50000 Sales Records.xlsx")
if __name__ == "__assignment 2__":

    if not sys.argv[1:]:
        print("here is an Error empty argument. Please add the complete excel filename  with the full path :" )

        sys.exit(0)
    excel_file_input = sys.argv[1]

d_frame = pd.read_excel('50000 Sales Records.xlsx')


#Step 3
#group1 = d_frame.groupby('country')['total profit'].sum()[r1]  # have dictationary index then get series for ll of total profit then filter it by index particular country  we are reading

country_choice = (input("which country "))
Tot_prof = findPrint()
Tot_prof.country(country_choice, d_frame)


#Step 4
region_choice = (input("which region "))
Tot_region = findPrint()
Tot_region.region(d_frame)



# charts country - bar
bar_co = findPrint()
bar_co.bar_country(d_frame)




# charts region - bar
bar_re = findPrint()
bar_re.bar_region(d_frame)


# charts country - pie
pie_co = findPrint()
pie_co.pie_country(d_frame)




# charts region - pie
pie_region = findPrint()
pie_region.pie_region(d_frame)

