from main import square_the_number, cube_the_number

def test_square_pass():
    assert square_the_number(10) == 100

def test_cube_fail():
    assert cube_the_number(10) == 1000