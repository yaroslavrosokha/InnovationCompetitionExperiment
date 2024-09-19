from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants

import numpy as np



class p03_task(Page):
    """Description of the game: How to play and returns expected"""

    form_model = 'player'
    form_fields = ['responses','checkConfirm']

    def vars_for_template(self):
        return {'offer_numbers': zip(range(1,len(Constants.safeOption2)+1),Constants.safeOption2)}

    def before_next_page(self):
        self.participant.vars['LossAversionChoices']=self.player.responses
        self.player.chosenQuestion=np.random.choice(np.arange(20)) + 1
        self.participant.vars['LossAversionQuestion'] = self.player.chosenQuestion
        self.player.chosenDraw = np.random.choice([-self.player.chosenQuestion*.5,5.00],p=[.5,.5])
        self.participant.vars['LossAversionDraw'] = self.player.chosenDraw
        if self.player.responses[self.player.chosenQuestion-1]=='A':
            self.participant.vars['LossAversionEarn'] = self.player.chosenDraw
        else:
            self.participant.vars['LossAversionEarn'] = 0.0


page_sequence = [
    p03_task
]
