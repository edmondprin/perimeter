import random
from perimeter import gen_question, calculate_expected, check_result, run_quiz

def test_gen_question():
    for _ in range(1000):
        n = random.randint(1, 50)
        mass_test = gen_question(n)
        assert len(mass_test) == n
        for _ in mass_test:
            assert 1 <= _ <= 20
            assert isinstance(_, int) 

def test_calculate_expected():
    expected_sum_3 = calculate_expected([2, 4, 5])
    assert expected_sum_3 == 11
    expected_sum_6 = calculate_expected([4, 12, 9, 3, 5, 9])
    assert expected_sum_6 == 42

def test_check_result():
    this_eval = check_result(3, 5)
    assert this_eval is False
    this_second_eval = check_result(10,10)
    assert isinstance(this_eval, bool) and isinstance(this_second_eval, bool)

def test_run_quiz():
    points, details = run_quiz(2, 3, lambda n:4)
    assert len(details) == 2
