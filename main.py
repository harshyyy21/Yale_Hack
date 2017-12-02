from datetime import datetime
def add_fare(filename):
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
                total_fare = float(line[7]) + float(line[8])
                total_fare = round(total_fare, 2)
                d[line_number] = total_fare
                line_number += 1
        return d

def split_dates(filename):
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
        return d

def make_datetime(filename):
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
        return d

def convert_user_datetime(user_date):
    date = datetime.strptime(user_date, '%m/%d/%y')
    return date

def rel_fares(filename, budget, num_people, origin, date):
    d = {}
    with open (filename) as text:
        line_number = 1
        for line in text:
            line = line.strip()
            line = line.split(",")
            if line[0] == "BatchId":
                continue
            total_price = float(add_fare(filename)[line_number]) * float(num_people)
            new_date = convert_user_datetime(date)
            if total_price <= budget and line[1] == origin and convert_user_datetime(split_dates(filename)[line_number][0]) >= new_date:
                d[line_number] = line[1:3] + split_dates(filename)[line_number] + [line[4]] + [add_fare(filename)[line_number]]
                line_number += 1
            else:
                line_number += 1
        return d

#print(add_fare("Deals.csv"))
print(rel_fares("Deals.csv", 400, 1, "FLL", "12/6/17"))
#print(make_datetime("Deals.csv"))
#print split_dates("Deals.csv")
