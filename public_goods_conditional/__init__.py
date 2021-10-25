from otree.api import *


class Constants(BaseConstants):
    name_in_url = 'public_goods_conditional'
    players_per_group = 4
    num_rounds = 2
    endowment = cu(20)
    multiplier = 1.8


class Subsession(BaseSubsession):
    pass

class Group(BaseGroup):
    total_contribution = models.CurrencyField()
    individual_share = models.CurrencyField()
    contribution_average = models.CurrencyField()


class Player(BasePlayer):

    #Eingabe unconditional Endowments
    contribution = models.CurrencyField(
        min=0, max=Constants.endowment, label="Ihr unabhängiger Beitrag zu dem Projekt:"
    )

    # Eingabe conditional Endowments

    # Nebeneinander mit CSS (funktioniert leider nur mit dem Text und nicht mit dem Feld dahinter)
    # -> Absatz zwischen Text und Feld muss verhindert werden:

    #contribution0 = models.CurrencyField(
    #    min=0, max=Constants.endowment, label="<table style='line-height: 200%'><tr><td>0"
    #)
    #contribution1 = models.CurrencyField(
    #    min=0, max=Constants.endowment, label="</td><td>1</td></tr>"
    #)
    #contribution2 = models.CurrencyField(
    #    min=0, max=Constants.endowment, label="<tr><td>2</td>"
    #)
    #contribution3 = models.CurrencyField(
    #    min=0, max=Constants.endowment, label="<td>3</td></tr></table>"

    contribution0 = models.CurrencyField(
        min=0, max=Constants.endowment, label="0"
    )
    contribution1 = models.CurrencyField(
        min=0, max=Constants.endowment, label="1"
    )
    contribution2 = models.CurrencyField(
        min=0, max=Constants.endowment, label="2"
    )
    contribution3 = models.CurrencyField(
        min=0, max=Constants.endowment, label="3"
    )
    contribution4 = models.CurrencyField(
        min=0, max=Constants.endowment, label="4"
    )
    contribution5 = models.CurrencyField(
        min=0, max=Constants.endowment, label="5"
    )
    contribution6 = models.CurrencyField(
        min=0, max=Constants.endowment, label="6"
    )
    contribution7 = models.CurrencyField(
        min=0, max=Constants.endowment, label="7"
    )
    contribution8 = models.CurrencyField(
        min=0, max=Constants.endowment, label="8"
    )
    contribution9 = models.CurrencyField(
        min=0, max=Constants.endowment, label="9"
    )
    contribution10 = models.CurrencyField(
        min=0, max=Constants.endowment, label="10"
    )
    contribution11 = models.CurrencyField(
        min=0, max=Constants.endowment, label="11"
    )
    contribution12 = models.CurrencyField(
        min=0, max=Constants.endowment, label="12"
    )
    contribution13 = models.CurrencyField(
        min=0, max=Constants.endowment, label="13"
    )
    contribution14 = models.CurrencyField(
        min=0, max=Constants.endowment, label="14"
    )
    contribution15 = models.CurrencyField(
        min=0, max=Constants.endowment, label="15"
    )
    contribution16 = models.CurrencyField(
        min=0, max=Constants.endowment, label="16"
    )
    contribution17 = models.CurrencyField(
        min=0, max=Constants.endowment, label="17"
    )
    contribution18 = models.CurrencyField(
        min=0, max=Constants.endowment, label="18"
    )
    contribution19 = models.CurrencyField(
        min=0, max=Constants.endowment, label="19"
    )
    contribution20 = models.CurrencyField(
        min=0, max=Constants.endowment, label="20"
    )



#    time_pressure = models.BooleanField()

    # Random ID zuweisen

    #random_id = models.IntegerField()

#def creating_session(self):
#    for p in self.get_players():
#        from random import randrange
#        p.random_id = randrange(3)



# FUNCTIONS


def set_payoffs(group: Group):                                  #(contribution_average=float, payoff=float)
    # Zufalls-Spieler wird ausgewählt
    # random_player = random(group.get_players())
    # rest_players = 'Jeder Spieler außer random_player'
    # ODER: erst

    #evtl. so:

    #random_player = get_player_by_id(p.random_id)


    # Durchschnitt der unconditional Endowments der übrigen Spieler wird berechnet und gerundet
    # contributions_rest = [p.contribution for p in rest_players]
    # group.average_rest_players = sum(contributions_rest)
    # group.average_rest_players_round = round(group.average_rest_players)

    # Auszahlung -> normaler PGG Algorithmus mit gerundetem Durchschnitt als gewähltes conditional Endowment des Zufalls-Spielers

    #   if group.average_rest_players_round = 1:
    #       contribution_random_player = 1
    #   else:
    #       if group.average_rest_players_round = 2:
    #           contribution_random_player = 2
    #           else:
    #              if group.average_rest_players_round = 3:
    #               contribution_random_player = 3
    #              else:
    #               contribution_random_player = 0

    # group.total_contribution = sum(p.contribution for p in rest_players) + contribution_random_player

    p1 = group.get_player_by_id(1)
    p2 = group.get_player_by_id(2)
    p3 = group.get_player_by_id(3)
    p4 = group.get_player_by_id(4)


    group.contribution_average = round((p2.contribution + p3.contribution + p4.contribution) / 3)
    #group.contribution_average = round(contribution_average)



    if group.contribution_average == 0:
        group.individual_share = Constants.multiplier * ((p1.contribution0 + p2.contribution + p3.contribution + p4.contribution) / 4)
        p1.payoff = Constants.endowment - p1.contribution0 + group.individual_share      # <-- für den Fall, dass der payoff von P1 ebenfalls mit seiner
        p2.payoff = Constants.endowment - p2.contribution + group.individual_share       # abhängigen Contribution gerechnet wird (wie auch der group_individual_share),
        p3.payoff = Constants.endowment - p3.contribution + group.individual_share       # ansonsten einfach mit - p1.contribution statt - p1.contribution0
        p4.payoff = Constants.endowment - p4.contribution + group.individual_share

    elif group.contribution_average == 1:
        group.individual_share = Constants.multiplier * ((p1.contribution1 + p2.contribution + p3.contribution + p4.contribution) / 4)
        p1.payoff = Constants.endowment - p1.contribution1 + group.individual_share
        p2.payoff = Constants.endowment - p2.contribution + group.individual_share
        p3.payoff = Constants.endowment - p3.contribution + group.individual_share
        p4.payoff = Constants.endowment - p4.contribution + group.individual_share

    elif group.contribution_average == 2:
        group.individual_share = Constants.multiplier * ((p1.contribution2 + p2.contribution + p3.contribution + p4.contribution) / 4)
        p1.payoff = Constants.endowment - p1.contribution2 + group.individual_share
        p2.payoff = Constants.endowment - p2.contribution + group.individual_share
        p3.payoff = Constants.endowment - p3.contribution + group.individual_share
        p4.payoff = Constants.endowment - p4.contribution + group.individual_share

    elif group.contribution_average == 3:
        group.individual_share = Constants.multiplier * ((p1.contribution3 + p2.contribution + p3.contribution + p4.contribution) / 4)
        p1.payoff = Constants.endowment - p1.contribution3 + group.individual_share
        p2.payoff = Constants.endowment - p2.contribution + group.individual_share
        p3.payoff = Constants.endowment - p3.contribution + group.individual_share
        p4.payoff = Constants.endowment - p4.contribution + group.individual_share

    elif group.contribution_average == 4:
        group.individual_share = Constants.multiplier * ((p1.contribution4 + p2.contribution + p3.contribution + p4.contribution) / 4)
        p1.payoff = Constants.endowment - p1.contribution4 + group.individual_share
        p2.payoff = Constants.endowment - p2.contribution + group.individual_share
        p3.payoff = Constants.endowment - p3.contribution + group.individual_share
        p4.payoff = Constants.endowment - p4.contribution + group.individual_share

    elif group.contribution_average == 5:
        group.individual_share = Constants.multiplier * ((p1.contribution5 + p2.contribution + p3.contribution + p4.contribution) / 4)
        p1.payoff = Constants.endowment - p1.contribution5 + group.individual_share
        p2.payoff = Constants.endowment - p2.contribution + group.individual_share
        p3.payoff = Constants.endowment - p3.contribution + group.individual_share
        p4.payoff = Constants.endowment - p4.contribution + group.individual_share

    elif group.contribution_average == 6:
        group.individual_share = Constants.multiplier * ((p1.contribution6 + p2.contribution + p3.contribution + p4.contribution) / 4)
        p1.payoff = Constants.endowment - p1.contribution6 + group.individual_share
        p2.payoff = Constants.endowment - p2.contribution + group.individual_share
        p3.payoff = Constants.endowment - p3.contribution + group.individual_share
        p4.payoff = Constants.endowment - p4.contribution + group.individual_share

    elif group.contribution_average == 7:
        group.individual_share = Constants.multiplier * ((p1.contribution7 + p2.contribution + p3.contribution + p4.contribution) / 4)
        p1.payoff = Constants.endowment - p1.contribution7 + group.individual_share
        p2.payoff = Constants.endowment - p2.contribution + group.individual_share
        p3.payoff = Constants.endowment - p3.contribution + group.individual_share
        p4.payoff = Constants.endowment - p4.contribution + group.individual_share

    elif group.contribution_average == 8:
        group.individual_share = Constants.multiplier * ((p1.contribution8 + p2.contribution + p3.contribution + p4.contribution) / 4)
        p1.payoff = Constants.endowment - p1.contribution8 + group.individual_share
        p2.payoff = Constants.endowment - p2.contribution + group.individual_share
        p3.payoff = Constants.endowment - p3.contribution + group.individual_share
        p4.payoff = Constants.endowment - p4.contribution + group.individual_share

    elif group.contribution_average == 9:
        group.individual_share = Constants.multiplier * ((p1.contribution9 + p2.contribution + p3.contribution + p4.contribution) / 4)
        p1.payoff = Constants.endowment - p1.contribution9 + group.individual_share
        p2.payoff = Constants.endowment - p2.contribution + group.individual_share
        p3.payoff = Constants.endowment - p3.contribution + group.individual_share
        p4.payoff = Constants.endowment - p4.contribution + group.individual_share

    elif group.contribution_average == 10:
        group.individual_share = Constants.multiplier * ((p1.contribution10 + p2.contribution + p3.contribution + p4.contribution) / 4)
        p1.payoff = Constants.endowment - p1.contribution10 + group.individual_share
        p2.payoff = Constants.endowment - p2.contribution + group.individual_share
        p3.payoff = Constants.endowment - p3.contribution + group.individual_share
        p4.payoff = Constants.endowment - p4.contribution + group.individual_share

    elif group.contribution_average == 11:
        group.individual_share = Constants.multiplier * ((p1.contribution11 + p2.contribution + p3.contribution + p4.contribution) / 4)
        p1.payoff = Constants.endowment - p1.contribution11 + group.individual_share
        p2.payoff = Constants.endowment - p2.contribution + group.individual_share
        p3.payoff = Constants.endowment - p3.contribution + group.individual_share
        p4.payoff = Constants.endowment - p4.contribution + group.individual_share

    elif group.contribution_average == 12:
        group.individual_share = Constants.multiplier * ((p1.contribution12 + p2.contribution + p3.contribution + p4.contribution) / 4)
        p1.payoff = Constants.endowment - p1.contribution12 + group.individual_share
        p2.payoff = Constants.endowment - p2.contribution + group.individual_share
        p3.payoff = Constants.endowment - p3.contribution + group.individual_share
        p4.payoff = Constants.endowment - p4.contribution + group.individual_share

    elif group.contribution_average == 13:
        group.individual_share = Constants.multiplier * ((p1.contribution13 + p2.contribution + p3.contribution + p4.contribution) / 4)
        p1.payoff = Constants.endowment - p1.contribution13 + group.individual_share
        p2.payoff = Constants.endowment - p2.contribution + group.individual_share
        p3.payoff = Constants.endowment - p3.contribution + group.individual_share
        p4.payoff = Constants.endowment - p4.contribution + group.individual_share

    elif group.contribution_average == 14:
        group.individual_share = Constants.multiplier * ((p1.contribution14 + p2.contribution + p3.contribution + p4.contribution) / 4)
        p1.payoff = Constants.endowment - p1.contribution14 + group.individual_share
        p2.payoff = Constants.endowment - p2.contribution + group.individual_share
        p3.payoff = Constants.endowment - p3.contribution + group.individual_share
        p4.payoff = Constants.endowment - p4.contribution + group.individual_share

    elif group.contribution_average == 15:
        group.individual_share = Constants.multiplier * ((p1.contribution15 + p2.contribution + p3.contribution + p4.contribution) / 4)
        p1.payoff = Constants.endowment - p1.contribution15 + group.individual_share
        p2.payoff = Constants.endowment - p2.contribution + group.individual_share
        p3.payoff = Constants.endowment - p3.contribution + group.individual_share
        p4.payoff = Constants.endowment - p4.contribution + group.individual_share

    elif group.contribution_average == 16:
        group.individual_share = Constants.multiplier * ((p1.contribution16 + p2.contribution + p3.contribution + p4.contribution) / 4)
        p1.payoff = Constants.endowment - p1.contribution16 + group.individual_share
        p2.payoff = Constants.endowment - p2.contribution + group.individual_share
        p3.payoff = Constants.endowment - p3.contribution + group.individual_share
        p4.payoff = Constants.endowment - p4.contribution + group.individual_share

    elif group.contribution_average == 17:
        group.individual_share = Constants.multiplier * ((p1.contribution17 + p2.contribution + p3.contribution + p4.contribution) / 4)
        p1.payoff = Constants.endowment - p1.contribution17 + group.individual_share
        p2.payoff = Constants.endowment - p2.contribution + group.individual_share
        p3.payoff = Constants.endowment - p3.contribution + group.individual_share
        p4.payoff = Constants.endowment - p4.contribution + group.individual_share

    elif group.contribution_average == 18:
        group.individual_share = Constants.multiplier * ((p1.contribution18 + p2.contribution + p3.contribution + p4.contribution) / 4)
        p1.payoff = Constants.endowment - p1.contribution18 + group.individual_share
        p2.payoff = Constants.endowment - p2.contribution + group.individual_share
        p3.payoff = Constants.endowment - p3.contribution + group.individual_share
        p4.payoff = Constants.endowment - p4.contribution + group.individual_share

    elif group.contribution_average == 19:
        group.individual_share = Constants.multiplier * ((p1.contribution19 + p2.contribution + p3.contribution + p4.contribution) / 4)
        p1.payoff = Constants.endowment - p1.contribution19 + group.individual_share
        p2.payoff = Constants.endowment - p2.contribution + group.individual_share
        p3.payoff = Constants.endowment - p3.contribution + group.individual_share
        p4.payoff = Constants.endowment - p4.contribution + group.individual_share

    elif group.contribution_average == 20:
        group.individual_share = Constants.multiplier * ((p1.contribution20 + p2.contribution + p3.contribution + p4.contribution) / 4)
        p1.payoff = Constants.endowment - p1.contribution20 + group.individual_share
        p2.payoff = Constants.endowment - p2.contribution + group.individual_share
        p3.payoff = Constants.endowment - p3.contribution + group.individual_share
        p4.payoff = Constants.endowment - p4.contribution + group.individual_share


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

class Instructions_5(Page):
    @staticmethod
    def is_displayed(player):
        return player.round_number == 1

class Contribute(Page):
    form_model = 'player'
    form_fields = ['contribution']


class Contribute_conditional(Page):
    form_model = 'player'
    form_fields = ['contribution0', 'contribution1', 'contribution2', 'contribution3', 'contribution4', 'contribution5', 'contribution6', 'contribution7', 'contribution8', 'contribution9', 'contribution10', 'contribution11', 'contribution12', 'contribution13', 'contribution14', 'contribution15', 'contribution16', 'contribution17', 'contribution18', 'contribution19', 'contribution20']
    #after_all_players_arrive = set_random_id

class ResultsWaitPage(WaitPage):
    after_all_players_arrive = set_payoffs


class Results(Page):
    pass


page_sequence = [Instructions_1, Instructions_2, Instructions_3, Instructions_4, Contribute, Instructions_5, Contribute_conditional, ResultsWaitPage]
