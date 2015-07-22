from django import test
from django.core.urlresolvers import reverse


class SpeakerTests(test.TestCase):

    def test_list_all_speakers(self):
        response = self.client.get(reverse('api:speakers_list'))
        self.assertEqual(200, response.status_code)
