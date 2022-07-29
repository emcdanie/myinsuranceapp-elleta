import unittest 
from project import app 
import requests 

class TestApp(unittest.TestCase):

    token=''
    base_url='http://localhost:5000/api/v1'
    
    def test_1_getToken(self): 
        tester = app.test_client(self) 
        user_data = {"email":"jd@myinsuranceapp.com","password":"passwordjd"} 
        response = tester.post('/api/v1/token',content_type='application/json', json = user_data)
        data= response.json 
        
        print(f"post token: {data}")
        self.assertEqual(response.status_code, 200)

        if response.status_code==200:
            TestApp.token=data['token']
        
    def test_2_get_user_products_valid_token(self):
        tester = app.test_client(self)
        print(f"token: {self.token}")
        headers = {"Authorization": f"Bearer {TestApp.token}"}
        response = tester.get('/api/v1/users/2/products', content_type='application/json', headers=headers)

        data= response.json        
        print(f"get_user_products: {data}")
        self.assertEqual(response.status_code, 200)
        self.assertTrue(len(data)>0)
    

    def test_3_get_user_products_invalid_token(self):
        tester = app.test_client(self)
        ivalid_fake_token='CfDJ8OW5OI0CPGJBgSNlGwO0x4YF7qbYKVv7KOO-N0eFtDUzXOrL7F9Xd9W1otVi4ueJOkAmAhuoHFWNkqRaFD7zvAMHMSKncl6Vo5QXKmpvy6vqxOKxSURdIey8aZPRi3Nnhp2p9la-Al5xrVKz0lignRdcCHf3O7pF9zv_sNx_c_T7pUe3WsxaJEPX3t_9FO2Wjw'
        headers = {"Authorization": f"Bearer {ivalid_fake_token}"}
        response = tester.get('/api/v1/users/1/products', content_type='application/json', headers=headers)
        data= response.json 
        print(f"get_user_products: {data}")
        self.assertEqual(response.status_code > 400)


     
       