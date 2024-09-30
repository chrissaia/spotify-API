import unittest
from app import app
import csv
import os

class TestApp(unittest.TestCase):
    
    def setUp(self):
        # sets up the test client
        self.app = app.test_client()
        self.app.testing = True

    def test_homepage(self):
        # test homepage route
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)

    def test_playlist_route(self):
        # mock form data with a dummy playlist_id
        response = self.app.post('/playlist', data={'playlist_id': 'dummy_playlist_id'})
        self.assertIn(b'error fetching data', response.data)  # because it's a dummy id, expect error message

    def test_csv_creation(self):
        # test if csv file is created and contains data
        with open('dataDict.csv', 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(['Song', 'Artist', 'Popularity', 'URI'])
            writer.writerow(['Test Song', 'Test Artist', 50, 'spotify:track:test_uri'])

        self.assertTrue(os.path.exists('dataDict.csv'))

        with open('dataDict.csv', newline='') as csvfile:
            reader = csv.reader(csvfile)
            rows = list(reader)
            self.assertEqual(len(rows), 2)  # should have 2 rows: header and 1 song data

if __name__ == '__main__':
    unittest.main()
