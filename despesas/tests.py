from datetime import datetime
from time import strftime
from rest_framework.test import APITestCase


class TestGetAllDespesas(APITestCase):
    URL = "/api/v1/despesas/"
    
    def test_should_be_return_all_values_in_despesas(self):
        data = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.client.post(self.URL, data={
            "descricao": "Primeira despesa", "valor": 1250.00, "data": data
        })
        response = self.client.get(self.URL, format='json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data[0]["id"], 1)
        self.assertEqual(response.data[0]["descricao"], "Primeira despesa")
        self.assertEqual(response.data[0]["valor"], 1250.00)
        self.assertEqual(response.data[0]["data"].replace("T", " ").replace("Z", ""), data)
    


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
        self.client.post(self.URL, data={
            "descricao": "Primeira despesa", "valor": 1250.00, "data": "2022-08-11 20:18:50"
        })
        response = self.client.post(self.URL, data={
            "descricao": "Primeira despesa", "valor": 2500.00, "data": "2022-08-12 20:18:50"
        })
        value = {"error": "Dados não inseridos com sucesso!"}
        self.assertEqual(value, response.data)
        self.assertEqual(response.status_code, 400)


class TestDespesasGetByID(APITestCase):
    URL = "/api/v1/despesas/"
        
    def test_should_be_get_despesas_by_id(self):
        data = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.client.post(self.URL, data={
            "descricao": "Primeira despesa", "valor": 1250.00, "data": data
        })
        response = self.client.get(self.URL + "1/", format='json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data["id"], 1)
        self.assertEqual(response.data["descricao"], "Primeira despesa")
        self.assertEqual(response.data["valor"], 1250.00)
        self.assertEqual(response.data["data"].replace("T", " ").replace("Z", ""), data)
    
    
    def test_should_return_error(self):
        response = self.client.get(self.URL + "1/", format='json')
        self.assertEqual({"error": "Não há dados cadastrados para o id: 1!"}, response.data)


class TestDelete(APITestCase):
    URL = "/api/v1/despesas/"
    
    def test_should_be_delete_and_return_value(self):
        data = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.client.post(self.URL, data={
            "descricao": "Primeira despesa", "valor": 1250.00, "data": data
        })
        response = self.client.delete(self.URL + "1/", format='json')
        self.assertEqual({"message": "Dados deletados com sucesso!"}, response.data)

    
    def test_should_be_delete_return_error(self):
        response = self.client.delete(self.URL + "1/", format='json')
        self.assertEqual({"error": "Dados não encontrados para id: 1!"}, response.data)


class TestUpdate(APITestCase):
    URL = "/api/v1/despesas/"
    
    def test_should_be_return_error(self):
        response = self.client.put(self.URL + "1/", data={
            "id": 1, "descricao": "Primeira despesa", "valor": 1250.00, "data": "2022-08-24 20:46:55"
        })
        self.assertEqual({"error": "Dados não encontrados para id: 1!"}, response.data)
        
    
    def test_should_be_update_and_return_value(self):
        data = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.client.post(self.URL, data={
            "descricao": "Primeira despesa", "valor": 1250.00, "data": data
        })
        response = self.client.put(self.URL + "1/", data={
            "id": 1, "categoria": "Outras", "descricao": "Primeira despesa", "valor": 1250.00, "data": "2022-08-24 20:46:55"
        })
        self.assertEqual({"message": "Dados atualizados com sucesso!"}, response.data)