import numpy as np
from otree.api import *


author = 'Yaroslav Rosokha'
doc = """
Demographic Questionnaire (Pre-experiment Survey) 
"""


class Constants(BaseConstants):
    name_in_url = 'App01_PreExperimentQuestionnaire'
    players_per_group = None
    num_rounds = 1


class Group(BaseGroup):
    pass


class Subsession(BaseSubsession):
    pass


class Player(BasePlayer):
    # Questionnaire
    ageSelect = models.IntegerField(verbose_name='Age:', min=16, max=100)
    genderSelect = models.StringField(
        choices=['Male', 'Female', 'Other', 'Prefer Not To Say'], verbose_name='Sex/Gender:'
    )
    raceSelect = models.StringField(
        choices=[
            'White',
            'Hispanic or Latino',
            'Black or African American',
            'Native American or American Indian',
            'Asian or Pacific Islander',
            'Other',
            'Prefer Not To Say',
        ],
        verbose_name='Race/Ethnicity:',
    )
    classSelect = models.StringField(
        choices=[
            'Freshman',
            'Sophomore',
            'Junior',
            'Senior',
            'Graduate student',
            'Professional student',
            'Continuing education student',
            'Prefer Not To Say',
        ],
        verbose_name='Class Status:',
    )
    majorSelect = models.StringField(
        choices=[
            'Economics, Management, or Business',
            'STEM (Science, Technology, Engineering, Math)',
            'Liberal Arts',
            'Other',
            'Prefer Not To Say',
        ],
        verbose_name='Major:',
    )



# FUNCTIONS
# PAGES
class Questionnaire(Page):
    form_model = 'player'
    form_fields = [
        'ageSelect',
        'genderSelect',
        'raceSelect',
        'classSelect',
        'majorSelect'
    ]

page_sequence = [Questionnaire]
