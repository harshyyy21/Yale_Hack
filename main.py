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


"""def rel_fares(filename, budget, num_people, origin):
    d = {}
    with open (filename) as text:
        for line in text:
        line = line.strip()
        line = line.split(",")
        return line"""

print(add_fare("Deals.csv"))
