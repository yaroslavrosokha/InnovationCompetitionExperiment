import random

import numpy as np
from otree.api import *


author = 'Yaroslav Rosokha'
doc = """
Big 5 Questionnaire (44-item from John, O. P., & Srivastava, S. (1999))
"""


class Constants(BaseConstants):
    name_in_url = 'App09_BigFiveQuestionnaire'
    players_per_group = None
    num_rounds = 1
    questions = [
        "Is talkative",
        "Tends to find fault with others",
        "Does a thorough job",
        "Is depressed, blue",
        "Is original, comes up with new ideas",
        "Is reserved",
        "Is helpful and unselfish with others",
        "Can be somewhat careless",
        "Is relaxed, handles stress well",
        "Is curious about many different things",
        "Is full of energy",
        "Starts quarrels with others",
        "Is a reliable worker",
        "Can be tense",
        "Is ingenious, a deep thinker",
        "Generates a lot of enthusiasm",
        "Has a forgiving nature",
        "Tends to be disorganized",
        "Worries a lot",
        "Has an active imagination",
        "Tends to be quiet",
        "Is generally trusting",
        "Tends to be lazy",
        "Is emotionally stable, not easily upset",
        "Is inventive",
        "Has an assertive personality",
        "Can be cold and aloof",
        "Perseveres until the task is finished",
        "Can be moody",
        "Values artistic, aesthetic experiences",
        "Is sometimes shy, inhibited",
        "Is considerate and kind to almost everyone",
        "Does things efficiently",
        "Remains calm in tense situations",
        "Prefers work that is routine",
        "Is outgoing, sociable",
        "Is sometimes rude to others",
        "Makes plans and follows through with them",
        "Gets nervous easily",
        "Likes to reflect, play with ideas",
        "Has few artistic interests",
        "Likes to cooperate with others",
        "Is easily distracted",
        "Is sophisticated in art, music, or literature",
    ]


class Group(BaseGroup):
    pass


class Subsession(BaseSubsession):
    pass

def creating_session(subsession: Subsession):

        if subsession.round_number == 1:
            for p in subsession.get_players():
                randomOrder = list(range(1, 44 + 1))
                random.shuffle(randomOrder)
                p.participant.vars['bigFiveOrder'] = dict(zip(range(1, 44 + 1), randomOrder))
                out = ""
                for x in randomOrder:
                    out += "," + str(x)
                p.myOrder = out


class Player(BasePlayer):
    myResponses1 = models.StringField()
    myResponses2 = models.StringField()
    myOrder = models.StringField()


# FUNCTIONS
# PAGES
class BigFive(Page):
    form_model = 'player'
    form_fields = ['myResponses1']

    @staticmethod
    def vars_for_template(player: Player):
        tempQ1 = []
        for i in range(1, 11 + 1):
            tempQ1.append(Constants.questions[player.participant.vars['bigFiveOrder'][i] - 1])
        tempQ2 = []
        for i in range(12, 22 + 1):
            tempQ2.append(Constants.questions[player.participant.vars['bigFiveOrder'][i] - 1])
        return {
            'randomQuestionsOrder1': zip(range(1, 11 + 1), tempQ1),
            'randomQuestionsOrder2': zip(range(12, 22 + 1), tempQ2),
        }

    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        player.participant.vars['Big5Part1'] = player.myResponses1


class BigFivePart2(Page):
    form_model = 'player'
    form_fields = ['myResponses2']

    @staticmethod
    def vars_for_template(player: Player):
        tempQ3 = []
        for i in range(23, 33 + 1):
            tempQ3.append(Constants.questions[player.participant.vars['bigFiveOrder'][i] - 1])
        tempQ4 = []
        for i in range(34, 44 + 1):
            tempQ4.append(Constants.questions[player.participant.vars['bigFiveOrder'][i] - 1])
        return {
            'randomQuestionsOrder3': zip(range(1, 11 + 1), tempQ3),
            'randomQuestionsOrder4': zip(range(12, 22 + 1), tempQ4),
        }

    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        player.participant.vars['Big5Part2'] = player.myResponses2


page_sequence = [BigFive, BigFivePart2]
