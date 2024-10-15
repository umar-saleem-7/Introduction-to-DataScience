def commonUsers(setA, setB, setC):
    print('---Users that visited Both Page A and Page B')
    for user in setA:
        if user in setB:
            print(user, end='  ')
    print()
    print('---Users that Visited Either Page A or Page C, but not Both')
    users = setA ^ setC
    for user in users:
        print(user, end='  ')
    print()
    return

def updatePageA(pageA, newUsers):
    pageA.update(newUsers)
    return pageA

def removeFromPageB(pageB, listToRemove):
    pageB.difference_update(listToRemove)
    return pageB

def main():
    pageA = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
    pageB = {1, 5, 8, 9, 11, 13, 6, 15, 19, 4}
    pageC = {2, 5, 9, 10, 13, 18, 19, 20, 21, 7}

    commonUsers(pageA, pageB, pageC)
    updatedPageA = updatePageA(pageA, [22, 14, 17])
    print(f'---Updated Page A with new Users is:\n {updatedPageA}')
    removefrompageB = removeFromPageB(pageB, [13, 15, 4])
    print(f'---Page B After Removing list of Users:\n {removefrompageB}')

main()

