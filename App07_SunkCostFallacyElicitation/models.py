from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)

import numpy as np

author = 'Yaroslav Rosokha'

doc = """
Sunk Cost Elicitation.
"""


class Constants(BaseConstants):
    name_in_url = 'App07_SunkCostFallacyElicitation'
    players_per_group = None
    num_rounds = 1

    safeOption2 = [0.5, 1.0, 1.5, 2.0, 2.5, 3.0, 3.5, 4.0, 4.5, 5.0, 5.5, 6.0, 6.5, 7.0, 7.5, 8.0, 8.5, 9.0, 9.5, 10.0]
    safeOption2Practice = [0.5, 2.5, 5, 7.5, 10.0]

    riskySuccess=10
    riskyFailure=0


class Group(BaseGroup):
    pass

class Subsession(BaseSubsession):
    pass

class Player(BasePlayer):
    chosenPracticeQuestion = models.IntegerField()
    practiceResponses = models.StringField()

    checkConfirm = models.StringField()

    practiceTaskSelected = models.StringField()
    practiceDecisionSelected = models.StringField()
    practiceDrawSelected = models.StringField()

    responses = models.StringField()
    chosenQuestion = models.IntegerField()
    chosenTaskPart2 = models.IntegerField()
    chosenDraw = models.IntegerField()



