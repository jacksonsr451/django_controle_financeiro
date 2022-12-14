from datetime import datetime
from rest_framework.test import APITestCase


class TestGetAllReceitas(APITestCase):
    URL = "/api/v1/receitas/"
    
    def test_should_be_return_all_values_in_receitas(self):
        data = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.client.post(self.URL, data={
            "descricao": "Primeira receita", "valor": 1250.00, "data": data
        })
        response = self.client.get(self.URL, format='json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data[0]["id"], 1)
        self.assertEqual(response.data[0]["descricao"], "Primeira receita")
        self.assertEqual(response.data[0]["valor"], 1250.00)
        self.assertEqual(response.data[0]["data"].replace("T", " ").replace("Z", ""), data)
    
    def test_should_be_return_error(self):
        response = self.client.get(self.URL, format='json')
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.data, {"error": "Não há dados cadastrados!"})

    
    def test_should_be_filter_by_descicao(self):
        data = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.client.post(self.URL, data={
            "descricao": "Primeira receita", "valor": 1250.00, "data": data
        })
        self.client.post(self.URL, data={
            "descricao": "Segunda receita", "valor": 1250.00, "data": data
        })
        self.client.post(self.URL, data={
            "descricao": "Terceira receita", "valor": 1250.00, "data": data
        })
        response = self.client.get(self.URL + "?descricao=Primeira", format='json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 1)
    

class TestCreateReceitas(APITestCase):
    URL = "/api/v1/receitas/"
    
    def test_should_be_create_despessa_and_return_status_code_and_message_ok(self):
        data = datetime.now()
        value = {"message": "Dados inseridos com sucesso!"}
        response = self.client.post(self.URL, data={
            "descricao": "Primeira receita", "valor": 1250.00, "data": data
        })
        self.assertEqual(value, response.data)
        self.assertEqual(response.status_code, 200)
        
    
    def test_should_be_return_error_duplicate_data(self):
        self.client.post(self.URL, data={
            "descricao": "Primeira receita", "valor": 1250.00, "data": "2022-08-11 20:18:50"
        })
        response = self.client.post(self.URL, data={
            "descricao": "Primeira receita", "valor": 2500.00, "data": "2022-08-12 20:18:50"
        })
        value = {"error": "Dados não inseridos com sucesso!"}
        self.assertEqual(value, response.data)
        self.assertEqual(response.status_code, 400)


class TestReceitasGetByID(APITestCase):
    URL = "/api/v1/receitas/"
        
    def test_should_be_get_receitas_by_id(self):
        data = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.client.post(self.URL, data={
            "descricao": "Primeira receita", "valor": 1250.00, "data": data
        })
        response = self.client.get(self.URL + "1/", format='json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data["id"], 1)
        self.assertEqual(response.data["descricao"], "Primeira receita")
        self.assertEqual(response.data["valor"], 1250.00)
        self.assertEqual(response.data["data"].replace("T", " ").replace("Z", ""), data)
    
    
    def test_should_return_error(self):
        response = self.client.get(self.URL + "1/", format='json')
        self.assertEqual({"error": "Não há dados cadastrados para o id: 1!"}, response.data)


class TestDelete(APITestCase):
    URL = "/api/v1/receitas/"
    
    def test_should_be_delete_and_return_value(self):
        data = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.client.post(self.URL, data={
            "descricao": "Primeira receita", "valor": 1250.00, "data": data
        })
        response = self.client.delete(self.URL + "1/", format='json')
        self.assertEqual({"message": "Dados deletados com sucesso!"}, response.data)

    
    def test_should_be_delete_return_error(self):
        response = self.client.delete(self.URL + "1/", format='json')
        self.assertEqual({"error": "Dados não encontrados para id: 1!"}, response.data)


class TestUpdate(APITestCase):
    URL = "/api/v1/receitas/"
    
    def test_should_be_return_error(self):
        response = self.client.put(self.URL + "1/", data={
            "id": 1, "descricao": "Primeira receita", "valor": 1250.00, "data": "2022-08-24 20:46:55"
        })
        self.assertEqual({"error": "Dados não encontrados para id: 1!"}, response.data)
        
    
    def test_should_be_update_and_return_value(self):
        data = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.client.post(self.URL, data={
            "descricao": "Primeira receita", "valor": 1250.00, "data": data
        })
        response = self.client.put(self.URL + "1/", data={
            "id": 1, "descricao": "Primeira receita", "valor": 1250.00, "data": "2022-08-24 20:46:55"
        })
        self.assertEqual({"message": "Dados atualizados com sucesso!"}, response.data)
        

class TestFilterByAnoAndMes(APITestCase):
    URL = "/api/v1/receitas/"
    
    
    def test_should_be_return_list_by_ano_and_mes(self):
        self.add_values_id_db()
        response = self.client.get(self.URL + "2022/01/", format='json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 1)
        
        

    def add_values_id_db(self) -> None:
        self.client.post(self.URL, data={
            "descricao": "Primeira receita de agosto", "valor": 1250.00, "data": "2022-08-13 15:25:55"
        })
        self.client.post(self.URL, data={
            "descricao": "Primeira receita de julho", "valor": 1250.00, "data": "2022-07-13 15:25:55"
        })
        self.client.post(self.URL, data={
            "descricao": "Segunda receita de julho", "valor": 1250.00, "data": "2022-07-13 15:25:55"
        })
        self.client.post(self.URL, data={
            "descricao": "Primeira receita de janeiro", "valor": 1250.00, "data": "2022-01-13 15:25:55"
        })
        
    
    def test_should_be_return_message_error(self):
        response = self.client.get(self.URL + "2022/01/", format='json')
        self.assertEqual(response.data, {"error": "Não há dados neste periodo de ano: 2022 e mês: 01."})