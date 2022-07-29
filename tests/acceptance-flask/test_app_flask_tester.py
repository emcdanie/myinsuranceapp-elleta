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
    


 

     
       