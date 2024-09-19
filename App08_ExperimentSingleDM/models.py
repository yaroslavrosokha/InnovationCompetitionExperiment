from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)

import numpy as np

author = 'Yaroslav Rosokha'

doc = """
Innovation experiment: singled decision-maker.
"""


class Constants(BaseConstants):
    name_in_url = 'App08_ExperimentSingleDM'

    min_payment = 0
    players_per_group = None
    tasks = 8
    maxTechnologies = 10
    num_rounds = tasks
    cost1 = 1
    expLambda = 0.125

    existingTechnologies = [18.421, 23.966, 15.177, 18.421, 23.966, 15.177, 16.832, 20.205]


class Group(BaseGroup):

    pass



class Subsession(BaseSubsession):

    def creating_session(self):
        if self.round_number == 1:
            for p in self.get_players():
                arr = np.array([18.421, 23.966, 15.177, 18.421, 23.966, 15.177, 16.832, 20.205])
                np.random.shuffle(arr)
                p.participant.vars['innovationSingleDMOrder'] = arr

class Player(BasePlayer):

    #Contest variables
    taskNumber = models.IntegerField()

    bestTech = models.FloatField()
    existingTech = models.FloatField(initial=15)
    myTechEx1 = models.StringField()
    myDecisionsEx1 = models.StringField()
    myEarnEx1 = models.CurrencyField()


    def initDraws(self):
        self.bestTech = 0
        self.existingTech = self.participant.vars['innovationSingleDMOrder'][self.round_number - 1]
        self.taskNumber = self.round_number
