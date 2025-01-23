import random
import time


# Funkcja minigry orzeł/reszka
def orzel_reszka():
    """Symuluje rzut monetą, zwraca 'Orzeł' lub 'Reszka'"""
    return random.choice(["Orzeł", "Reszka"])
    

def graj_do_trzech_rzutow():
    while True:  # Pętla powtarza grę w przypadku remisu
        print("Wybierz Orzeł lub Reszka:")
        wybor = input("Twój wybór (Orzeł/Reszka): ").strip().capitalize()

        if wybor not in ["Orzeł", "Reszka"]:
            print("Nieprawidłowy wybór! Spróbuj ponownie.")
            continue

        liczba_rzutow = 0
        wyniki = {"Orzeł": 0, "Reszka": 0}  # Liczymy ile razy wypadł Orzeł i Reszka

        print("Naciśnij Enter, aby rzucić monetą.")

        while liczba_rzutow < 3:
            input(f"\nRzut nr {liczba_rzutow + 1} - naciśnij Enter, aby wykonać rzut...")
            pokaz_kropki(3)
            wynik = orzel_reszka()  # Wykonaj rzut

            wyniki[wynik] += 1  # Zwiększ licznik dla wyniku rzutu
            liczba_rzutow += 1  # Zwiększ liczbę wykonanych rzutów
            print(f"Wynik rzutu: {wynik}")

        # Po 3 rzutach, pokazujemy wyniki
        print("\nKoniec gry! Ostateczne wyniki:")
        print(f"Orzeł: {wyniki['Orzeł']} razy")
        print(f"Reszka: {wyniki['Reszka']} razy")

        # Określamy zwycięzcę na podstawie liczby rzutów
        if wyniki["Orzeł"] > wyniki["Reszka"]:
            zwyciezca = "Orzeł"
        elif wyniki["Reszka"] > wyniki["Orzeł"]:
            zwyciezca = "Reszka"
        else:
            print("\nRemis! Gra się powtarza...\n")
            time.sleep(1)
            continue

        # Sprawdzamy, czy użytkownik wygrał
        if wybor == zwyciezca:
            print("\nGratulacje! Wygrałeś!")
            return "Win"
        else:
            print()
            return "Lost"

# Funkcja zadaj pytanie
def zadaj_pytanie(pytanie):
    odpowiedz = input(pytanie + " (tak/nie): ").strip().lower()
    while odpowiedz not in ["tak", "nie"]:  # Obsługuje błędne odpowiedzi
        print("Proszę odpowiedzieć 'tak' lub 'nie'.")
        time.sleep(0.3)  # Przerwa 0.3 sekundy
        odpowiedz = input(pytanie + " (tak/nie): ").strip().lower()
    return odpowiedz

#Kosmetic :>
def pokaz_kropki(n):
    for _ in range(n):  # Wyświetlimy 4 kropki
        print(".", end="", flush=True)  # Drukuje kropkę w tej samej linii
        time.sleep(0.4)  # Przerwa 0.3 sekundy

    print()  # Zakończenie linii po wypisaniu kropek
def napis_startowy():
    text1 = """
                   __          __ _  _          _                                             _        
                   \ \        / /(_)| |        (_)                                           | |       
                    \ \  /\  / /  _ | |_  __ _  _  __      __   __ _  _ __  ____ ___   _ __  | |_      
                     \ \/  \/ /  | || __|/ _` || | \ \ /\ / /  / _` || '__||_  // _ \ | '_ \ | __|     
                      \  /\  /   | || |_| (_| || |  \ V  V /  | (_| || |    / /|  __/ | |_) || |_  _   
                       \/  \/    |_| \__|\__,_||_|   \_/\_/    \__, ||_|   /___|\___| | .__/  \__|(_)  
                                              _/ |              __/ |                 | |              
                                             |__/              |___/                  |_| 
    """
    text2 = """
 _   _  ___  ____  _____  ___   ____   ___     _      _____  _______   __ ____  ___     _     __        __ _____ ___  _____  _____   _    
| | | ||_ _|/ ___||_   _|/ _ \ |  _ \ |_ _|   / \    |__  / |__  /\ \ / // ___||_ _|   / \    \ \      / /|__  /|_ _|| ____||_   _| / \   
| |_| | | | \___ \  | | | | | || |_) | | |   / _ \     / /    / /  \ V /| |     | |   / _ \    \ \ /\ / /   / /  | | |  _|    | |  / _ \  
|  _  | | |  ___) | | | | |_| ||  _ <  | |  / ___ \   / /_   / /_   | | | |___  | |  / ___ \    \ V  V /   / /_  | | | |___   | | / ___ \ 
|_| |_||___||____/  |_|  \___/ |_| \_\|___|/_/   \_\ /____| /____|  |_|  \____||___|/_/   \_\    \_/\_/   /____||___||_____|  |_|/_/   \_\   
    """

    
    print(text1)
    print(text2)
    print("-------------------------------------------------------------------------------------------------------------------------------------------")
    print("DOSTOSUJ OKNO KONSOLI TAK ABY NAPIS BYŁ CZYTELNY")
def napis_dead():
    text = """
 _   _  __  __  ___  _____  ____      _     ____   _____
| | | ||  \/  ||_ _|| ____||  _ \    / \   / ___| |__  /
| | | || |\/| | | | |  _|  | |_) |  / _ \  \___ \   / / 
| |_| || |  | | | | | |___ |  _ <  / ___ \  ___) | / /_ 
 \___/ |_|  |_||___||_____||_| \_\/_/   \_\|____/ /____|

                        _,.-----.,_
                      ,-~           ~-.
                    ,^___           ___^. 
                   /~"   ~"   .   "~   "~"
                  Y  ,--._    I    _.--.  Y
                  | Y     ~-. | ,-~     Y |
                  | |        }:{        | |
                 j l       / | \       ! l
               .-~  (__,.--" .^. "--.,__)  ~-.
              (           / / | \ \           )
               \.____,   ~  \/"\/  ~   .____,/
                ^.____                 ____.^
                   | |T ~\  !   !  /~ T| |
                   | |l   _ _ _ _ _   !| |
                   | l \/V V V V V V\/ j |
                   l  \ \|_|_|_|_|_|/ /  !
                    \  \[T T T T T TI/  /
                     \  `^-^-^-^-^-^'  /
                      \               /
                       \.           ,/
                         "^-.___,-^"
    """
    print(text)
def napis_koniec():
    text = """
 _  __  ___   _   _  ___  _____   ____ 
| |/ / / _ \ | \ | ||_ _|| ____| / ___|
| ' / | | | ||  \| | | | |  _|  | |             
| . \ | |_| || |\  | | | | |___ | |                  
|_|\_\ \___/ |_| \_||___||_____| \____|                                                             
                                                 
                                                
         Game By Bartosz FLY                                                                                                                                                                                                    
                        

    """
    print(text)
#Chapters
def dialog_1():
    print("> Nazywasz się Dawid Chucherko")
    time.sleep(0.3)  # Przerwa 0.3 sekundy
    print("> Zostawiła cię żona i wylądowałeś na ulicy bez grosza przy duszy")
    time.sleep(0.3)  # Przerwa 0.3 sekundy

    odpowiedz = zadaj_pytanie("Chcesz udowodnić sobie i światu że zostałeś niesprawiedliwie potraktowany")
    print("")

    if odpowiedz == "tak":
        print("> Pierwszym twoim zadaniem będzie znalezienie noclegu na ten dzień")
        time.sleep(0.3)  # Przerwa 0.3 sekundy
        
        odpowiedz2 = zadaj_pytanie("Do głowy przychodzi ci pobliski park czy chcesz się tam udać? ")
        print("")

        if odpowiedz2 == "tak":           
            print("> Idziesz do parku")
            time.sleep(0.3)
            pokaz_kropki(7)
            park()

        else:
            print("> Decydujesz się przejść swoją dzielnicą")  
            time.sleep(0.3)          
            pokaz_kropki(7)            
            motel()            

    else:
        print("> Decydujesz się wrócić w domu")
        print("")
        time.sleep(0.3)  # Przerwa 0.3 sekundy
        koniec() 

def park():
    print("> Nie wiesz czy chcesz zniżać się do poziomu spania w krzakach ale jedne wyglądają obiecująco")
    pokaz_kropki(7)
    print("")

    odpowiedz = zadaj_pytanie("Po drodze mijasz znajomego z czasów podstawówki, ubranego w garnitur i rozmawiającego przez telefon czy mimo  wszytsko chcesz go zaczepić?")
    if odpowiedz == "tak":
        print()
        print("> Przypominasz sobie że nazywa się Tomek")
        time.sleep(0.3)
        tomek()
    else:
            print("> Widzisz ławkę")
            time.sleep(0.3)  # Przerwa 0.3 sekundy 
            lawka()            

def lawka():
    print()
    odpowiedz = zadaj_pytanie("Czy decysujesz się teoche zdrzemnąć na ławce")
    if odpowiedz == "tak":
        print("> Zasypiasz na ławce")
        pokaz_kropki(5)
        time.sleep(0.3)
        print()
        print("> Po chwili budzisz się z zimna i widzisz ze pod ławką leży  moneta")
        time.sleep(0.3)
        print("> Postanawiasz zagrać z samym sobą i rzucić do 3")
        wynik = graj_do_trzech_rzutow()
        if wynik == "Win":
            print()
            print("> Nagle...")
            time.sleep(0.5)
            print("> Podchodzi do ciebie stary dobry znajomy Tomek i proponuje kawkę w swoim biurze")
            time.sleep(0.5)
            print("> Bez wielkiego wachania ufasz orłowi i podążasz za przyjacielem z dawnych lat")
            time.sleep(0.3)
            biuro()            
        elif wynik == "Lost":
            print()
            print("> Moneta spadła ci do kanałów i znika w czeluści mroku...")
            time.sleep(0.3)
            print("> Po chwili obierasz kierunek => motel")
            time.sleep(0.3)
            motel()
    else:
        print("> Po chwili obierasz kierunek => motel")
        motel() 

def tomek():
    print()
    print("> Tomek reaguje z optymizmem i rozłącza się mówiąc że zaraz oddzwoni")
    time.sleep(0.3)  # Przerwa 0.3 sekundy    
    odpowiedz2 = zadaj_pytanie ("Po dłuższej rozmowie, Tomek daje ci swoją wizytówkę i pyta czy przyjdziesz do niego do biura")
    if odpowiedz2 == "tak":
        print("> Idziesz z tomkiem do biura do biura")
        pokaz_kropki(6)
        time.sleep(0.3)
        print()
        biuro()     
        
    else:
        print("> Żegnacie się...")
        pokaz_kropki(5)
        time.sleep(0.3)
        motel()

def biuro():
        print("> Wchodzisz do biura")
        time.sleep(0.3)
        print("> Tomasz nalewa ci kawę i po chwili rozmowy pyta czy nie chcesz podjąć się u niego darmowego szkolenie w inwestowaniu")
        time.sleep(0.3)	
        odpowiedz = zadaj_pytanie("Wchodzisz w to?")

        if odpowiedz == "tak":
            print()
            print("> Mówi że przez pierwsze trzy miesiące będziesz mógł spać w biurze i dodaje że mężczyźni muszą sie wspierać")
            time.sleep(0.3)
            print("> Mija pierwszy miesiąc twojej pracy, Tomek widzi w tobie potencjał, świat bardzo szybko pokazał że życie jest sprawiedliwe i nigdy nie wiemy co nas spotka za rogiem")
            time.sleep(0.3)
            koniec()
        else:
            print ("> Nie zgodziłeś się na prace z tomkiem")
            time.sleep(0.3)
            print ("> Niemniej jednak Tomek nakłonił cię do zagrania w orła i reszkę żeby zdecydować czy podejmiesz się tego zadania")
            time.sleep(0.3)
            print("> Tomek pyta sie co obstawiasz")
            time.sleep(0.3)

            wynik = graj_do_trzech_rzutow()  # Wywołanie gry orzeł/reszka

            if wynik == "Win":
                print("> Wypadł Orzeł! Podejmujesz się zadania!")
                time.sleep(0.3)
                print("> Mówi że przez pierwsze trzy miesiące będziesz mógł spać w biurze i dodaje że mężczyźni muszą sie wspierać")
                time.sleep(0.3)
                print("> Mija pierwszy miesiąc twojej pracy, Tomek widzi w tobie potencjał, świat bardzo szybko pokazał że życie jest sprawiedliwe i nigdy nie wiemy co nas spotka za rogiem")
                time.sleep(0.3)
                koniec()
            elif wynik == "Lost":
                print("> Wypadła Reszka! Nie podejmujesz się zadania.")
                time.sleep(0.3)
                print("> Pogawędka chwile trwa i decydujesz się opóścić biuro")
                time.sleep(0.3)
                motel()

def motel():
        print()
        print("> Podczas spaceru środkiem swojej miejscowośći widzisz Motel, myślisz sobie:")
        time.sleep(0.3)	
        print("> Dziś rano sie myłem i wyglądam wmiare zadbanie może trzeba spytać na recepcji czy nie potrzebują pomocy w zamian za jednodniowy nocleg...")
        time.sleep(0.3)
        pokaz_kropki(6)
        print()
        time.sleep(0.3)
        print("> Docierasz do motelu")
        odpowiedz = zadaj_pytanie ("Wchodzisz do niego?")
        if odpowiedz == "tak":
            print()
            print("> Przy recepcji zauważasz kobietę w twoim wieku, która naturalnie się do ciebie uśmiecha lecz jest brzydka")
            time.sleep(0.3)
            print("> Pytasz ją czy możesz jakoś pomóc?")
            time.sleep(0.3)
            pani_ania()            
        else:
            print()
            print ("> Kierujesz się na wysypisko śmieci")
            time.sleep(0.3)
            pokaz_kropki(6)
            wysypisko()                  

def pani_ania():

    odpowiedz = zadaj_pytanie("Przedstawia się jako Ania i odpowiada pytaniem czy umiesz naprawić zmywarkę")
    if odpowiedz == "tak":
        print()
        time.sleep(0.3)
        print("> Naprawiasz zmywarkę poczym kobieta oferuje ci pokój na jedną noc i romantyczną kolacje za darmo")            
        odpowiedz = zadaj_pytanie("Próbujesz szczęścia i korzystasz z kolacji?")
        if odpowiedz == "tak":
            print()
            randka()
        else:
            print()
            time.sleep(0.3)
            print("> Spisz jedną noc w motelu")
            time.sleep(0.3)
            pokaz_kropki(6)
            print("")
            print("> Budzisz się...") 
            time.sleep(0.5)
            print("> Po chwili decydujesz się pójść na wysypisko śmieci")
            time.sleep(0.5)
            print("> Wychodzisz z Motelu i idziesz na wysypisko")
            pokaz_kropki(6)
            wysypisko()             
            
    else:
        print("> Masz niesamowitego lenia a Pani Ania wygląda obrzydliwie i zaczyna gadać że śmierdzisz")
        time.sleep(0.3)
        print("> Pani Ania proponuje żebyś chociaż wyrzucił śmieci")
        time.sleep(0.3)
        print("")
        time.sleep(0.3)
        print("> wychodzisz z motelu i idziesz dalej w strone motelowego składowiska odpadów")        
        pokaz_kropki(3)
        time.sleep(1)
        print()
        wyrzucanie_smieci() 

def wyrzucanie_smieci():
    print()
    print("> Wyrzucasz tam śmieci od pani Ani")
    time.sleep(0.3)
    odpowiedz = zadaj_pytanie("Patrzysz na śmierdzący śmietnik i zadajesz sobie pytanie czy śpisz tutaj")
    if odpowiedz == "tak":
        print("> Śpisz w śmietniku")
        pokaz_kropki(6)        
        print()
        print("> Rano decydujesz się ruszyć na wypisko śmieci")
        time.sleep(0.3)
        print("> Była to pierwsza myśl która przyszła do głowy po nocy spędzonej na śmieciach motelu")
        pokaz_kropki(3)
        wysypisko()
    else:
        print()
        print("> Nie może być z tobą aż tak źle... probujesz zadecydować monetą czy wracasz do hotelu bajerować Anię czy szukasz innych alternatyw")
        print("> Jeśli wygrasz lecisz w bajere")
        wynik = graj_do_trzech_rzutow()
        if wynik == "Win":
            print("> Decydujesz się bajerować Anię")
            time.sleep(0.3)
            print("> Wracasz do motelu i gadka się wam klei......")
            time.sleep(0.3)
            print()
            time.sleep(0.3)
            print("> Po chwili...")  
            time.sleep(0.3)          
            randka()
        elif wynik == "Lost":
            print("> Spluwasz na sterte śmieci motelowych i ruszasz w dalszą podróż")
            time.sleep(0.3) 
            pokaz_kropki(5)           
            wysypisko()

def randka():

    print("> Decydujesz się na randkę z panią Anią")
    time.sleep(0.3)
    print("> Okazało się że się macie ze sobą wiele wspólnego")
    time.sleep(0.3)
    odpowiedz = zadaj_pytanie("Pani Ania proponuje ci zatrudnienie u siebie na kasie w swoim motelu. Zgadzasz sie?")
    time.sleep(0.3)
    if odpowiedz == "tak":
        print()
        print("> Ochoczo podejmujesz się roboty rozwijając swoją relację z panią Anią")
        time.sleep(0.3)
        print("> Zyjecie długo i szczęśliwie")
        time.sleep(0.3)        
        koniec()
        #KONIEC
    else:
        print()
        print("> Odmawiasz pani Ani")
        time.sleep(0.3)
        print("> Pani Ania czuję się urażona")
        time.sleep(0.3)
        print("> Ozięble cie rzegna i zostawia na ulicy")
        time.sleep(0.3)
        print("> Z bezradności idziesz dalej szukać szczęścia")
        time.sleep(0.3)
        pokaz_kropki(6)
        wysypisko()

def wysypisko():    
    print()
    print ("> Docierasz na wysypisko śmieci") 
    time.sleep(0.3)
    print("> Na wysypisku spotykasz Zdzicha")
    time.sleep(0.3)
    print("> Zaczynasz z nim rozmawiać")
    time.sleep(0.3)
    pokaz_kropki(3)
    print("> Po chwili rozmowy Zdzichu okazuje sie kompletnym imbecylem i zaczyna cie irytować")
    time.sleep(0.3)
    print("> Przez to że Zdzichu nie jest jakiś super bystry dostrzegasz możliwość zaproponowania mu układu żeby troche u niego zarobić")
    time.sleep(0.3)
    print("> Proponujesz gre w Orła i reszkę do 3 wygranych")
    time.sleep(0.3)
    print("> Jeśli ty wygrasz to możesz pracować ze zdzichem w przeciwnym razie nie dostajesz pracy")
    time.sleep(0.3)
    print("> Zdzichu zgadza się na ten układ")
    time.sleep(0.3)
    print("> ")
    time.sleep(0.3)
    print()

    wynik = graj_do_trzech_rzutow()
    if wynik == "Win":
            print()
            print("> Wygrałeś z kierownikiem wysypiska")
            time.sleep(0.5)
            print("> Irytujący Zdzichu tłumaczy ci jak wygląda twoja praca czyli spalanie śmieci")
            time.sleep(0.5)
            print("> Słuchasz zdzicha i wiesz ze zarobisz przynajmniej na nocleg w hotelu")
            koniec()
            #Koniec
                        
    elif wynik == "Lost":
            print()
            print("> Moneta niestety nie pozwoliła tobie wygrać")
            time.sleep(0.3)
            print("> Zdzichu napawa się wygraną i określa ciebie jako nieudacznika")
            time.sleep(0.3)
            print("> Kończysz tę niezręczną rozmowę i idziesz spać do pobliskiego kontenera znajdującego się na wysypisku śmieci")
            time.sleep(0.3)
            print("> Ponosisz śmierć gdyż kontener w nocy został zutylizowany")
            time.sleep(0.3)
            napis_dead()
            pokaz_kropki(10)
            time.sleep(0.3)
            print()
            print("> Okazuje się że to tylko zły sen...")
            dialog_1()            

def koniec():
    napis_koniec()
    odpowiedz = zadaj_pytanie("> Czy chcesz zagrać ponownie?")
    if odpowiedz == "tak":
        print()
        main()
    else:
        print("Dziękuję za gre!")

# Funkcja główna
def main():
    napis_startowy()
    time.sleep(0.3)  # Przerwa 0.3 sekundy
    print("Podczas rozgrywki posługuj się komendami tak lub nie")
    time.sleep(0.3)  # Przerwa 0.3 sekundy    
    # Zadaj pytanie i zbierz odpowiedź
    odpowiedz = zadaj_pytanie("Czy chcesz zacząć swoją podróż?")
    print("")

    # Obsługuje odpowiedź gracza
    if odpowiedz == "tak":
        print("Zaczynasz swoją podróż!")
        print("")
        time.sleep(0.3)  # Przerwa 0.3 sekundy
        dialog_1()
    else:
        print("Decydujesz się zostać w domu. Koniec gry.")        
        time.sleep(5)  # Przerwa 0.3 sekundy

if __name__ == "__main__":
    main()
