from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants

import numpy as np


class p01_introduction(Page):
    """Description of the game: How to play and returns expected"""
    pass


class p03_task(Page):
    """Description of the game: How to play and returns expected"""

    form_model = 'player'
    form_fields = ['responses','checkConfirm']

    def vars_for_template(self):
        return {'offer_numbers': zip(range(1,len(Constants.safeOption2)+1),Constants.safeOption2)}

    def before_next_page(self):
        self.participant.vars['SunkCostChoices'] = self.player.responses
        self.player.chosenQuestion = np.random.choice(np.arange(20)) + 1
        self.participant.vars['SunkCostQuestion'] = self.player.chosenQuestion
        if self.player.responses[self.player.chosenQuestion-1]=='A':
            self.participant.vars['SunkCostEarn'] = 15-5-.5*float(self.player.chosenQuestion)
        else:
            self.participant.vars['SunkCostEarn'] = 15-5


class WaitForOthers(WaitPage):
    template_name = 'App07_SunkCostFallacyElicitation/myWaitPage.html'

    def vars_for_template(self):

        title_text = "Please wait for other participants..."
        body_text = ""

        return {'title_text': title_text,"body_text":body_text}


page_sequence = [
    p01_introduction,
    p03_task
]
