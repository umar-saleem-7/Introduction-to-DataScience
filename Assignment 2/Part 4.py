def filterUser(dic):
    newDic = {}
    for key, value in dic.items():
        if value['rating'] >= 4:
            newDic[key] = value['rating']
    
    sortedDic = dict(sorted(dic.items(), key=lambda item: item[1]['rating'], reverse=True)[:5])

    return newDic, sortedDic

def combineDic(*dics):
    combinedDic = {}
    for dic in dics:
        for key, value in dic.items():
            if key not in combinedDic:
                combinedDic[key] = value
            else:
                combinedDic[key]['rating'] = max(combinedDic[key]['rating'], value['rating'])
                combinedDic[key]['comments'] += ',' + value['comments']
    ratedDic ={}
    for key, value in combinedDic.items():
        if value['rating'] >= 3:
            ratedDic[key] = value['rating']
    return combinedDic, ratedDic
        
def main():
    dic = {
        101: {'rating': 5, 'comments': 'Great service!'},
    102: {'rating': 3, 'comments': 'Average experience.'},
    103: {'rating': 4, 'comments': 'Good, but could be better.'},
    104: {'rating': 2, 'comments': 'Not satisfied with the support.'},
    105: {'rating': 5, 'comments': 'Excellent! Very happy with the product.'},
    106: {'rating': 4, 'comments': 'Quite good.'},
    107: {'rating': 3, 'comments': 'Could improve service.'},
    108: {'rating': 5, 'comments': 'Perfect! Loved it.'},
    109: {'rating': 1, 'comments': 'Very bad experience.'},
    110: {'rating': 4, 'comments': 'Satisfied with the overall experience.'}
    }

    dic2 = {
    104: {'rating': 2, 'comments': 'Not satisfied with the support.'},
    103: {'rating': 5, 'comments': 'Excellent improvement!'},
    105: {'rating': 5, 'comments': 'Very happy with the product.'}
    }

    filteredDic, sortedDic = filterUser(dic)
    print('---Users with Rating 4 or Higher: ')
    for userid, rating in filteredDic.items():
        print(f'User with userID {userid} has Rating {rating}')
    print('---Top 5 Users with high Rating: ')
    for userid, feedback in sortedDic.items():
        rating = feedback['rating']
        comments = feedback['comments']
        print(f'User with userID {userid} has Rating {rating} and comments {comments}')
    comb, rated = combineDic(dic, dic2)
    print('---Combined Dictionary is: ')
    print(comb)
    print('---User with Rating 3 or higher: ')
    for userid, rating in rated.items():
        print(f'User with userID {userid} has Rating {rating}')


main()
