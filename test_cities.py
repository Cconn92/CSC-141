from city_functions import city_country

def test_city_country():
    result = city_country('santiago', 'chile')
    assert result == 'Santiago, Chile'

def test_city_country_population():
    result = city_country('santiago', 'chile', population=5000000)
    assert result == 'Santiago, Chile – population 5000000'
