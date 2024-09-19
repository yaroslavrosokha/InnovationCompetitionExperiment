from otree.api import Currency as c, currency_range
from . import pages
from ._builtin import Bot
from .models import Constants


class PlayerBot(Bot):

    def play_round(self):
        yield (pages.P1_1_Introduction)
        yield (pages.P2_1_ExampleTask)
        yield (pages.P3_1_ExampleTask)
        yield (pages.P3a_1_PracticeCompensation)
        yield (pages.P4_1_Task1)
        yield (pages.P5_1_Task2)
        yield (pages.P12_1_ExampleTask)

        # yield (pages.P4_1_Task1)
        # yield (pages.P5_1_Task2)
        # yield (pages.P6_1_Task3)
        # yield (pages.P7_1_Task4)
        # yield (pages.P10_1_Results)