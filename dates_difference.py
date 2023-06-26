import datetime
from datetime import date

current = date.today().year
#current_year = current.year
#other = date(1066,12,16)
#other_year = other.year

#diff = current_year - other_year

#print(other_year," was ",diff," years ago")

print("ENTER YEAR")
user_year = input("")

date_user_year = datetime.datetime.strptime(user_year, '%Y')

fin_user_year = date_user_year.year

diff = current - fin_user_year

def get_difference():
    if diff > 0:
        print(fin_user_year,"AD was",diff,"years ago")
    else:
        n_year = abs(diff)
        print(fin_user_year,"AD is",n_year,"years in the future")
    
get_difference()
