def tallest_skyscraper(lst):
    found_one = False
    count = -1
    for mini_list in lst:
        count += 1
        if 1 in mini_list:
            found_one = True
            break
    
    if found_one:
        return len(lst) - count

    return 0