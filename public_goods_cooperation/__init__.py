from otree.api import *



class Constants(BaseConstants):
    name_in_url = 'public_goods_cooperation'
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
    individual_share = models.FloatField()


class Player(BasePlayer):
    personal_income = models.IntegerField()
    kepttoken_income = models.IntegerField()
#    real_payoff = models.FloatField()
#    payoff_2 = models.FloatField()
    contribution = models.IntegerField(
        min=0, max=Constants.endowment, label="Ihr Beitrag zum Projekt:"
    )
    expectation1 = models.IntegerField(
        min=0, max=(Constants.players_per_group - 1) * Constants.endowment, label='</br><b>Ihre Schätzungen (in Wertmarken)</b></br></br>Summe der Beiträge aller anderen Gruppenmitglieder:</p>'
    )

    expectation2 = models.IntegerField(
        min=0, max=Constants.endowment, label="Der niedrigste Beitrag der anderen Gruppenmitglieder:"
    )

    expectation3 = models.IntegerField(
        min=0, max=Constants.endowment, label="Der höchste Beitrag der anderen Gruppenmitglieder:"
    )

    contribution_pct_p1 = models.FloatField()
    contribution_pct_p2 = models.FloatField()
    contribution_pct_p3 = models.FloatField()
    contribution_pct_p4 = models.FloatField()

    contribution_p1 = models.IntegerField()
    contribution_p2 = models.IntegerField()
    contribution_p3 = models.IntegerField()
    contribution_p4 = models.IntegerField()

#    payoffs = models.CurrencyField()
    payoff_1 = models.CurrencyField(initial=0)
    payoff_2 = models.CurrencyField(initial=0)
    payoff_3 = models.CurrencyField(initial=0)
    payoff_4 = models.CurrencyField(initial=0)

    p_payoff_1 = models.CurrencyField(initial=0)
    p_payoff_2 = models.CurrencyField(initial=0)
    p_payoff_3 = models.CurrencyField(initial=0)
    p_payoff_4 = models.CurrencyField(initial=0)

    contribution_others = models.FloatField()

# FUNCTIONS
def set_payoffs(group: Group):
    players = group.get_players()
    contributions = [p.contribution for p in players]
#    payoffs = [p.payoff for p in players]
    group.total_contribution = sum(contributions)
    group.individual_share = (
        group.total_contribution * Constants.multiplier                 #wenn mit Spieleranzahl, dann noch "/ Constants.players_per_group" dahinter
    )

    for p in players:
        p.payoff = Constants.beginningloss + Constants.endowment - p.contribution + group.individual_share
#        p.payoff = format(float(p.payoff / 10), '.2f')
#        p.participant.payoff = format(float(p.participant.payoff / 10), '.2f')
        p.personal_income = (Constants.beginningloss + Constants.endowment - p.contribution)
        p.kepttoken_income = (Constants.endowment - p.contribution)
        p.contribution_p1 = contributions[0]
        p.contribution_p2 = contributions[1]
        p.contribution_p3 = contributions[2]
        p.contribution_p4 = contributions[3]
        p.contribution_pct_p1 = contributions[0] / Constants.endowment
        p.contribution_pct_p2 = contributions[1] / Constants.endowment
        p.contribution_pct_p3 = contributions[2] / Constants.endowment
        p.contribution_pct_p4 = contributions[3] / Constants.endowment
        p.contribution_others = group.total_contribution - p.contribution

    payoffs = [p.payoff for p in players]                                  #nur für Runden-PayOff
    for p in players:
        p.payoff_1 = p.payoff_1 + payoffs[0]
        p.payoff_2 = p.payoff_2 + payoffs[1]
        p.payoff_3 = p.payoff_3 + payoffs[2]
        p.payoff_4 = p.payoff_4 + payoffs[3]

    participant_payoffs = [p.participant.payoff for p in players]          #für gesamtes PayOff im Spiel
    for p in players:
        p.p_payoff_1 = participant_payoffs[0]
        p.p_payoff_2 = participant_payoffs[1]
        p.p_payoff_3 = participant_payoffs[2]
        p.p_payoff_4 = participant_payoffs[3]



#    p.payoff_2 = p.payoff
#    p.real_payoff = p.payoff_2 * 0.2                                      #je nachdem, wie hoch "real_world_currency_per_point" in settings.py ist

#    p.payoff_end = 40 - (p.payoff * 0.02)




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
    form_fields = ['contribution', 'expectation1','expectation2','expectation3']


class ResultsWaitPage(WaitPage):
    after_all_players_arrive = set_payoffs

class Info_Page(Page):
    pass

class Income_Page(Page):
    pass

class Results(Page):
    pass


page_sequence = [Instructions_1, Instructions_2, Instructions_3, Instructions_4, Contribute, ResultsWaitPage, Info_Page, Income_Page]
#page_sequence = [Contribute, ResultsWaitPage, Info_Page, Income_Page]
