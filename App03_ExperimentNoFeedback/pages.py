from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants



class p02_description(Page):
    """Description of the game: How to play and returns expected"""
    def is_displayed(self):
        return self.subsession.round_number == 1

class p05_example3(Page):
    """Description of the game: How to play and returns expected"""
    form_model = 'player'
    form_fields =['myTechEx3','otherTechEx3','myEarnEx3']

    def is_displayed(self):
        return self.subsession.round_number == 1


class p07_preTask(Page):
    """Description of the game: How to play and returns expected"""

    def is_displayed(self):
        if self.player.round_number % Constants.maxTechnologies == 1:
            self.player.initDraws()
        else:
            self.player.getPreviousDraws()
        return self.subsession.round_number % Constants.maxTechnologies == 1

    def vars_for_template(self):
        temp = {}
        temp['marketType'] = self.player.marketType
        temp['myCost'] = self.player.myCost
        temp['taskNumber'] = self.player.taskNumber+0 #CHANGE HERE WHEN CHANGING ORDER
        return temp

class p08_taskPart1(Page):
    """Description of the game: How to play and returns expected"""
    form_model = 'player'
    form_fields = ['myChoice']

    def before_next_page(self):
        self.player.updateMyTech()

    def vars_for_template(self):
        temp = {}
        temp['marketType'] = self.player.marketType
        temp['bestTech'] = self.player.bestTech
        temp['marketTech'] = self.player.marketTech
        temp['currentEarn'] = self.player.currentEarn
        # temp['myDraws'] = self.player.myDraws
        temp['myTech'] = self.player.myTech
        temp['taskNumber'] = self.player.taskNumber+0 #CHANGE HERE WHEN CHANGING ORDER
        temp['techNumber'] = self.player.techNumber
        temp['myCost'] = self.player.myCost
        temp['winStatus'] = self.player.winStatus

        return temp

class p09_postTaskPart1(Page):
    """Description of the game: How to play and returns expected"""
    form_model = 'player'
    form_fields = ['myEarnN']

    def before_next_page(self):
        self.participant.vars['NoFeedTask'+str(self.player.taskNumber)+"Earn"]=self.player.myEarnN

        if self.player.myEarnings==None:
            self.player.myEarnings=str(self.player.myEarnN)
        else:
            self.player.myEarnings+=","+str(self.player.myEarnN)


    def is_displayed(self):
        return self.subsession.round_number % Constants.maxTechnologies == 0

    def vars_for_template(self):
        temp = {}
        temp['marketType'] = self.player.marketType
        temp['bestTech'] = self.player.bestTech
        temp['marketTech'] = self.player.marketTech
        temp['currentEarn'] = self.player.currentEarn
        # temp['myDraws'] = self.player.myDraws
        temp['myTech'] = self.player.myTech
        temp['taskNumber'] = self.player.taskNumber+0 #CHANGE HERE WHEN CHANGING ORDER
        temp['techNumber'] = self.player.techNumber
        temp['myCost'] = self.player.myCost
        temp['winStatus'] = self.player.winStatus

        return temp



class WaitForOtherBegin(WaitPage):
    template_name = 'App03_ExperimentNoFeedback/myWaitPage.html'

    def after_all_players_arrive(self):
        if self.round_number % Constants.maxTechnologies  == 1:
            pass

    def vars_for_template(self):
        title_text = "Please wait for other participants"
        body_text = ""
        return {'title_text': title_text,"body_text":body_text}


class WaitForOtherEnd(WaitPage):
    template_name = 'App03_ExperimentNoFeedback/myWaitPage.html'

    def after_all_players_arrive(self):
        self.group.getBestTech()

    def vars_for_template(self):
        title_text = "Please wait for other participants"
        body_text = ""
        return {'title_text': title_text, "body_text": body_text}



page_sequence = [
    p02_description,
    p05_example3,
    WaitForOtherBegin,
    p07_preTask,
    p08_taskPart1,
    WaitForOtherEnd,
    p09_postTaskPart1

]
