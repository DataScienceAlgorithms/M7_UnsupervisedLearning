import itertools

header = ["level", "lang", "tweets", "phd", "interviewed_well"]
table = [
        ["Senior", "Java", "no", "no", "False"],
        ["Senior", "Java", "no", "yes", "False"],
        ["Mid", "Python", "no", "no", "True"],
        ["Junior", "Python", "no", "no", "True"],
        ["Junior", "R", "yes", "no", "True"],
        ["Junior", "R", "yes", "yes", "False"],
        ["Mid", "R", "yes", "yes", "True"],
        ["Senior", "Python", "no", "no", "False"],
        ["Senior", "R", "yes", "no", "True"],
        ["Junior", "Python", "yes", "no", "True"],
        ["Senior", "Python", "yes", "yes", "True"],
        ["Mid", "Python", "no", "yes", "True"],
        ["Mid", "Java", "yes", "no", "True"],
        ["Junior", "Python", "no", "yes", "False"]
    ]

# warmup
def prepend_attribute_label(table, header):
    for row in table:
        for i in range(len(row)):
            row[i] = header[i] + "=" + str(row[i])

prepend_attribute_label(table, header)
for row in table:
    print(row)
# why do this? if we represent each row as a set, we can't distinguish
# between tweets and phd because they have overlapping domains




# how to represent rules in python?
# use dictionaries!
# rule #1 IF interviewed_well=False THEN tweets=no
rule1 = {"lhs": ["interviewed_well=False"], "rhs": ["tweets=no"]}
# rule #5 IF phd=no AND tweets=yes THEN interviewed_well=True
rule5 = {"lhs": ["phd=no", "tweets=yes"], "rhs": ["interviewed_well=True"]}

#helper function
def check_row_match(terms, row):
    # return 1 if all the terms are in the row (match)
    # return 0 otherwise
    for term in terms:
        if term not in row:
            return 0
    return 1

#TODO 
# ARM lab task #2
# ARM lab task #3
