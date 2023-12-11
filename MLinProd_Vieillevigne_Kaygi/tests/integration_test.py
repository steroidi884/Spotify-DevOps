import unittest
from flask import Flask
from flask_testing import TestCase
import app

class TestApp(TestCase):
    def create_app(self):
        app.app.config['TESTING'] = True
        return app.app

    def test_index_route(self):
        response = self.client.get('/')
        self.assert200(response)
        self.assertTemplateUsed('suggestions.html')

    def test_add_suggestion(self):
        # Test d'ajout d'une suggestion
        data = {'artiste': 'Nouvel Artiste', 'musique': 'Nouvelle Musique'}
        response = self.client.post('/add', data=data, follow_redirects=True)
        self.assert200(response)
        self.assertIn(b'Nouvel Artiste', response.data)
        self.assertIn(b'Nouvelle Musique', response.data)

    def test_update_suggestion(self):
        # Test de mise à jour d'une suggestion
        data = {'artiste': 'Artiste Modifié', 'musique': 'Musique Modifiée'}
        response = self.client.post('/update/0', data=data, follow_redirects=True)
        self.assert200(response)
        self.assertIn(b'Artiste Modifié', response.data)
        self.assertIn(b'Musique Modifiée', response.data)

    def test_delete_suggestion(self):
        # Test de suppression d'une suggestion
        response = self.client.post('/delete/0', follow_redirects=True)
        self.assert200(response)
        self.assertNotIn(b'Artiste Modifié', response.data)  # Assurez-vous que la suggestion a été supprimée

if __name__ == '__main__':
    unittest.main()
