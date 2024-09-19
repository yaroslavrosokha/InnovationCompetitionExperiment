from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)

import numpy as np

author = 'Yaroslav Rosokha'

doc = """
Risk Aversion Elicitation (ala Holt-Laury)
"""


class Constants(BaseConstants):
    name_in_url = 'App05_RiskAversionElicitation'
    players_per_group = None
    num_rounds = 1

    safeOption2 = [.5,1,1.5,2,2.5,3,3.5,4,4.5,5,5.5,6,6.5,7,7.5,8,8.5,9,9.5,10]
    safeOption2Practice = [0.5, 2.5, 5, 7.5, 10.0]

    riskySuccess=10
    riskyFailure=0


class Group(BaseGroup):
    pass

class Subsession(BaseSubsession):
    pass

class Player(BasePlayer):
    chosenPracticeQuestion = models.IntegerField()
    practiceResponses = models.StringField(initial="")

    checkConfirm = models.StringField()

    practiceTaskSelected = models.StringField()
    practiceDecisionSelected = models.StringField()
    practiceDrawSelected = models.StringField()

    responses = models.StringField()
    chosenQuestion = models.IntegerField()
    chosenTaskPart2 = models.IntegerField()
    chosenDraw = models.IntegerField()



