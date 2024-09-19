from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants

import random

class AchievementComp(Page):

    form_model = 'player'
    form_fields = ['myResponses1']

    def vars_for_template(self):
        tempQ1 = []
        for i in range(1,8+1):
            tempQ1.append(Constants.questions[self.participant.vars['randomCompOrder'][i]-1])

        tempQ2 = []
        for i in range(9,16+1):
            tempQ2.append(Constants.questions[self.participant.vars['randomCompOrder'][i]-1])

        return {'randomQuestionsOrder1': zip(range(1, 8 + 1), tempQ1),
                'randomQuestionsOrder2': zip(range(9, 16 + 1), tempQ2)}

    def before_next_page(self):
        self.participant.vars['achievementComp']=self.player.myResponses1


page_sequence = [

    AchievementComp

]
