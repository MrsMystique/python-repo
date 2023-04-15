from Knowlege_base_python.Python_sintax.functions.fuel import convert, gauge
import pytest

def test_conv():
    assert convert("2/3") == 67
    """with pytest.raises(ZeroDivisionError):
        convert('1/0')
    with pytest.raises(ValueError):
        convert('1.5/2')
    with pytest.raises(ValueError):
        convert('3/2')
    with pytest.raises(ValueError):
        convert('cat')"""

def test_gauge():
    assert gauge(67) == '67%'
    assert gauge(99) == 'F'
    assert gauge(1) == 'E'