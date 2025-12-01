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

#ARM task 2
def compute_rule_counts(rule, table):
    Nleft = Nright = Nboth = 0
    Ntotal = len(table)
    for row in table:
        Nleft += check_row_match(rule["lhs"], row)
        Nright += check_row_match(rule["rhs"], row)
        Nboth += check_row_match(rule["lhs"] + rule["rhs"], row)

    return Nleft, Nright, Nboth, Ntotal

#ARM task 3
def compute_rule_interestingness(rule, table):
    Nleft, Nright, Nboth, Ntotal = compute_rule_counts(rule, table)
    print(Nleft, Nright, Nboth, Ntotal)
    rule["confidence"] = Nboth / Nleft
    rule["support"] = Nboth / Ntotal
    rule["completeness"] = Nboth / Nright

for rule in [rule1, rule5]:
    compute_rule_interestingness(rule, table)
    print(rule)


# Set Theory Basics (Important for Apriori)
# A set is an unordered collection with NO duplicates.
# Python has a built-in set type that takes care of that.

transaction = ["chocolate", "grahams", "chocolate", "marshmallows"]
transaction_set = set(transaction)
print("set:", transaction_set)

# Notes:
# - Duplicate "chocolate" is removed.
# - Order is lost because sets are unordered.
# - Apriori sometimes requires ORDERED itemsets,
#   so we will convert sets back to sorted lists later.

# Union and Intersection
# A ∪ B (Union): items in A OR B (or both)
# A ∩ B (Intersection): items in BOTH A and B
# Apriori needs union() when combining itemsets.
# transaction_set.union()
# or...
# with lists
# example: we have a set (list) LHS and a set (list) RHS of a rule
# union is sorted(LHS + RHS)
# LHS intersect RHS = 0 (empty set)
# there won't be any duplicates with this union

# Subset Checking
# A ⊆ B if ALL elements of A appear in B.
# set has issubset()
#   A.issubset(B)
# or
# using lists instead of sets, we can define:
#   check_row_match(A, B) -> 1 if A is a subset of B, else 0


# Powerset (All Possible Subsets)
# Powerset = all subsets of a set including empty set and itself.

# convert our set to a sorted list to preserve order
transaction = sorted(list(transaction_set))
print("list:", transaction)

# generate the powerset using itertools.combinations()
powerset = []
for i in range(len(transaction) + 1):
    powerset.extend(itertools.combinations(transaction, i))

print("powerset:", powerset)

# each element of powerset is a tuple representing a subset.


# each row in our dataset is a "transaction" ("itemset")
# Apriori Lab!!!

# Apriori starter code
transactions = [
 ["b", "c", "m"],
 ["b", "c", "e", "m", "s"],
 ["b"],
 ["c", "e", "s"],
 ["c"],
 ["b", "c", "s"],
 ["c", "e", "s"],
 ["c", "e"]
]

# NOTE: Apriori Lab task #1: find the set I
def compute_unique_values(table):
    unique = set()
    for row in table:
        for value in row: 
            unique.add(value)
    return sorted(list(unique))

transactions_I = compute_unique_values(transactions)
print(transactions_I)
interview_I = compute_unique_values(table)
print(interview_I)

# NOTE: apriori algorithm step 4 prune step: examine all susbets of c with k - 1 elements
def compute_k_minus_1_subsets(itemset):
    # or use itertools.combinations()
    subsets = []
    for i in range(len(itemset)):
        subsets.append(itemset[:i] + itemset[i + 1:])
    return subsets


# compute support of an itemset 
def compute_support(itemset, table):
    count = 0
    for row in table:
        if check_row_match(itemset, row):
            count += 1
    return count / len(table)

# combine itemsets to generate candidate (4a)
def combine_itemsets(Lkminus1, k):
    candidates = []
    # TODO: Loop through all pairs of itemsets in Lkminus1
    # for each pair A, B:
    # check if first k-2 items are the same (prefix match)
    # combine A and B to form a candidate of size k
    # ensure candidate has exactly k items and is not already in the list
    # append valid candidate to candidates
    return candidates


# prune candidates whose subsets are not a member of Lk-1 (4b)
def prune_candidates(Ck, Lkminus1):
    candidates_after_pruning = []
    # TODO: 
    # for each candidate in Ck
    # generate all (k-1)-sized subsets of the candidate
    # check if all subsets are in Lkminus1
    # if yes, append candidate to candidates_after_pruning list
    
    return candidates_after_pruning


# NOTE: Apriori Lab task #4/5: generate confident rules using supported itemsets
def generate_apriori_rules(supported_itemsets, table, minconf):
    rules = []
    # for each itemset S in supported_itemsets
    # generate the 1 term RHSs and the corresponding LHSs
    # check confidence >= minconf => append to rules
    # move on to the 2 term RHS...upto len(S)-1 term RHS
    return rules 

# NOTE: Apriori Lab task #3: find supported itemsets
def apriori(table, minsup, minconf):
    # goal is to generate and return supported and confident rules
    # TODO: finish apriori implementation
    supported_itemsets = []
  
    
    #step1: create L1 (set of supported itemsets of cardinatiy one)
    I = compute_unique_values(table)
    L1 = []
    for item in I:
        #check support of singleton
        if compute_support([item], table) >= minsup:
            L1.append([item])

    #step2: Initialize k
    k = 2
    Lkminus1 = L1
    # step3: loop while there are supported itemsets in previous level
    while Lkminus1:
        # step 4 : Generate candidates from Lk-1
        #step4a: join candidates
        Ck = combine_itemsets(Lkminus1, k)
        
        # step4b: prune candidates
        Ck = prune_candidates(Ck, Lkminus1)
        
        # step5: prune all itemsets in Ck, that are not supported, to create Lk
        Lk = []
        for candidate in Ck:
            if compute_support(candidate, table) >= minsup:
                Lk.append(candidate)
        supported_itemsets.extend(Lk)
        
        # prepare for next iteration
        Lkminus1 = Lk
        #step6: increase k by 1
        k += 1
    #print("Supported itemsets", supported_itemsets)
    rules = generate_apriori_rules(supported_itemsets, table, minconf)
    return rules 

k2_subsets = compute_k_minus_1_subsets(["c", "e", "s"])
print(k2_subsets) # [[c, e], [c, s], [e, s]]

rules = apriori(transactions, 0.25, 0.8)
print(rules) # TODO: check against your hand trace from Apriori Lab tasks #4/5
