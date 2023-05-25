# Pobranie danych od użytkownika - zdanie
zdanie = input("Podaj zdanie: ")

# Pobranie danych od użytkownika - działanie arytmetyczne
dzialanie = input("Podaj działanie arytmetyczne: ")

# Wyciągnięcie unikatowych znaków alfanumerycznych
znaki_unikatowe = set(re.findall(r'\w', zdanie))

# Wyświetlenie unikatowych znaków po spacji
print("Unikatowe znaki alfanumeryczne:", ' '.join(znaki_unikatowe))

# Sklasyfikowanie podanego zdania
zdanie_rozne_litery = set(re.findall(r'\b[A-Z]\w*', zdanie))
ilosc_przecinkow = zdanie.count(',')
ilosc_kropek = zdanie.count('.')
skroty = set(re.findall(r'\b\w{1,3}\b', zdanie))

# Wyświetlenie sklasyfikowanych danych
print("Słowa rozpoczynające się dużą literą:", ', '.join(zdanie_rozne_litery))
print("Ilość użytych przecinków:", ilosc_przecinkow)
print("Ilość użytych kropek:", ilosc_kropek)
print("Skróty słowne:", ', '.join(skroty))

# Tworzenie zbiorów dla działania arytmetycznego
znaki_dzialania = set(re.findall(r'[-+*/]', dzialanie))
liczby_calkowite = set(re.findall(r'\d+', dzialanie))
liczby_zmiennoprzecinkowe = set(re.findall(r'\d+\.\d+', dzialanie))
ilosc_znakow_dzialania = len(znaki_dzialania)

# Wyświetlenie zbiorów dla działania arytmetycznego
print("Liczby całkowite:", ', '.join(liczby_calkowite))
print("Liczby zmiennoprzecinkowe:", ', '.join(liczby_zmiennoprzecinkowe))
print("Użyte znaki arytmetyczne:", ', '.join(znaki_dzialania))
print("Ilość znaków arytmetycznych:", ilosc_znakow_dzialania)
