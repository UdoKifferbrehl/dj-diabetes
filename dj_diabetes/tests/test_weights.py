# coding: utf-8
from datetime import datetime

from dj_diabetes.forms.base import WeightsForm
from dj_diabetes.models.weights import Weights
from dj_diabetes.tests import MainTest


class WeightsTest(MainTest):

    def setUp(self):
        super(WeightsTest, self).setUp()

        user = self.user
        weight = 80
        date_weights = datetime.now()
        self.weights = Weights.objects.create(user=user,
                                              weight=weight,
                                              date_weights=date_weights)

    def test_weights(self):
        self.assertTrue(isinstance(self.weights, Weights))
        self.assertEqual(self.weights .__str__(), "%s (date: %s)" %
                         (self.weights .weight, self.weights .date_weights))

    def test_valid_form(self):
        data = {'weight': 80, 'date_weights': datetime.now()}
        initial = {'user': self.user}
        form = WeightsForm(data=data, initial=initial)
        self.assertTrue(form.is_valid())

    def test_invalid_form(self):
        form = WeightsForm()
        self.assertFalse(form.is_valid())
