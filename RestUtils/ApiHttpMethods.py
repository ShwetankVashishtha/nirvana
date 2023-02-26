import requests


class ApiHttpMethods:

    @staticmethod
    def post(base_url, endpoint, data):
        url = f"{base_url}/{endpoint}"
        headers = {'Content-Type': 'application/json'}
        response = requests.post(url, json=data, headers=headers)

        return response

    @staticmethod
    def get(base_url, endpoint, params=None):
        url = f"{base_url}/{endpoint}"
        response = requests.get(url, params=params)

        return response

    @staticmethod
    def get(base_url, endpoint, headers=None, params=None):
        url = f"{base_url}/{endpoint}"
        response = requests.get(url, headers=headers, params=params)

        return response

    @staticmethod
    def put(base_url, endpoint, data):
        url = f"{base_url}/{endpoint}"
        headers = {'Content-Type': 'application/json'}
        response = requests.put(url, json=data, headers=headers)

        return response

    @staticmethod
    def delete(base_url, endpoint):
        url = f"{base_url}/{endpoint}"
        response = requests.delete(url)

        return response
