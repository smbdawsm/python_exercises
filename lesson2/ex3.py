number_of_month = int(input('please input number of month: '))
Winter = {
    1: "January",
    2: "February",
    12: "December" 
    }
Spring = {
    3: "March",
    4: "April",
    5: "May"
    }
Summer = {
    6: "June",
    7: "July",
    8: "August"
    }
Fall = {
    9: "September",
    10: "October",
    11: "November"
    }
dict_of_month = {
    "winter": ["January", "February", "December"],
    "spring": ["March", "April", "May"],
    "summer": ["June", "July", "August"],
    "Fall": ["September", "October", "November"]}
list_of_month = [Winter, Spring, Summer, Fall]
for el in list_of_month:
    if number_of_month in el:
        month = el.get(number_of_month)
for k, v in dict_of_month.items():
    if month in v:
        print(f'The time of the year is {k} and the name of month is {month}')
    

        