import unittest
from project import app

class TestApp(unittest.TestCase):
    
    def setUp(self):
        self.client = app.test_client(self)
        test_data = {"email":"jd@myinsuranceapp.com","password":"passwordjd"}
        response = self.client.post('/api/v1/token',content_type='application/json', json=test_data) 
        self.assertEqual(response.status_code, 200)
        data = response.json

        print(f"post token: {data}")
        self.token=data['token']
        self.headers = {"Authorization": f"Bearer {self.token}"}
        
    def test_2_get_restricted(self):
        response = self.client.get('/api/v1/users/', content_type='application/json', headers=self.headers)
        data = response.json
        print(f"get restricted: {data}")
        self.assertLess(0, len(data))
        self.assertIn("address", data[0])
        
    
    def test_2_post(self):
        test_data = {"address": "C Street 1",
                     "email": "jd@myinsuranceapp.com",
                     "fullname": "John Doe",
                     "birthdate": "02.10.2020",
                     "country": "Berlin",
                     "city": "Spain",
                     "password": "poo",}
        response = self.client.post('/api/v1/users/',content_type='application/json',headers=self.headers, json=test_data)
        data=response.json
        print(f"post: {data}")
        self.assertEqual(response.status_code, 200)
        self.assertTrue(data["ok"])

    def test_3_get_none(self):
        response =self.client.post('/api/v1/token', content_type='application/json')
        data=response.json
        print(f"get post 2: {data}")
        self.assertEqual(response.status_code, 400)
        
    def test_4_post_emailmissing(self):
        test_data = {"address": "C Street 1",
                     "fullname": "John Doe",
                     "birthdate": "02.10.2020",
                     "email": "jh@gmail.com",
                     "country": "Berlin",
                     "city": "Spain",
                     "password": "poo",}
        response = self.client.post('/api/v1/users/',content_type='application/json',headers=self.headers, json=test_data)
        data=response.json
        print(f"post: {data}")
        self.assertEqual(response.status_code, 200)