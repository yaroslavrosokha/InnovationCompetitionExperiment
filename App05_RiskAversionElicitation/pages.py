from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants

import numpy as np


class p01_introduction(Page):
    """Description of the game: How to play and returns expected"""

    form_model = 'player'
    form_fields = ['practiceResponses','checkConfirm']

    def vars_for_template(self):
        return {'offer_numbers': zip(range(1,len(Constants.safeOption2Practice)+1),Constants.safeOption2Practice)}

    def is_displayed(self):
        self.player.chosenPracticeQuestion=np.random.choice(np.arange(5))+1
        self.player.chosenQuestion = np.random.choice(np.arange(5)) + 1
        return self.subsession.round_number == 1


class p02_compensationInstructions(Page):
    """Description of the game: How to play and returns expected"""

    form_model = 'player'
    form_fields = ['practiceTaskSelected','practiceDecisionSelected','practiceDrawSelected']


    def vars_for_template(self):
        temp = {'offer_numbers': zip(range(1,len(Constants.safeOption2Practice)+1),Constants.safeOption2Practice)}
        temp['practiceResponses'] = self.player.practiceResponses
        temp['chosenPracticeQuestion'] = self.player.chosenPracticeQuestion
        return temp


class p03_task(Page):
    """Description of the game: How to play and returns expected"""

    form_model = 'player'
    form_fields = ['responses','checkConfirm']

    def vars_for_template(self):
        return {'offer_numbers': zip(range(1,len(Constants.safeOption2)+1),Constants.safeOption2)}

    def before_next_page(self):
        self.participant.vars['RiskAversionChoices']=self.player.responses
        self.player.chosenQuestion=np.random.choice(np.arange(20)) + 1
        self.participant.vars['RiskAversionQuestion'] = self.player.chosenQuestion
        self.player.chosenDraw = np.random.choice([10,0],p=[.5,.5])
        self.participant.vars['RiskAversionDraw'] = self.player.chosenDraw
        if self.player.responses[self.player.chosenQuestion-1]=='A':
            self.participant.vars['RiskAversionEarn'] = self.player.chosenDraw
        else:
            self.participant.vars['RiskAversionEarn'] = self.player.chosenQuestion*.5



class WaitForOthers(WaitPage):
    template_name = 'riskAversionElicitation/myWaitPage.html'

    def vars_for_template(self):
        print("RiskAversion,WaitForOthers()...")

        title_text = "Please wait for other participants..."
        body_text = ""

        return {'title_text': title_text,"body_text":body_text}


page_sequence = [
    p01_introduction,
    p02_compensationInstructions,
    p03_task
]
