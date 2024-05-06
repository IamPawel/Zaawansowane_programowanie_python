# plik odpowiedzialny za zapisywanie do pliku pracy do wykonania.
import time


def get_next_id(filename):
    with open(filename, "r") as file:
        lines = file.readlines()
    ids = []
    # Iteracja przez linie tekstu
    for line in lines:
        # Szukanie początku numeru ID
        id_start = 0
        # Szukanie końca numeru ID (znajdowanie pierwszego znaku, który nie jest cyfrą)
        id_end = id_start
        while id_end < len(line) and line[id_end].isdigit():
            id_end += 1
        # Wyciągnięcie numeru ID z linii i dodanie do listy
        if id_end > id_start:
            ids.append(int(line[id_start:id_end]))
    if len(ids) == 0:
        return 1
    else:
        next_id = max(ids) + 1
        return next_id


def produce(filename):
    next_id = get_next_id(filename)
    with open(filename, "a") as file:
        file.write(f"{next_id};{time.time()};pending\n")


if __name__ == "__main__":
    produce("zadania.txt")
