def get_status(st):
    status = {
        '1': "Nowy",
        '2': "W trakcie",
        '3': "Do sprawdzenia",
        '4': "Zakończony",
    }
    return status[str(st)]
