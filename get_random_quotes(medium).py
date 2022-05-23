

# imports
import requests


def get_random_quotes() -> list:
    """
    Denne funksjonen bruker requests modulen for å hente en tilfeldig quote fra API
    :return: json, som inneholder alle quotes
    """
    # parametere for request
    parameters={
        "page": 1,
        "limit": 150
    }

    # gjør en GET request

    response = requests.get(url="https://api.quotable.io/quotes", params=parameters)
    response.raise_for_status()

    # returner data
    data = [quote["content"] for quote in response.json()["results"]]
    return data


def write_data_to_medium_mode_txt(data: list) -> None:
    """
    Denne funksjonen tar dataen fra API-et of skriver det til medium_mode.txt
    :param data: tilfeldige quotes fra API kallet
    """
    # åpne filen for å skrive data i den
    with open("data/medium_mode.txt", "a", encoding="utf-8") as file:
        for quote in data:
            file.write(f"{quote}\n")
