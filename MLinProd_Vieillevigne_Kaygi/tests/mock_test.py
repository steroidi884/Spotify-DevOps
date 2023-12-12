import unittest
from unittest.mock import patch
from flask import Flask
from flask_testing import TestCase
import MLinProd_Vieillevigne_Kaygi.app
class TestAppWithMocks(TestCase):
    def create_app(self):
        app.app.config['TESTING'] = True
        return app.app

    @patch('app.pd.read_csv')
    @patch('app.update_csv')
    def test_add_suggestion_with_mock(self, mock_update_csv, mock_read_csv):
        # Configure le mock pour lire un CSV existant
        mock_read_csv.return_value = app.pd.DataFrame(columns=['Artiste', 'Titre'])

        # Test d'ajout d'une suggestion avec mock
        data = {'artiste': 'Nouvel Artiste', 'musique': 'Nouvelle Musique'}
        response = self.client.post('/add', data=data, follow_redirects=True)
        self.assert200(response)
        self.assertIn(b'Nouvel Artiste', response.data)
        self.assertIn(b'Nouvelle Musique', response.data)

        # Vérifie que la fonction de mise à jour a été appelée
        mock_update_csv.assert_called_once()

if __name__ == '__main__':
    unittest.main()
