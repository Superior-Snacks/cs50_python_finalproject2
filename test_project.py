from project import convert_weight, convert_volume, convert_currency, convert_length, convert_temperature, get_currency, decide

def test_convert_weight():
    assert convert_weight(1, "kg", "g") == 1000
    assert convert_weight(1, "mg", "yg") == 1.0000000000000001e+21
    assert convert_weight(1, "ton_uk", "kg") == 1016.0469088
    assert convert_weight(1, "ton_us", "kg") == 907.18474

def test_convert_volume():
    assert convert_volume(1, "l", "ml") == 1000
    assert convert_volume(1, "ml", "yl") == 1.0000000000000001e+21
    assert convert_volume(1, "gal_uk", "l") == 4.54609
    assert convert_volume(1, "gal_us", "l") == 3.78541

def test_convert_lenght():
    assert convert_length(1, "km", "m") == 1000
    assert convert_length(1, "m", "ym") == 1.0000000000000001e+24
    assert convert_length(1, "ft", "m") == 0.3048
    assert convert_length(1, "mi", "m") == 1609.344

def test_convert_temperature():
    assert convert_temperature(1, "C", "F") == 33.8
    assert convert_temperature(1, "f", "K") == 255.92777777777775
    assert convert_temperature(1, "k", "C") == -272.15
    assert convert_temperature(1, "f", "c") == -17.22222222222222

def test_convert_currency():
    assert convert_currency() ==
    assert convert_currency() ==
    assert convert_currency() ==
    assert convert_currency() ==

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