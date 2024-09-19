from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants



class p02_description(Page):
    """Description of the game: How to play and returns expected"""
    def is_displayed(self):
        self.player.existingTech=self.participant.vars['innovationSingleDMOrder'][self.player.round_number-1]
        return self.subsession.round_number == 1

    def before_next_page(self):
        self.player.initDraws()

    def vars_for_template(self):
        temp = {}
        temp['existingTech'] = self.player.existingTech
        return temp

class p03_example1(Page):
    """Description of the game: How to play and returns expected"""
    form_model = 'player'
    form_fields =['myTechEx1','myEarnEx1','myDecisionsEx1']

    def vars_for_template(self):
        temp = {}
        temp['existingTech'] = self.participant.vars['innovationSingleDMOrder'][self.player.round_number-1]
        temp['taskNumber'] = self.player.round_number+19
        return temp

    def before_next_page(self):
        self.participant.vars['SingleTask'+str(self.player.round_number)+"Earn"]=self.player.myEarnEx1

page_sequence = [
    p02_description,
    p03_example1
]
