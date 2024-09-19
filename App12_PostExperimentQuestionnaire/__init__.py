import numpy as np
from otree.api import *


author = 'Yaroslav Rosokha'
doc = """
Post-experimental Questionnaire.
"""


class Constants(BaseConstants):
    name_in_url = 'App12_PostExperimentQuestionnaire'
    players_per_group = None
    num_rounds = 1


class Group(BaseGroup):
    pass


class Subsession(BaseSubsession):
    pass


class Player(BasePlayer):
    # Questionnaire
    understandingSelect = models.StringField(
        choices=['Clear', 'Somewhat Clear', 'Somewhat Confusing', 'Confusing'],
        verbose_name='Clarity of Instructions:',
        blank=True,
        widget=widgets.RadioSelectHorizontal,
    )
    explainedText = models.StringField(
        verbose_name='What could have been explained better?',
        blank=True,
    )
    strategy3Text = models.StringField(
        verbose_name='What was your strategy for the third market type (in which you were sole entrepreneur)?',
        blank=True,
    )
    strategy2Text = models.StringField(
        verbose_name='What was your strategy for the second market type (in which you and another randomly selected participant were two entrepreneur, and best available technology was unknown)?',
        blank=True,
    )
    strategy1Text = models.StringField(
        verbose_name='What was your strategy for the first market type (in which you and another randomly selected participant were two entrepreneur, and best available technology was known)?',
        blank=True,
    )


# FUNCTIONS
# PAGES
class Questionnaire(Page):
    form_model = 'player'
    form_fields = [
        'understandingSelect',
        'explainedText',
        'strategy1Text',
        'strategy2Text',
        'strategy3Text',
    ]

    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == Constants.num_rounds


class ThankYou(Page):
    @staticmethod
    def vars_for_template(player: Player):
        return {'earningsTotal': player.participant.payoff_plus_participation_fee()}


page_sequence = [
    Questionnaire,
    ThankYou,
]
