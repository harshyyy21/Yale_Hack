def add_fare(filename):
    d = {}
    with open (filename) as text:
        for line in text:
            if lists[7].isalpha() or lists[8].isalpha():
				pass
            else:



def rel_fares(filename, budget, num_people, origin):
    d = {}
    with open (filename) as text:
        for line in text:
        line = line.strip();
        line = line.split(",")
        return line

print(rel_fares("Deals.csv", 700, 4, "Chicago"))
