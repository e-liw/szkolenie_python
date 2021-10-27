if __name__ == "__main__":
    import pyfiglet
    from calculator import calc
    baner = pyfiglet.figlet_format("K a l k u l a t o r")
    print(baner)
    print('''
            Dostępne działania :
            + dodawanie
            - odejmowanie
            * mnozenie
            / dzielenie
            ** potegownie
            ''')
    input('Wybierz działanie:')
