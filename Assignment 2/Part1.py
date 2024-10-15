def filterUsers(listOfTuples):
    countries = {'USA', 'Canada'}
    names = []
    filteredUsers = []
    for tuple in listOfTuples:
        if tuple[3] in countries and tuple[2] > 30:
            filteredUsers.append(tuple)
            names.append(tuple[1])
    return filteredUsers, names

def getTopOldest_and_findDuplicates(listOfTuples):
    sortedList = sorted(listOfTuples, key=lambda x:x[2], reverse=True)
    top10 = sortedList[:10]

    names = set()
    duplicates = []
    for tuple in listOfTuples:
        if tuple[1] in names:
            duplicates.append(tuple[1])
        else:
            names.add(tuple[1])
    return top10, duplicates

def main():
    listOfTuples = [
        (11, 'Umar', 21, 'Pakistan'),
        (13, 'John', 35, 'USA'),
        (14, 'Alex', 41, 'Canada'),
        (22, 'Adams', 33,  'California'),
        (17, 'Mustafa', 22, 'Pakistan'),
        (15, 'Ahmad', 19, 'India'),
        (18, 'Umar', 23, 'UK'),
        (21, 'Haroon', 38, 'USA'),
        (23, 'Hasaan', 25, 'Spain'),
        (19, 'Omer', 22, 'Pakistan')
    ]

    # part a
    filter, names = filterUsers(listOfTuples)
    print('---People Live in USA or Canada with Age More than 30 Are:')
    print('UserID\tName\tAge\tCountry')
    for tup in filter:
        print(f'{tup[0]}\t{tup[1]}\t{tup[2]}\t{tup[3]}')

    print('---People Live in USA or Canada with Age More than 30 Are:')
    for name in names:
        print(name)

    # part b
    top10, duplicates = getTopOldest_and_findDuplicates(listOfTuples)
    print('---Top 10 Oldest People are:')
    print('UserID\tName\tAge\tCountry')
    for tup in top10:
        print(f'{tup[0]}\t{tup[1]}\t{tup[2]}\t{tup[3]}')

    print('---People with Duplicates Names Are:')    
    for name in duplicates:
        print(name)


main()
