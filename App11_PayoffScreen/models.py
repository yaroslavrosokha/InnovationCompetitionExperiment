from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)

import numpy as np

author = 'Yaroslav Rosokha'

doc = """
Payoff information.
"""


class Constants(BaseConstants):
    name_in_url = 'App11_PayoffScreen'
    players_per_group = None
    num_rounds = 1


class Group(BaseGroup):
    pass


class Subsession(BaseSubsession):
    pass

class Player(BasePlayer):
    total = models.CurrencyField()
    task1 = models.StringField()
    task2 = models.StringField()
