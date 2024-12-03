from main import get_input

def total_count_tester_A():
    actual_result = get_input()
    assert actual_result[0] == 3
    print('A test pass')

def total_count_tester_G():
    actual_result = get_input()
    assert actual_result[1] == 9
    print('G test pass')

def total_count_tester_C():
    actual_result = get_input()
    assert actual_result[2] == 7
    print('C test pass')

def total_count_tester_T():
    actual_result = get_input()
    assert actual_result[3] == 11
    print('T test pass')

def total_count_tester_X():
    actual_result = get_input()
    assert actual_result[4] == 7
    print('Unknowns test pass')

total_count_tester_A()
total_count_tester_G()
total_count_tester_C()
total_count_tester_T()
total_count_tester_X()