from project import convert_weight, convert_volume, convert_currency, convert_length, convert_temperature, get_currency, decide

def test_convert_weight():
    assert convert_weight(1, "kg", "g") == 1000
    assert convert_weight(1, "mg", "yg") == 1.0000000000000001e+21
    assert convert_weight(1, "ton_uk", "kg") == 1016.0469088
    assert convert_weight(1, "ton_us", "kg") == 907.18474

def test_convert_volume():
    assert convert_volume() ==
    assert convert_volume() ==
    assert convert_volume() ==
    assert convert_volume() ==

def test_convert_currency():
    assert convert_currency() ==
    assert convert_currency() ==
    assert convert_currency() ==
    assert convert_currency() ==

def test_convert_lenght():
    assert convert_length() ==
    assert convert_length() ==
    assert convert_length() ==
    assert convert_length() ==

def test_convert_temperature():
    assert convert_temperature() ==
    assert convert_temperature() ==
    assert convert_temperature() ==
    assert convert_temperature() ==

def test_get_currency():
    assert get_currency() ==
    assert get_currency() ==
    assert get_currency() ==
    assert get_currency() ==

def test_decide():
    assert decide() ==
    assert decide() ==
    assert decide() ==
    assert decide() ==