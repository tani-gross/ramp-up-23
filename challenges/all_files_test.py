import circle_or_square_easy
import discount_percentage_easy
import highest_integer_recursion_medium
import increment_very_easy
import sum_of_even_and_odd_medium
import tallest_skyscraper_hard
import two_number_sum_very_easy
import uncensor_hard

def test_circle_greater():
    assert circle_or_square_easy.circle_or_square(5, 7.5) == True

def test_square_greater():
    assert circle_or_square_easy.circle_or_square(5, 8) == False

def test_discount():
    assert discount_percentage_easy.dis(200, 20) == 160
    assert discount_percentage_easy.dis(100, 5) == 95

def test_highest_integer():
    assert highest_integer_recursion_medium.find_highest([-2,7,-10,98,1090,4,78,3,-10,10000,96,3]) == 10000

def test_increment():
    assert increment_very_easy.increment(-2) == -1
    assert increment_very_easy.increment(10) == 11
    
def test_even_odd_sum():
    assert sum_of_even_and_odd_medium.sum_odd_and_even([1,2,3,4,5,6,7,8,9,10,-2,-5]) == [28, 20]

def test_skyscraper():
    grid = [
        [0,0,0,0,0],
        [0,1,0,1,0],
        [1,1,0,1,0],
        [1,1,1,1,1]
    ]

    grid2 = [
        [0,0,0],
        [0,0,0],
        [0,0,0]
    ]

    grid3 = [[1,0,1]]

    assert tallest_skyscraper_hard.tallest_skyscraper(grid) == 3
    assert tallest_skyscraper_hard.tallest_skyscraper(grid2) == 0
    assert tallest_skyscraper_hard.tallest_skyscraper(grid3) == 1

def test_two_sum():
    assert two_number_sum_very_easy.add_two_numbers(5, 10) == 15
    assert two_number_sum_very_easy.add_two_numbers(-3,-1) == -4

def test_uncensor():
    assert uncensor_hard.uncensor("Wh*t's m* nam*", "aye") == "What's my name"




