from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)

author = 'Yaroslav Rosokha'

doc = """
Introduction to the innovation experiment.
"""

class Constants(BaseConstants):
    name_in_url = 'App02_ExperimentIntroduction'

    min_payment = 5
    players_per_group = None
    duration = 60

    num_rounds = 1

class Group(BaseGroup):
    pass

class Subsession(BaseSubsession):
    pass

class Player(BasePlayer):
    pass
