"""
    This module manages the random answers of GrandPy-Bot
    to reinforce the interractivity.
"""
from random import choice


class GrandPySoul:
    """
        All interruptions of GranPy-Bot are available in this class.
    """
    def __init__(self):
        self.quotes_formatted_address = ["Biensur mon poussin, l'adresse est ",
                                         "Si ma mémoire ne me joue pas de tour, c'est ",
                                         "Oui bien évidement, ",
                                         "Je crois me rappeler que c'est "]


        self.quotes_description = ["T'ai-je déjà raconté que ",
                                   "Oui..., cela me revient maintenant..., ",
                                   "Ca me rappelle que ",
                                   "Savais-tu que "]

        self.messages_error = ["ZZZzz zzZZZZzzzzz Zzzz ZZZZzzzz ",
                               "Parle plus fort, à mon âge tu sais.... ",
                               "Cela ne me dis rien du tout... ",
                               "Demande à GrandMyPy, peut-être... "]


    def formatted_address_quote(self):
        """
            Return a random sentence for the formatted adress.
        """
        return choice(self.quotes_formatted_address)

    def error_message_quote(self):
        """
            Return a random sentence for the error message.
        """
        return choice(self.messages_error)

    def desrciption_quote(self):
        """
            Return a random sentence for the description.
        """
        return choice(self.quotes_description)
