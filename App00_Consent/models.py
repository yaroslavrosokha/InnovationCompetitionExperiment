from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)

import numpy as np

author = 'Yaroslav Rosokha'

doc = """
Informed Consent
"""


class Constants(BaseConstants):
    name_in_url = 'Consent'
    players_per_group = None
    num_rounds = 1


class Group(BaseGroup):
    pass

class Subsession(BaseSubsession):
    pass

class Player(BasePlayer):

    consent = models.StringField()
