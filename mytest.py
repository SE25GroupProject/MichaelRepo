import pytest
from myfile import analyze_array

class TestAnalyzeArray:
    def test_even_sum(self, capsys):
        array = [1, 2, 3, 3, 4, 3, 2, 1]
        total, average = analyze_array(array)
        captured = capsys.readouterr()
        assert total == 19
        assert average == 2.375
        assert "The sum is odd!" in captured.out
        assert "The average is greater than 2" in captured.out

    def test_odd_sum(self, capsys):
        array = [1, 1, 1, 1]
        total, average = analyze_array(array)
        captured = capsys.readouterr()
        assert total == 3
        assert average == 1.0
        assert "The sum is even!" in captured.out
        assert "The average is 2 or less" in captured.out