def add_fare(filename):
    d = {}
    with open (filename) as text:
        line_number = 0
        for line in text:
            if lists[7].isalpha() or lists[8].isalpha():
				pass
            line_number += 1
            else:
                total_fare = int(lists[7]) + int(lists[8])
                d[line_number] = total_fare
        return d


def rel_fares(filename, budget, num_people, origin):
    d = {}
    with open (filename) as text:
        for line in text:
        line = line.strip();
        line = line.split(",")
        return line

print(rel_fares("Deals.csv", 700, 4, "Chicago"))
