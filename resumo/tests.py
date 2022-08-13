from rest_framework.test import APITestCase



class TestResumo(APITestCase):
    URL = "/api/v1/resumo/"
    
    def test_should_be_return_values_by_ano_and_mes(self):
        self.insert_data()
        value = self.get_value()
        response = self.client.get(self.URL + "2022/08", format='json')
        self.assertEqual(value, response.data)
    
    
    def get_value(self):
        return {
            "total receitas": 1200.0,
            "total despesas": 1200.0,
            "saldo final": 0.0,
            "total gasto por categoria": {
                "Alimentação": 400.0,
                "Saúde": 400.0,
                "Moradia": 0.0,
                "Transporte": 0.0,
                "Educação": 400.0,
                "Lazer": 0.0,
                "Imprevistos": 0.0,
                "Outras": 0.0
            }
        }
    
    
    def insert_data(self):
        self.client.post("/api/v1/despesas/", data={
            "categoria": "Alimentação", "descricao": "Primeira despesa", "valor": 200.00, "data": "2022-08-12 17:20:55"
        })
        self.client.post("/api/v1/receitas/", data={
            "descricao": "Primeira receita", "valor": 200.00, "data": "2022-08-12 17:20:55"
        })
        self.client.post("/api/v1/despesas/", data={
            "categoria": "Alimentação", "descricao": "Segunda despesa", "valor": 200.00, "data": "2022-08-12 17:20:55"
        })
        self.client.post("/api/v1/receitas/", data={
            "descricao": "Segunda receita", "valor": 200.00, "data": "2022-08-12 17:20:55"
        })
        self.client.post("/api/v1/despesas/", data={
            "categoria": "Saúde", "descricao": "Terceira despesa", "valor": 200.00, "data": "2022-08-12 17:20:55"
        })
        self.client.post("/api/v1/receitas/", data={
            "descricao": "Terceita receita", "valor": 200.00, "data": "2022-08-12 17:20:55"
        })
        self.client.post("/api/v1/despesas/", data={
            "categoria": "Saúde", "descricao": "Quarta despesa", "valor": 200.00, "data": "2022-08-12 17:20:55"
        })
        self.client.post("/api/v1/receitas/", data={
            "descricao": "Quarta receita", "valor": 200.00, "data": "2022-08-12 17:20:55"
        })
        self.client.post("/api/v1/despesas/", data={
            "categoria": "Educação", "descricao": "Quinta despesa", "valor": 200.00, "data": "2022-08-12 17:20:55"
        })
        self.client.post("/api/v1/receitas/", data={
            "descricao": "Quinta receita", "valor": 200.00, "data": "2022-08-12 17:20:55"
        })
        self.client.post("/api/v1/despesas/", data={
            "categoria": "Educação", "descricao": "Sexta despesa", "valor": 200.00, "data": "2022-08-12 17:20:55"
        })
        self.client.post("/api/v1/receitas/", data={
            "descricao": "Sexta receita", "valor": 200.00, "data": "2022-08-12 17:20:55"
        })
    
    
    def get_data(self) -> dict:
        return {
            "total receitas": 1200.00,
            "total despesas": 1200.00,
            "saldo final": 0.00,
            "total gasto por categoria": {
                "Alimentação": 400.00,
                "Saúde": 400.00,
                "Moradia": 0.00,
                "Transporte": 0.00,
                "Educação": 400.00,
                "Lazer": 0.00,
                "Imprevistos": 0.00,
                "Outras": 0.00
            }
        }
