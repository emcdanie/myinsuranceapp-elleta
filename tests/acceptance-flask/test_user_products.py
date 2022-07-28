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

    def test_2_get_user_products_valid_token(self):
        response = self.client.get('/api/v1/users/1/products', content_type='application/json', headers=self.headers)
        data= response.json       
        print(f"get_user_products: {data}")
        self.assertEqual(response.status_code, 200)
        self.assertTrue(len(data)>0)
      
    
 
    def test_3_get_user_products_invalid_token(self):
        ivalid_fake_token='CfDJ8OW5OI0CPGJBgSNlGwO0x4YF7qbYKVv7KOO-N0eFtDUzXOrL7F9Xd9W1otVi4ueJOkAmAhuoHFWNkqRaFD7zvAMHMSKncl6Vo5QXKmpvy6vqxOKxSURdIey8aZPRi3Nnhp2p9la-Al5xrVKz0lignRdcCHf3O7pF9zv_sNx_c_T7pUe3WsxaJEPX3t_9FO2Wjw'

        headers = {"Authorization": f"Bearer {ivalid_fake_token}"}
        response = self.client.get('/api/v1/users/2/products', content_type='application/json', headers=headers)
        data= response.json
        print(f"get_user_products: {data}")

       
        self.assertTrue(response.status_code > 400)
        
