import pytest
from list_utils import find_one, find_n,find_streak, first_elements, transpose, displace

def test_find_one():
    needle = 1
    none = [0, 0, 5, 's']
    beginning = [1,None, 9, 6 , 0, 0]
    end = ['x', '0', 1]
    several = [0, 0, 3, 4, 1, 3, 2, 1, 3, 4]

    assert find_one(none, needle) == False
    assert find_one(beginning, needle)
    assert find_one(end, needle)
    assert find_one(several, needle) 


def test_find_n():

    assert find_n([2, 3, 4, 5, 6], 2, -1) == False
    assert find_n([1, 2, 3, 4,5], 42, 2) == False
    assert find_n([1, 2, 3, 4, 5], 1, 2) == False
    assert find_n([1, 2, 3, 2, 4, 5], 2, 2) == True
    assert find_n([1, 2, 3, 4, 5, 4, 6, 4, 7, 4, 6], 4, 2) == True   
    assert find_n([1,2,3,4], "x", 0) == True

def test_find_streak():
    assert find_streak([1, 2, 3, 4, 5], 4, -1) == False
    assert find_streak([1, 2, 3, 4, 5], 42, 2) == False
    assert find_streak([1, 2, 3, 4], 4, 1) == True
    assert find_streak([1, 2, 3, 1, 2], 2, 2) == False
    assert find_streak([1, 2, 3, 4, 5, 5, 5], 5, 3) == True
    assert find_streak([5, 5, 5, 1, 2, 3, 4], 5, 3) == True
    assert find_streak([1, 2, 5, 5, 5, 3, 4], 5, 3) == True
    assert find_streak([1, 2, 3, 4, 5, 5, 5], 5, 4) == False

def test_first_elements():
    original = [[0,7,3], [4,0,1]]
    lista_vacia = [[],[]]
    lol2 = [[0,7,3], [4,0,1], [5,6,7], [7,8,9]]

    assert first_elements(original) == [0,4]  
    assert first_elements(lista_vacia) == []
    assert first_elements(lol2) == [0,4,5,7]  

def test_transpose():
    lol2 = [[0,7,3,1], [4,0,1,2], [5,6,7,3], [7,8,9,6]]
    original = [[0,7,3], [4,0,1]]
    


    assert transpose(lol2) == [[0,4,5,7], [7,0,6,8], [3,1,7,9], [1,2,3,6]]
    assert transpose(original) == [[0,4], [7,0], [3,1]]
    assert transpose(transpose(original)) == original

def test_zero_distance_displace():
    l1 = [1, 2, 3, 4, 5, 6]
    l2 = [1]
    l3 = [[4, 5], ['x', 'o', 'c']]

    assert displace([], 0) == []
    assert displace(l1, 0) == l1
    assert displace(l2, 0) == l2
    assert displace(l3, 0) == l3

def test_positive_distance_displace():

    l1 = [1, 2, 3, 4, 5, 6]
    l2 = [1]
    l3 = [[4, 5], ['x', 'o', 'c']]
    l4 = [9, 6, 5]

    assert displace([], 2) == []
    assert displace(l1, 2) == [None, None, 1, 2, 3, 4]
    assert displace(l2, 3, '-') == ['-']
    assert displace(l3, 1, '#') == ['#', [4, 5]]
    assert displace(l4, 3, 0) == [0, 0, 0]

def test_negative_distance_displace():
    l1 = [1, 2, 3, 4, 5, 6]
    l2 = [1]
    l3 = [[4, 5], ['x', 'o', 'c']]
    l4 = [9, 6, 5]

    assert displace([], -2) == []
    assert displace(l1, -2) == [3, 4, 5, 6, None, None]
    assert displace(l2, -3, '-') == ['-']
    assert displace(l3, -1, '#') == [['x', 'o', 'c'], '#']
    assert displace(l4, -3, 0) == [0, 0, 0]

