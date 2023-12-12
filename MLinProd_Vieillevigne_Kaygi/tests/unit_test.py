import unittest
from unittest.mock import patch
from MLinProd_Vieillevigne_Kaygi.app import update_csv

class TestUpdateCSV(unittest.TestCase):
    @patch('app.pd.DataFrame.to_csv')
    def test_update_csv(self, mock_to_csv):
        # Données de test
        items = [['Artiste1', 'Musique1'], ['Artiste2', 'Musique2']]

        # Appel de la fonction à tester
        update_csv(items)

        # Vérification que la fonction to_csv a été appelée avec les bonnes données
        mock_to_csv.assert_called_once_with('Spotify.csv', index=False)

if __name__ == '__main__':
    unittest.main()
