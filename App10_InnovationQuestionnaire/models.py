from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)

import numpy as np
import random

author = 'Yaroslav Rosokha'

doc = """
Achievement-striving + Competitive
"""


class Constants(BaseConstants):
    name_in_url = 'App10_InnovationQuestionnaire'
    players_per_group = None
    num_rounds=1

    questions=[
        "Go straight for the goal.",
        "Work hard.",
        "Turn plans into actions.",
        "Plunge into tasks with all my heart.",
        "Do more than what's expected of me.",
        "Set high standards for myself and others.",
        "Demand quality.",
        "Am not highly motivated to succeed.",
        "Do just enough work to get by.",
        "Put little time and effort into my work.",

        "Accept challenging tasks.",
        "Am good at many things.",
        "Feel up to any task.",
        "Am not highly motivated to succeed.",
        "Do just enough work to get by.",
        "Undertake few things on my own."
    ]


class Group(BaseGroup):
    pass


class Subsession(BaseSubsession):
        def creating_session(self):
            if self.round_number == 1:
                for p in self.get_players():
                    randomOrder = list(range(1,16+1))
                    random.shuffle(randomOrder)
                    p.participant.vars['randomCompOrder'] = dict(zip(range(1,16+1), randomOrder))
                    out = ""
                    for x in randomOrder:
                        out+=","+str(x)
                    p.myOrder = out

class Player(BasePlayer):

    myResponses1 = models.StringField()
    myOrder = models.StringField()
