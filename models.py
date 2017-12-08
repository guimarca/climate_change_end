'''
from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)
import random
'''
from __future__ import division
from otree.db import models
from otree.constants import BaseConstants
from otree.models import BaseSubsession, BaseGroup, BasePlayer, BaseLink

from otree import widgets
from otree.common import Currency as c, currency_range
import random

from django_countries.fields import CountryField


doc = """
Climate change game a la Milinski + competition final payoffs screen
"""


class Constants(BaseConstants):
    name_in_url = 'climate_change_end'
    players_per_group = None
    num_rounds = 1



class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass



class Player(BasePlayer):
    prevention = models.IntegerField(initial=1)
    catastrophe = models.IntegerField(initial=0)

    prevention_fund = models.IntegerField(initial=0)
    private_fund = models.IntegerField(initial=0)

    tau = 0

    P = models.FloatField()
    random_catastrophe = models.FloatField()

    q_age = models.PositiveIntegerField(verbose_name='¿Qué edad tienes?',
                                        choices=range(18, 125),
                                        initial=None)
    q_gender = models.CharField(initial=None,
                                choices=['Hombre', 'Mujer', 'Otro', 'No quiero especificarlo'],
                                verbose_name='¿Cuál es tu sexo?',
                                widget=widgets.RadioSelect())
    q_country = CountryField(verbose_name='¿Qué nacionalidad tienes?')
    q_study = models.TextField(verbose_name='¿Qué estudios tienes/estás cursando?')
    q_comments = models.TextField(verbose_name="Por favor, deja tus comentarios sobre el experimento")

    def set_payoffs(self):
        self.tau = self.participant.vars.get('tau')
        self.P = self.participant.vars.get('P')
        self.random_catastrophe = self.participant.vars.get('random_catastrophe')
        self.prevention_fund = self.participant.vars.get('prevention_fund')
        self.private_fund = self.participant.vars.get('private_fund')
        self.payoff = self.participant.vars.get('payoff')
        self.prevention = self.participant.vars.get('prevention')
        self.catastrophe = self.participant.vars.get('catastrophe')



class Link(BaseLink):
    pass