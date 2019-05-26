# Przed pierwszym uruchomieniem 

Aby zainstalować wszystkie wymagane dependecje wystarczy po sklonowaniu wpisać w konsole:

```
pip install -r requirements.txt
```

# Korzystanie z funkcji

W celu obliczenia średniej liczby osób które przystąpiły do egzaminu dla danego województwa i roku należy wywołać program z parametrami:

```
python main.py -srednia [wojewodztwo] [rok]
```

Dla procentowej zdawalności dla danego województwa na przestrzeni lat:

```
python main.py -zdawalnosc [wojewodztwo]
```

W celu wyświetlenia województwa które miało najlepszą zdawalność w konkretnym roku:

```
python main.py -najlepsze [rok]
```

W celu wyświetlenia ogólnej regresji zdawalności:
```
python main.py -regresja
```
W celu porównania zdawalności w dwóch podanych wojewodztwach:
```
python main.py -porownaj [wojewodztwo 1] [wojewodztwo 2]
```
