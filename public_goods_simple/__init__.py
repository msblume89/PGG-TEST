from otree.api import *



class Constants(BaseConstants):
    name_in_url = 'public_goods_simple'
    players_per_group = 4
    num_rounds = 2
    endowment = 20
    multiplier = 0.5                                #wenn mit Spieleranzahl in PayOff-Formel, dann bei 4 Spielern 1,6 (0,4*4)
                                                    #sonst bei bei 2 Sp. 1, bei 4 Sp. 0.5, bei 8 Sp. 0.25 usw. (Vogt Paper) bzw. 2 Sp. 0.8, bei 4 Sp. 0.4, bei 8 Sp. 0.2 usw.(Gächter Paper)
    beginningloss = -40                             #Anfangswert des Privatkontos


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    total_contribution = models.IntegerField()
    total_claim = models.IntegerField()
    individual_share = models.FloatField()


class Player(BasePlayer):
    personal_income = models.IntegerField()
#    real_payoff = models.FloatField()
#    payoff_2 = models.FloatField()
    contribution = models.IntegerField(
        min=0, max=Constants.endowment, label="Ihr Beitrag zum Projekt:"
    )
    claim = models.IntegerField(
        min=0, max=Constants.endowment, label="Ihre Entnahme aus dem Projekt:"
    )



# FUNCTIONS
def set_payoffs(group: Group):
    players = group.get_players()

    contributions = [p.contribution for p in players]
    group.total_contribution = sum(contributions)

    claims = [p.claim for p in players]
    group.total_claim = sum(claims)

    group.individual_share = (
            (group.total_contribution - group.total_claim) * Constants.multiplier                 #wenn mit Spieleranzahl, dann noch "/ Constants.players_per_group" dahinter
    )

    for p in players:
        p.payoff = Constants.beginningloss + Constants.endowment - p.contribution + p.claim + group.individual_share

        p.personal_income = (Constants.beginningloss + Constants.endowment - p.contribution + p.claim)






# PAGES

class Instructions_1(Page):
    @staticmethod
    def is_displayed(player):
        return player.round_number == 1

class Instructions_2(Page):
    @staticmethod
    def is_displayed(player):
        return player.round_number == 1

class Instructions_3(Page):
    @staticmethod
    def is_displayed(player):
        return player.round_number == 1

class Instructions_4(Page):
    @staticmethod
    def is_displayed(player):
        return player.round_number == 1

class Contribute(Page):
    form_model = 'player'
    form_fields = ['contribution', 'claim']


class ResultsWaitPage(WaitPage):
    after_all_players_arrive = set_payoffs

class Info_Page(Page):
    pass

class Income_Page(Page):
    pass

class Results(Page):
    pass


page_sequence = [Instructions_1, Instructions_2, Instructions_3, Instructions_4, Contribute, ResultsWaitPage, Results]
#page_sequence = [Contribute, ResultsWaitPage, Info_Page, Income_Page]
