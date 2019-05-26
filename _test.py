import pytest
import main

data = main.DataProcessing()


# Testing output from first task
def test_Average(capsys):
    data.AverageVoivo("Pomorskie", 2010)
    captured = capsys.readouterr()
    assert captured.out == "2010 - 20963\n"

    data.AverageVoivo("Lubelskie", 2012)
    captured = capsys.readouterr()
    assert captured.out == "2012 - 22626\n"


# Testing output from second task
def test_PassRate(capsys):
    data.PercentPassInVoivo("Pomorskie")
    captured = capsys.readouterr()
    assert captured.out == "2010 - 81 %\n2011 - 74 %\n2012 - 80 %\n2013 - 80 %\n2014 - 71 %\n2015 - 73 %\n2016 - 79 %\n2017 - 78 %\n2018 - 77 %\n"

    data.PercentPassInVoivo("Lubuskie")
    captured = capsys.readouterr()
    assert captured.out == "2010 - 82 %\n2011 - 76 %\n2012 - 82 %\n2013 - 83 %\n2014 - 73 %\n2015 - 75 %\n2016 - 81 %\n2017 - 79 %\n2018 - 79 %\n"


# Testing output from third task
def test_BestVoivo(capsys):
    data.MostPassInYear(2012)
    captured = capsys.readouterr()
    assert captured.out == "2012 - województwo Małopolskie\n"

    data.MostPassInYear(2010)
    captured = capsys.readouterr()
    assert captured.out == "2010 - województwo Kujawsko-pomorskie\n"


# Testing output from fourth task
def test_Regression(capsys):
    data.DetectRegression()
    captured = capsys.readouterr()
    assert captured.out == "województwo Dolnośląskie: 2010 -> 2011\nwojewództwo Kujawsko-pomorskie: 2010 -> 2011\nwojewództwo Lubelskie: 2010 -> 2011\nwojewództwo Lubuskie: 2010 -> 2011" \
                           "\nwojewództwo Łódzkie: 2010 -> 2011\nwojewództwo Małopolskie: 2010 -> 2011\nwojewództwo Mazowieckie: 2010 -> 2011\n" \
                           "województwo Opolskie: 2010 -> 2011\nwojewództwo Podkarpackie: 2010 -> 2011\nwojewództwo Podlaskie: 2010 -> 2011\n" \
                           "województwo Pomorskie: 2010 -> 2011\nwojewództwo Śląskie: 2010 -> 2011\nwojewództwo Świętokrzyskie: 2010 -> 2011\n" \
                           "województwo Warmińsko-Mazurskie: 2010 -> 2011\nwojewództwo Wielkopolskie: 2010 -> 2011\nwojewództwo Zachodniopomorskie: 2010 -> 2011\n" \
                           "województwo Dolnośląskie: 2013 -> 2014\nwojewództwo Kujawsko-pomorskie: 2013 -> 2014\nwojewództwo Lubelskie: 2013 -> 2014\n" \
                           "województwo Lubuskie: 2013 -> 2014\nwojewództwo Łódzkie: 2013 -> 2014\nwojewództwo Małopolskie: 2013 -> 2014\n" \
                           "województwo Mazowieckie: 2013 -> 2014\nwojewództwo Opolskie: 2013 -> 2014\nwojewództwo Podkarpackie: 2013 -> 2014\n" \
                           "województwo Podlaskie: 2013 -> 2014\nwojewództwo Pomorskie: 2013 -> 2014\nwojewództwo Śląskie: 2013 -> 2014\n" \
                           "województwo Świętokrzyskie: 2013 -> 2014\nwojewództwo Warmińsko-Mazurskie: 2013 -> 2014\nwojewództwo Wielkopolskie: 2013 -> 2014\n" \
                           "województwo Zachodniopomorskie: 2013 -> 2014\nwojewództwo Dolnośląskie: 2016 -> 2017\nwojewództwo Kujawsko-pomorskie: 2016 -> 2017\n" \
                           "województwo Lubelskie: 2016 -> 2017\nwojewództwo Lubuskie: 2016 -> 2017\nwojewództwo Łódzkie: 2016 -> 2017\n" \
                           "województwo Mazowieckie: 2016 -> 2017\nwojewództwo Opolskie: 2016 -> 2017\nwojewództwo Podkarpackie: 2016 -> 2017\nwojewództwo Podlaskie: 2016 -> 2017\n" \
                           "województwo Pomorskie: 2016 -> 2017\nwojewództwo Śląskie: 2016 -> 2017\nwojewództwo Świętokrzyskie: 2016 -> 2017\n" \
                           "województwo Warmińsko-Mazurskie: 2016 -> 2017\nwojewództwo Wielkopolskie: 2016 -> 2017\nwojewództwo Zachodniopomorskie: 2016 -> 2017\n" \
                           "województwo Lubuskie: 2017 -> 2018\nwojewództwo Łódzkie: 2017 -> 2018\nwojewództwo Pomorskie: 2017 -> 2018\n"


# Testing output from fifth task
def test_Comparision(capsys):
    data.CompareVoivos("Pomorskie", "Lubuskie")
    captured = capsys.readouterr()
    assert captured.out == "2010 - Lubuskie\n2011 - Lubuskie\n2012 - Lubuskie\n2013 - Lubuskie\n2014 - Lubuskie\n2015 - " \
                           "Lubuskie\n2016 - Lubuskie\n2017 - Lubuskie\n2018 - Lubuskie\n"
