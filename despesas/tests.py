from datetime import datetime
from rest_framework.test import APITestCase


class TestGetAllDespesas(APITestCase):
    URL = "/api/v1/despesas/"
    
    def test_should_be_return_all_values_in_despesas(self):
        data = datetime.now()
        self.client.post(self.URL, data={
            "descricao": "Primeira despesa", "valor": 1250.00, "data": data
        })
        response = self.client.get(self.URL, format='json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, {
            "id": 1, "descricao": "Primeira despesa", "valor": 1250.00, "data": data
        })
    


class TestCreateDespesas(APITestCase):
    URL = "/api/v1/despesas/"
    
    def test_should_be_create_despessa_and_return_status_code_and_message_ok(self):
        data = datetime.now()
        value = {"message": "Dados inseridos com sucesso!"}
        response = self.client.post(self.URL, data={
            "descricao": "Primeira despesa", "valor": 1250.00, "data": data
        })
        self.assertEqual(value, response.data)
        self.assertEqual(response.status_code, 200)
        
    
    def test_should_be_return_error_duplicate_data(self):
        data = datetime.now()
        self.client.post(self.URL, data={
            "descricao": "Primeira despesa", "valor": 1250.00, "data": data
        })
        response = self.client.post(self.URL, data={
            "descricao": "Primeira despesa", "valor": 2500.00, "data": data
        })
        value = {"error": "Dados não inseridos com sucesso!"}
        self.assertEqual(value, response.data)
        self.assertEqual(response.status_code, 400)
