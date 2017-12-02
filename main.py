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
                d[line_number] = total_fare
                line_number += 1
        return d


def rel_fares(filename, budget, num_people, origin):
    d = {}
    with open (filename) as text:
        line_number = 1
        for line in text:
            line = line.strip()
            line = line.split(",")
            if line[0] == "BatchId":
                continue
            total_price = float(add_fare(filename)[line_number]) * float(num_people)
            if total_price <= budget:
                d[line_number] = line[1:5] + [add_fare(filename)[line_number]]
                line_number += 1
            else:
                line_number += 1
        return d

#print(add_fare("Deals.csv"))
print(rel_fares("Deals.csv", 400, 1, "JFK"))
