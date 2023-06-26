import datetime
from datetime import date

current = date.today().year

#######
#current_year = current.year
#other = date(1066,12,16)
#other_year = other.year
#diff = current_year - other_year
#print(other_year," was ",diff," years ago")
#######

## user enters year
print("ENTER YEAR (YYYY)")
user_year = input("")

## strip datetime from entered year
date_user_year = datetime.datetime.strptime(user_year, '%Y')

## get year from datetime object
fin_user_year = date_user_year.year

## calculate difference in years between the dates
diff = current - fin_user_year

## adjust output depending on past or future year
def get_difference():
    if diff > 0:
        print(fin_user_year,"AD was",diff,"years ago")
    else:
        n_year = abs(diff)
        print(fin_user_year,"AD is",n_year,"years in the future")
    
get_difference()
