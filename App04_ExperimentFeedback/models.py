from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)

import numpy as np

author = 'Yaroslav Rosokha'

doc = """
Innovation experiment: Contest with feedback.
"""


class Constants(BaseConstants):
    name_in_url = 'App04_ExperimentFeedback'
    players_per_group = 2
    tasks = 8
    maxTechnologies = 10
    expLambda = 0.125
    num_rounds = maxTechnologies * tasks
    cost2=1



class Group(BaseGroup):

    marketTech = models.FloatField()
    marketType = models.IntegerField()

    def getBestTech(self):
        p1, p2 = self.get_players()
        if p1.bestTech > p2.bestTech:
            self.marketTech = p1.bestTech
            winner = p1
            loser = p2
        elif p1.bestTech < p2.bestTech:
            self.marketTech = p2.bestTech
            winner = p2
            loser = p1
        else:
            self.marketTech = p2.bestTech
            if np.random.random() < 0.5:
                winner = p1
                loser = p2
            else:
                winner = p2
                loser = p1

        winner.winStatus=True
        loser.winStatus=False
        winner.marketTech=self.marketTech
        loser.marketTech=self.marketTech
        winner.currentEarn = c(self.marketTech)
        loser.currentEarn = c(0)


class Subsession(BaseSubsession):
    def creating_session(self):
        if self.round_number % Constants.maxTechnologies == 1:
            self.group_randomly()
        else:
            self.group_like_round(1+((self.round_number-1) // Constants.maxTechnologies)*Constants.maxTechnologies)


class Player(BasePlayer):
    #Contest variables
    marketType = models.IntegerField(initial=2)
    taskNumber = models.IntegerField()
    techNumber = models.IntegerField()
    bestTech = models.FloatField()
    marketTech = models.FloatField()
    currentEarn = models.CurrencyField()

    myChoice = models.BooleanField()
    winStatus = models.BooleanField(initial=False)
    myTech = models.StringField()
    myCost = models.CurrencyField()

    myEarnN = models.CurrencyField()
    myEarn = models.CurrencyField()
    myEarnings = models.StringField(initial=0)

    myCurrentTech = models.StringField()
    otherTech = models.StringField()

    myTechEx2 = models.StringField()
    myEarnEx2 = models.CurrencyField()
    otherTechEx2 = models.StringField()


    def updateMyTech(self):
        if self.myChoice==True:
            self.myTech += "," + str(np.round(np.random.exponential(scale=1.0/Constants.expLambda), 3))

        tempTech = self.myTech.split(",")
        tempTech = [float(t) for t in tempTech if len(t)>0]
        if len(tempTech)>0:
            self.bestTech = np.max(tempTech)
        else:
            self.bestTech = 0.0


    def initDraws(self):
        self.bestTech = 0.0
        self.marketTech = 0.0
        self.currentEarn = c(0)
        self.taskNumber = 1+self.round_number // Constants.maxTechnologies
        self.techNumber =  1+(self.round_number-1) % Constants.maxTechnologies
        self.myTech = ""
        self.myCost = c(1)


    def getPreviousDraws(self):
        self.bestTech = self.in_round(self.round_number - 1).bestTech
        self.marketTech = self.in_round(self.round_number - 1).marketTech
        self.currentEarn = self.in_round(self.round_number - 1).currentEarn

        self.myTech = self.in_round(self.round_number - 1).myTech
        self.marketType = self.in_round(self.round_number - 1).marketType
        self.taskNumber = self.in_round(self.round_number - 1).taskNumber
        self.techNumber = self.in_round(self.round_number - 1).techNumber+1
        self.myCost = self.in_round(self.round_number - 1).myCost
        self.myEarnings = self.in_round(self.round_number - 1).myEarnings
