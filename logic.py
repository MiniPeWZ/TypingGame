# imports
from tkinter import *
from tkinter import ttk
from tkinter.font import Font
import time
import random


# class block
class TypingTest(Tk):

    def __init__(self):
        """Initialiser applikasjonen"""
        super().__init__()

        # easy window init
        self.easy_window = None
        self.easy_mainframe = None
        self.easy_text_entry = None
        self.easy_rules_label = None
        self.easy_sentence_label = None
        self.easy_label_style = None

        # medium window init
        self.medium_window = None
        self.medium_mainframe = None
        self.medium_text_entry = None
        self.medium_sentence_label = None
        self.medium_rules_label = None
        self.medium_label_style = None

        # resultat variabler
        self.start_time =0
        self.total_time =0
        self.accuracy = 0
        self.wpm = 0

        # root konfigurasjon
        self.title("GorillaType")
        self.resizable(width=True, height=True)
        self.iconbitmap("assets/icons/icon.ico")

        # styles for programmet

        font_for_the_buttons = Font(family="Arial", size=14)
        self.button_style = ttk.Style()
        self.button_style.theme_use("default")
        self.button_style.configure("FountainBlueButton.TButton",
        background="#686868",
        foreground="#FFC300",
        font=font_for_the_buttons,
        width=15,
        borderwidth=1,
        focusthickness=3)

        self.frame_style=ttk.Style()
        self.frame_style.configure("BlueFrame.TFrame", background="#313131")

        self.label_style=ttk.Style()
        self.label_style.configure("DarkLabel.TLabel", background="#313131", foreground="#FFC300")

        # global frame for app
        self.global_frame = ttk.Frame(self, style="BlueFrame.TFrame")
        self.global_frame.grid(column=0, row=0)


        # etiketter

        font_for_the_title_label = Font(family="Arial", size=30, weight="bold")
        self.title_label = ttk.Label(self.global_frame,
                                     text="GorillaType", font=font_for_the_title_label, style="DarkLabel.TLabel")
        self.title_label.grid(column=1, row=0, padx=10, pady=10)

        font_for_the_diff_label = Font(family="Arial", size=18)
        self.diff_label = ttk.Label(self.global_frame,
                                    text="Choose Difficulty:", font=font_for_the_diff_label, style="DarkLabel.TLabel")
        self.diff_label.grid(column=1, row=2, padx=30, pady=30)

        # knapper
        self.easy_button=ttk.Button(self.global_frame, text="Easy", padding=10, style="FountainBlueButton.TButton",
                                      command=self.easy)
        self.easy_button.grid(column=0, row=3, padx=10, pady=10)

        self.medium_button = ttk.Button(self.global_frame, text="Medium"
                                                                "(Quotes)", padding=10,
                                        style="FountainBlueButton.TButton",
                                        command=self.medium)
        self.medium_button.grid(column=2, row=3, padx=10, pady=10)

        #mainloop
        self.mainloop()

    def easy(self):
        """
        Denne metoden implementerer easy mode for Typing Test Appen.
        ??pner i nytt Tkinter vindu.
        """
        # index variabel for identifying the window
        index = 0

        # hide the main window, till the TopLevel is not closed
        self.iconify()
        self.easy_button.configure(state=DISABLED)
        self.medium_button.configure(state=DISABLED)

        # Lag et nytt vindu hvor easy mode vises.
        self.easy_window = Toplevel()
        self.easy_window.title("Easy Mode")
        self.easy_window.resizable(width=True, height=True)
        self.easy_window.iconbitmap("assets/icons/icon.ico")

        #styles
        font_for_the_buttons=Font(family="Arial", size=14, weight="bold")
        buttons_style = ttk.Style()
        buttons_style.theme_use("default")
        buttons_style.configure("Buttons.TButton",
                                background="#686868",
                                foreground="#FFC300",
                                font=font_for_the_buttons,
                                width=10,
                                borderwidth=1,
                                focusthickness=3, )

        mainframe_style=ttk.Style()
        mainframe_style.configure("MainFrame.TFrame", background="#313131")

        self.easy_label_style = ttk.Style()
        self.easy_label_style.configure("Labels.TLabel", background="#313131", foreground="#FFC300", font=("Arial", 14))

        # Lag en main frame for viduet

        self.easy_mainframe = ttk.Frame(self.easy_window, style="MainFrame.TFrame")
        self.easy_mainframe.grid(column=0, row=0)

        # knapper
        start_button=ttk.Button(self.easy_mainframe, text="Start", padding=1, command=lambda: self.main(index),
                                  style="Buttons.TButton")
        start_button.grid(column=0, row=3, padx=10, pady=10)

        exit_button=ttk.Button(self.easy_mainframe, text="Exit", padding=1, command=lambda: self.close_window(index),
                                 style="Buttons.TButton")
        exit_button.grid(column=1, row=3, padx=10, pady=10)

        # entries
        font_for_the_entry=Font(family="Arial", size=14)
        self.easy_text_entry=ttk.Entry(self.easy_mainframe, width=60, font=font_for_the_entry)
        self.easy_text_entry.grid(column=0, row=1, padx=20, pady=20, columnspan=2)

        # etiketter
        self.easy_rules_label = ttk.Label(self.easy_mainframe,
                                          text="Press Start to Begin the Test. Press Enter to Complete It.",
                                          style="Labels.TLabel")
        self.easy_rules_label.grid(column=0, row=2, padx=10, pady=10, columnspan=2)

        self.easy_sentence_label = ttk.Label(self.easy_mainframe, text="GorillaType",
                                             style="Labels.TLabel")
        self.easy_sentence_label.grid(column=0, row=0, padx=10, pady=20, columnspan=2)

    def medium(self):
        """
        Dette implementerer medium mode som ??pnes i et nytt tkinter vindu.

        """
        # index variable for identifying the window


        index= 1

        # hide the main window, till the TopLevel is not closed
        self.iconify()
        self.easy_button.configure(state=DISABLED)
        self.medium_button.configure(state=DISABLED)

        # Lag et nytt vindu hvor medium mode vises.
        self.medium_window = Toplevel()
        self.medium_window.title("Medium Mode")
        self.medium_window.resizable(width=True, height=True)
        self.medium_window.iconbitmap("assets/icons/icon.ico")

        # styles
        font_for_the_buttons = Font(family="Arial", size=14, weight="bold")
        buttons_style = ttk.Style()
        buttons_style.theme_use("default")
        buttons_style.configure("Buttons.TButton",
        background="#686868",
        foreground="#FFC300",
        font=font_for_the_buttons,
        width=10,
        borderwidth=1,
        focusthickness=3, )

        mainframe_style =ttk.Style()
        mainframe_style.configure("MainFrame.TFrame", background="#313131")

        self.medium_label_style=ttk.Style()
        self.medium_label_style.configure("Labels.TLabel", background="#313131", foreground="#FFC300",
                                          font=("Arial", 14))

        # Lag main frame til vindu
        self.medium_mainframe = ttk.Frame(self.medium_window, style="MainFrame.TFrame")
        self.medium_mainframe.grid(column=0, row=0)

        # knapper
        start_button = ttk.Button(self.medium_mainframe, text="Start", padding=1,
                                  command=lambda: self.main(index),
                                  style="Buttons.TButton")
        start_button.grid(column=0, row=3, padx=10, pady=10)

        exit_button = ttk.Button(self.medium_mainframe, text="Exit", padding=1,
     command=lambda: self.close_window(index),
     style="Buttons.TButton")
        exit_button.grid(column=1, row=3, padx=10, pady=10)

        # entries
        font_for_the_entry = Font(family="Arial", size=14)
        self.medium_text_entry=ttk.Entry(self.medium_mainframe, width=60, font=font_for_the_entry)
        self.medium_text_entry.grid(column=0, row=1, padx=20, pady=20, columnspan=2)

        #etiketter
        self.medium_rules_label = ttk.Label(self.medium_mainframe,
                                            text="Press Start to Begin the Test. Press Enter to Complete It.",
                                            style="Labels.TLabel")
        self.medium_rules_label.grid(column=0, row=2, padx=10, pady=10, columnspan=2)

        self.medium_sentence_label = ttk.Label(self.medium_mainframe, text="GorillaType",
                                               style="Labels.TLabel")
        self.medium_sentence_label.grid(column=0, row=0, padx=10, pady=20, columnspan=2)

    def main(self, index):
        """
        Main funksjon til Typing appen.
        """
        #Sjekk index, for ?? avgjo??re hvilken test som skal startes
        if index == 0:
            # t??m text entry
            self.easy_text_entry.delete(0, END)

            # Hent en tilfeldig settning fra/easy_mode.txt
            with open("data/easy_mode.txt", "r", encoding="utf-8") as hard_file:
                # les file
                sentences = hard_file.read().split("\n")

                # Hent en tilfeldig settning
                random_sentence = random.choice(sentences)

            # start timeren


            self.start_time = time.time()

            # display settningen p?? label
            self.easy_sentence_label.grid_forget()
            self.easy_sentence_label = ttk.Label(self.easy_mainframe, text=random_sentence, style="Labels.TLabel")
            self.easy_sentence_label.grid(column=0, row=0, padx=10, pady=20, columnspan=2)

            # check if the Enter key was pressed, if it was than we need to calculate the results
            self.easy_window.bind("<Return>",
      lambda event, sentence=random_sentence, id_index=index: self.display_results(event,
                                                                                   sentence,
                                                                                   index))
        elif index == 1:
            #t??m text entry
            self.medium_text_entry.delete(0, END)

            # hent random settning fra data/medium_mode.txt
            with open("data/medium_mode.txt", "r", encoding="utf-8") as medium_file:
                # read filen
                sentences =medium_file.read().split("\n")

                # hent en random settning
                random_sentence = random.choice(sentences)

            # start timeren
            self.start_time = time.time()

            # display settningen p?? label
            self.medium_sentence_label.grid_forget()
            self.medium_sentence_label = ttk.Label(self.medium_mainframe, text=random_sentence, style="Labels.TLabel")
            self.medium_sentence_label.grid(column=0, row=0, padx=10, pady=20, columnspan=2)

            # sjekk om Enter key ble trykket, hvis den ble kalkuler resultatet.
            self.medium_window.bind("<Return>",
                        lambda event, sentence=random_sentence, id_index=index: self.display_results(event,
                                                                                                     sentence,
                                                                                                     index))

            # Hent random settning fra/easy_mode.txt
            with open("data/hard_mode.txt", "r", encoding="utf-8") as hard_file:
                #read
                sentences=hard_file.read().split("\n")

                # Hent random settning
                random_sentence = random.choice(sentences)

    def display_results(self, event, sentence, index):
        """
        Denne metoden kalulerer alle resultatene fra typing testen
        :param event: event som er overf??rt fra tkinter.bind(seq, func) metode
        :param sentence: settningen som er gitt til brukeren til testen
        :param index: index for ?? identifisere modusen til testen
        :return: None
        """
        # calculate time
        self.total_time = time.time() - self.start_time

        # Hent bruker input basert p?? vinduet som er ??pent
        if index == 0:
            user_input = self.easy_text_entry.get()
        elif index == 1:
            user_input = self.medium_text_entry.get()
        else:
            user_input = self.hard_text_entry.get()

        #kalkuler accuracy
        count = 0
        for i, char in enumerate(sentence):
            try:
                if user_input[i] == char:
                    count += 1
            except Exception:
                pass
        self.accuracy = count / len(user_input) * 100

        # Kalkuler wpm

        self.wpm = len(user_input) * 60 / (5 * self.total_time)

        # sjekk hvilken index overf??rt til metoden for ?? identifisere hvilken modus av testen som blir tatt.
        if index == 0:
            # vise resultat i medium window
            self.easy_rules_label.grid_forget()
            self.easy_rules_label = ttk.Label(self.easy_mainframe,
                                              text=f"Time:{round(self.total_time)} seconds Accuracy:{round(self.accuracy)}% Wpm:{round(self.wpm)}",
                                              style="Labels.TLabel")
            self.easy_rules_label.grid(column=0, row=2, padx=10, pady=10, columnspan=2)
        elif index == 1:
            # vise resultat i medium window
            self.medium_rules_label.grid_forget()
            self.medium_rules_label = ttk.Label(self.medium_mainframe,
                                                text=f"Time:{round(self.total_time)} seconds Accuracy:{round(self.accuracy)}% Wpm:{round(self.wpm)}",
                                                style="Labels.TLabel")
            self.medium_rules_label.grid(column=0, row=2, padx=10, pady=10, columnspan=2)


    def close_window(self, index):
        """
        Denne funksjonen lukker vinduet.
        :parameter index: index for ?? identifisere hvilket vindu som skal lukkes.
        """
        # lukker vinduet knyttet til den gitte index
        if index == 0:
            self.easy_window.destroy()
        elif index == 1:
            self.medium_window.destroy()

        # endrer button state tilbake til normal
        self.easy_button.configure(state=NORMAL)
        self.medium_button.configure(state=NORMAL)



        self.deiconify()
