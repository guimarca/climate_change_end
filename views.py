from . import models
from ._builtin import Page, WaitPage
from otree.api import Currency as c, currency_range
from .models import Constants



class ResultsFinal(Page):
    """Players payoff: How much each has earned"""

    def vars_for_template(self):
        self.player.set_payoffs()

        if self.player.prevention == 0:
            prev_text = 'No'
        else:
            prev_text = 'Sí'

        return {
            'prevention_amount_reached': prev_text,
            'P': ('%.2f' % (self.player.P)).replace(',', '.'),
            'tau': ('%.2f' % (self.player.tau)).replace(',', '.'),
            'prevention_fund': ('%.2f' % (self.player.prevention_fund)).replace(',', '.'),
            'pctg_catastrophe': ('%.2f' % (self.player.P * 100)).replace(',', '.'),
            'pctg_no_catastrophe': ('%.2f' % ((1-self.player.P) * 100)).replace(',', '.'),
            'random_catastrophe': ('%.2f' % round(self.player.random_catastrophe, 2)).replace(',', '.')
        }


class Demographics(Page):
    form_model = models.Player
    form_fields = [
        'q_age',
        'q_gender',
        'q_country',
        'q_study',
        'q_comments'
    ]

page_sequence = [
    ResultsFinal,
    Demographics
]
