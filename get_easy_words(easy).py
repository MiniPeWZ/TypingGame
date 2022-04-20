
# imports
import requests
import dotenv
import os
import random


# function block
def get_random_words() -> list:
    """
    Denne funksjonen sender en GET request til wordnik API for få en liste med tilfeldige ord
    :return: query of random words
    """
    # parametere for requesten
    dotenv.load_dotenv("C://EnvironmentalVariables//.env")
    parameters = {
        "api_key": os.environ.get("API_KEY"),
        "hasDictionaryDef": True,
        "minLength": 4,
        "maxLength": 8,
        "limit": 300,
    }

    # send en GET request
    response = requests.get("https://api.wordnik.com/v4/words.json/randomWords", params=parameters)
    response.raise_for_status()

    # returner dataen som en liste av ord
    data = [dictionary["word"] for dictionary in response.json()]
    return data


def write_data_to_easy_mode_txt(data: list) -> None:
    """
    Denn funksjonen tar dataen fra API-et of skriver det til easy_mode.txt
    :param data: liste av ord som må skrives til filen
    :return: None
    """
    # lag tilfeldige settninger med ordene
    sentences = [" ".join(random.sample(data, 7)) for i in range(30)]

    # skriv dem til easy_mode.txt
    with open("data/easy_mode.txt", "a", encoding="utf-8") as file:
        for sentence in sentences:
            file.write(f"{sentence}\n")


write_data_to_easy_mode_txt(get_random_words())
