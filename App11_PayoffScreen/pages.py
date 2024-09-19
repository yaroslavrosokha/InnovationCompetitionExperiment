from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants




class PaymentInfo(Page):

    form_model = 'player'
    form_fields = ['total','task1','task2']

    def before_next_page(self):
        self.participant.vars['totalPayoffs']=self.player.total
        self.player.payoff=self.player.total

    def vars_for_template(self):
        return {'YesFeedTask1Earn':self.participant.vars['YesFeedTask1Earn'],
                'YesFeedTask2Earn':self.participant.vars['YesFeedTask2Earn'],
                'YesFeedTask3Earn':self.participant.vars['YesFeedTask3Earn'],
                'YesFeedTask4Earn': self.participant.vars['YesFeedTask4Earn'],
                'YesFeedTask5Earn': self.participant.vars['YesFeedTask5Earn'],
                'YesFeedTask6Earn': self.participant.vars['YesFeedTask6Earn'],
                'YesFeedTask7Earn': self.participant.vars['YesFeedTask7Earn'],
                'YesFeedTask8Earn': self.participant.vars['YesFeedTask8Earn'],
                # 'YesFeedTask9Earn': self.participant.vars['YesFeedTask9Earn'],
                # 'YesFeedTask10Earn': self.participant.vars['YesFeedTask10Earn'],

                'NoFeedTask1Earn': self.participant.vars['NoFeedTask1Earn'],
                'NoFeedTask2Earn': self.participant.vars['NoFeedTask2Earn'],
                'NoFeedTask3Earn': self.participant.vars['NoFeedTask3Earn'],
                'NoFeedTask4Earn': self.participant.vars['NoFeedTask4Earn'],
                'NoFeedTask5Earn': self.participant.vars['NoFeedTask5Earn'],
                'NoFeedTask6Earn': self.participant.vars['NoFeedTask6Earn'],
                'NoFeedTask7Earn': self.participant.vars['NoFeedTask7Earn'],
                'NoFeedTask8Earn': self.participant.vars['NoFeedTask8Earn'],
                # 'NoFeedTask9Earn': self.participant.vars['NoFeedTask9Earn'],
                # 'NoFeedTask10Earn': self.participant.vars['NoFeedTask10Earn'],

                'RiskAversionEarn': float(self.participant.vars['RiskAversionEarn']),
                'RiskAversionQuestion': str(int(self.participant.vars['RiskAversionQuestion'])),
                'RiskAversionChoices': self.participant.vars['RiskAversionChoices'],
                'LossAversionEarn': float(self.participant.vars['LossAversionEarn']),
                'LossAversionQuestion': str(int(self.participant.vars['LossAversionQuestion'])),
                'LossAversionChoices': self.participant.vars['LossAversionChoices'],
                'SunkCostEarn': float(self.participant.vars['SunkCostEarn']),
                'SunkCostQuestion': str(int(self.participant.vars['SunkCostQuestion'])),
                'SunkCostChoices': self.participant.vars['SunkCostChoices'],

                'SingleTask1Earn': self.participant.vars['SingleTask1Earn'],
                'SingleTask2Earn': self.participant.vars['SingleTask2Earn'],
                'SingleTask3Earn': self.participant.vars['SingleTask3Earn'],
                'SingleTask4Earn': self.participant.vars['SingleTask4Earn'],
                'SingleTask5Earn': self.participant.vars['SingleTask5Earn'],
                'SingleTask6Earn': self.participant.vars['SingleTask6Earn'],
                'SingleTask7Earn': self.participant.vars['SingleTask7Earn'],
                'SingleTask8Earn': self.participant.vars['SingleTask8Earn'],
                # 'SingleTask9Earn': self.participant.vars['SingleTask9Earn'],
                # 'SingleTask10Earn': self.participant.vars['SingleTask10Earn']
                }

    def is_displayed(self):
        return self.round_number == Constants.num_rounds




page_sequence = [

    PaymentInfo

]
