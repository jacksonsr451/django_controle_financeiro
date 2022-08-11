from rest_framework.test import APITestCase


class TestGetAllDespesas(APITestCase):
    URL = "/api/v1/despesas/"
    
    def test_true(self):
        response = self.client.get(self.URL, format='json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, {"message": "ok"})
    
