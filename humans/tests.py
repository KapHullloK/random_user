from django.test import TestCase
from django.urls import reverse
from unittest.mock import patch, Mock

from humans.data_for_mocking import random_user_api_json
from humans.services import get_random_humans

from humans.models import Human


class HumansTestCase(TestCase):

    def setUp(self):
        self.human1 = Human.objects.create(
            first_name=f"Name{1}",
            last_name=f"Last{1}",
            gender="male",
            email=f"user{1}@example.com"
        )
        self.human2 = Human.objects.create(
            first_name=f"Name{2}",
            last_name=f"Last{2}",
            gender="female",
            email=f"user{2}@example.com"
        )

    def test_HomeView(self):
        response = self.client.get(reverse("humans:home-humans"))

        self.assertEqual(response.status_code, 200)

    def test_HumansListView_with_count_param(self):
        response = self.client.get(reverse("humans:list-humans"), {"count": 5})

        self.assertEqual(len(response.context["humans"]), 5)

    def test_HumanDetailView(self):
        response = self.client.get(reverse("humans:detail-humans", args=[self.human1.id]))

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context["human"], self.human1)

    def test_RandomHumanDetailView(self):
        response = self.client.get(reverse("humans:random-humans"))

        self.assertEqual(response.status_code, 200)
        self.assertTrue("human" in response.context)


class GetRandomHumansTestCase(TestCase):

    @patch('humans.services.requests.get')
    def test_get_random_humans(self, mock_get):
        mock_response = Mock()
        mock_response.json.return_value = random_user_api_json

        mock_response.status_code = 200
        mock_get.return_value = mock_response

        result = get_random_humans(2)

        self.assertEqual(len(result), 2)
        self.assertEqual(result[0]['name']['first'], 'Bently')
        self.assertEqual(result[1]['name']['first'], 'Jared')

        mock_get.assert_called_once()
