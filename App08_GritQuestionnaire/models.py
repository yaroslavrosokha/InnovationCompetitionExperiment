from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)

import numpy as np

author = 'Yaroslav Rosokha'

doc = """
Grit Questionnaire (Duckworth)
"""


class Constants(BaseConstants):
    name_in_url = 'App08_GritQuestionnaire'
    players_per_group = None
    num_rounds=1


class Group(BaseGroup):

    pass


class Subsession(BaseSubsession):
    pass

class Player(BasePlayer):

    # Part 4: Grit Questionnaire

    choiceVector=('Very much like me','Mostly like me','Somewhat like me','Not much like me','Not like me at all')

    grit_1 = models.StringField(
        choices=choiceVector,
        verbose_name='1) I have overcome setbacks to conquer an important challenge.',blank=False)

    grit_2 = models.StringField(
        choices=choiceVector,
        verbose_name='2) New ideas and projects sometimes distract me from previous ones.',blank=False)

    grit_3 = models.StringField(
        choices=choiceVector,
        verbose_name='3) My interests change from year to year.',blank=False)

    grit_4 = models.StringField(
        choices=choiceVector,
        verbose_name='4) Setbacks don’t discourage me.',blank=False)

    grit_5 = models.StringField(
        choices=choiceVector,
        verbose_name='5) I have been obsessed with a certain idea or project for a short time but later lost interest.',blank=False)

    grit_6 = models.StringField(
        choices=choiceVector,
        verbose_name='6) I am a hard worker.',blank=False)

    grit_7 = models.StringField(
        choices=choiceVector,
        verbose_name='7) I often set a goal but later choose to pursue a different one.',blank=False)

    grit_8 = models.StringField(
        choices=choiceVector,
        verbose_name='8) I have difficulty maintaining my focus on projects that take more than a few months to complete.',blank=False)

    grit_9 = models.StringField(
        choices=choiceVector,
        verbose_name='9) I finish whatever I begin.',blank=False)

    grit_10 = models.StringField(
        choices=choiceVector,
        verbose_name='10) I have achieved a goal that took years of work.',blank=False)

    grit_11 = models.StringField(
        choices=choiceVector,
        verbose_name='11) I become interested in new pursuits every few months.',blank=False)

    grit_12 = models.StringField(
        choices=choiceVector,
        verbose_name='12) I am diligent.',blank=False)
