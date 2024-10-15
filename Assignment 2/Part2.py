def totalUniqueUsers(tupleOfTuple):
    uniqueUsers = set()
    for transaction in tupleOfTuple:
        uniqueUsers.add(transaction[1])
    return len(uniqueUsers)

def maxAmount(tupleOfTuple):
    maxAmount = 0
    transac = None
    for transaction in tupleOfTuple:
        if len(transaction) != 4:
            print('Skip This Transaction Due to Incomplete Information')
            print(transaction)
            continue
        try:
            if transaction[2] > maxAmount:
                maxAmount = transaction[2]
                transac = transaction
        except IndexError:
            print('Failed to Process This Transaction Due to Indexes are not valid, or Some Other Errors')
    return transac

def main():
    transactions = (
    (1, 100, 25050, "2024-01-01 10:00:00"),
    (2, 101, 30075, "2024-01-01 11:15:00"),
    (3, 102, 150.00),
    (4, 103),
    (5, 104, 22550, "2024-01-02 14:00:00"),
    (6, 105, 12500, "2024-01-03 16:30:00"),
    (7, 106, 35025, "2024-01-03 17:00:00"),
    (8, 107, 40050, "2024-01-04 10:15:00"),
    (9, 108, 17575, "2024-01-04 11:45:00"),
    (10, 109, 27500, "2024-01-05 12:00:00")
    )

    unique_users = totalUniqueUsers(transactions)
    print('---Total Number of Unique Users: ', unique_users)
    print()
    tup = maxAmount(transactions)
    print(f'---Transaction With Highest Amount:\nTransactionID: {tup[0]}\tUserID: {tup[1]}\tAmount: {tup[2]}\tTimestamp: {tup[3]}')

main()
