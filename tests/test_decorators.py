

from src.decorators import log


# def test_log(capsys):
#     @log(filename="mylog.txt")
#     def my_function(x, y):
#         return x + y
#
#     my_function(1, 2)
#     captured = capsys.readouterr()
#     assert "my_function called with args: (1, 2), kwargs:{}. Result: 3\n" in captured.out
#
#     try:
#         my_function(0, 4)
#     except TypeError:
#         captured = capsys.readouterr()
#         assert "my function error: " in captured.out


def test_log(capsys):
    @log()
    def my_function(x, y):
        return x + y

    my_function(1, 2)
    captured = capsys.readouterr()
    assert "my_function called with args: (1, 2), kwargs:{}. Result: 3\n" in captured.out

    @log()
    def my_function_with_error(x, y):
        raise ValueError("Test error")

    try:
        my_function_with_error(0, 4)
    except ValueError:
        captured = capsys.readouterr()
        assert "my_function_with_error error: Test error. Inputs:(0, 4), {}\n" in captured.out
