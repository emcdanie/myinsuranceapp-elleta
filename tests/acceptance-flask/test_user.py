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
        self.assertEqual(response.status_code, 200)
        data = response.json
        print(f"get restricted: {data}")
        self.assertLess(0, len(data))
        self.assertIn("address", data[0])
        self.assertIn("B Street 1", data[0]["address"])

    def test_2_post(self):
        test_data = {"address": "C Street 1",
                     "email": "jd@myinsuranceapp.com",
                     "fullname": "John Doe",
                     "birthdate": "this is not a birthday02.10.2020",
                     "country": "Berlin",
                     "city": "Spain",
                     "password": "you never put plain text passwords into an api",}
        response = self.client.post('/api/v1/users/',content_type='application/json',headers=self.headers, json=test_data)
        data=response.json
        print(f"post: {data}")
        self.assertEqual(response.status_code, 200)
        self.assertTrue(data["ok"])

  
