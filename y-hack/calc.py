from datetime import datetime
"""def split_dates(filename):
    d = {}
    with open (filename) as text:
        line_number = 0
        for line in text:
            line = line.strip()
            line = line.split(",")
            if line[7].isalpha() or line[8].isalpha():
                line_number += 1
                pass
            else:
                sep_date_times = line[3].split(" ")
                d[line_number] = sep_date_times
                line_number += 1
        return d"""

"""def make_datetime(filename):
    d = {}
    with open (filename) as text:
        line_number = 0
        for line in text:
            line = line.strip()
            line = line.split(",")
            if line[7].isalpha() or line[8].isalpha():
                line_number += 1
                pass
            else:
                date = datetime.strptime(line[3], '%m/%d/%y %H:%M')
                d[line_number] = date
                line_number += 1
        return d"""

def convert_user_datetime(user_date):
    date = datetime.strptime(user_date, '%m/%d/%y')
    return date

def rel_fares(filename, budget, num_people, origin, date):
    d = {}
    origin = origin.upper()
    with open (filename) as text:
        line_number = 1
        for line in text:
            line = line.strip()
            line = line.split(",")
            if line[0] == "BatchId":
                continue

            total_price = (float(line[7]) + float(line[8])) * float(num_people)
            new_date = convert_user_datetime(date)
            sep_date_times = line[3].split(" ")
            if ((round(total_price, 2) <= float(budget)) and (line[1] == origin) and (convert_user_datetime(sep_date_times[0]) >= new_date)):
                print (total_price)
                print (budget)
                d[line_number] = line[1:3] + sep_date_times + [line[4]] + [total_price]
                line_number += 1
                #print (d[line_number])
            else:
                line_number += 1
        return d

print(rel_fares("Deals.csv", 30, 1, "PAP", "12/23/17"))
