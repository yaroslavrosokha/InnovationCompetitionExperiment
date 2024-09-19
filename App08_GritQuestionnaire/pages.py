from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants

import random

class Grit(Page):

    form_model = 'player'
    form_fields = ['grit_{}'.format(i) for i in range(1, 13)]

    def vars_for_template(self):
        temp=list(range(1,13))
        random.shuffle(temp)
        return {'questions': zip(temp,self.form_fields)}

    def is_displayed(self):
        return self.round_number == Constants.num_rounds



page_sequence = [

    Grit

]
