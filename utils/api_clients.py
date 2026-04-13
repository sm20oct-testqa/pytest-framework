import requests
from configs.config import base_url


class APIclient:

    def get(self,end_url):
        endpoint_url = base_url+end_url
        return requests.get(endpoint_url)
    

    def post(self,end_url,payload):
        endpoint_url = base_url+end_url
        return requests.post(endpoint_url,json=payload)
    

    def put(self,end_url,payload):
        endpoint_url = base_url+end_url
        return requests.put(endpoint_url,json=payload)

    
    def delete(self,):
        endpoint_url = base_url+end_url
        return requests.delete(endpoint_url)
