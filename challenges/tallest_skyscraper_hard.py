def tallest_skyscraper(lst):
    count = -1
    for mini_list in lst:
        count += 1
        if 1 in mini_list:
            break

    return len(lst) - count