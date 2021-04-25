import requests
import json


# Save image
# url = "https://imgs.xkcd.com/comics/state_word_map.png"
# r = requests.get(url)
# with open("F:\\Дима\\_IT Info\\Python_tutorial\\2021-03-18-QAForEveryone\\images\\map.png", "wb") as file:
#     file.write(r.content)

class HttpbinAPI:

    def get_page(self):
        url = "https://httpbin.org/get"
        payload = {'page': 2, 'any-key': 'any-value'}
        r = requests.get(url, payload)
        print(r.json())
        assert r.json()['args']['any-key'] == 'any-value', 'Wrong assertion'
        return self

    def add_info(self):
        url = "https://httpbin.org/post"
        payload = {'page': 2, 'any-key': 'any-value'}
        r = requests.post(url, payload)
        assert r.json()['form']['any-key'] == 'any-value', 'Wrong assertion'
        return self

    def get_auth_token(self):
        url = "https://httpbin.org/basic-auth/dima/nov"
        r = requests.get(url, auth=('dima', 'nov'))
        assert r.json()["authenticated"] == 1
        return self


class RestfulBookerAPI:

    def auth_token(self):
        payload = {
            "username": "admin",
            "password": "password123"
        }
        url = "https://restful-booker.herokuapp.com/auth"
        r = requests.post(url, payload)
        actual_result = r.status_code
        expected_result = 200
        token = r.json()["token"]
        assert actual_result == expected_result, f"Actual result: {actual_result}, Expected: {expected_result}"
        return token

    def create_booking(self):
        url = "https://restful-booker.herokuapp.com/booking"
        s = requests.Session()
        headers = {"Accept": "application/json", "Content-Type": "application/json"}
        payload = {
            "firstname": "Jim",
            "lastname": "Brown",
            "totalprice": 1234,
            "depositpaid": True,
            "bookingdates": {
                "checkin": "2018-01-01",
                "checkout": "2019-01-01"
            },
            "additionalneeds": "Breakfast"
        }
        r = s.post(url, data=json.dumps(payload), headers=headers)
        actual_result = r.status_code
        expected_result = 200
        assert actual_result == expected_result, f"Actual result: {actual_result}, Expected: {expected_result}"
        id = r.json()["bookingid"]
        return id

    def get_booking(self, id, total_price):
        url = f"https://restful-booker.herokuapp.com/booking/{id}"
        r = requests.get(url)
        actual_result = r.json()["totalprice"]
        expected_result = total_price
        assert actual_result == expected_result, f"Actual result: {actual_result}, Expected result: {expected_result}"
        return self


    def update_booking(self, id, tokent):
        url = f"https://restful-booker.herokuapp.com/booking/{id}"
        headers = {"Accept": "application/json", "Content-Type": "application/json", "token": tokent}
        payload = {
            "firstname": "Jim",
            "lastname": "Brown",
            "totalprice": 22222,
            "depositpaid": True,
            "bookingdates": {
                "checkin": "2018-01-01",
                "checkout": "2019-01-01"
            },
            "additionalneeds": "Breakfast"
        }
        r = requests.put(url, data=json.dumps(payload), headers=headers)
        # actual_result = r.json()["totalprice"]
        # expected_result = 22222,
        # assert actual_result == expected_result, f"Actual result: {actual_result}, Expected result: {expected_result}"
        return r.status_code


class ReqRes:

    def __init__(self):
        self.id = 1

    def get_user(self, id):
        url = f"https://reqres.in/api/users/{id}"
        r = requests.get(url)
        actual_result = r.json()["data"]["id"]
        expected_result = id
        assert actual_result == expected_result, f"Actual result: {actual_result}, Expected result: {expected_result}"
        return self

    def create_user(self):
        url = f"https://reqres.in/api/users"
        payload = {
            "name": "Dima",
            "job": "qa"
        }
        r = requests.post(url, payload)
        id = r.json()["id"]
        status_code = r.status_code
        assert status_code == 201, f"Status code: {status_code}"
        self.id = id
        return self


class SwaggerPet:

    def create_pet(self):
        url = "https://petstore.swagger.io/v2/pet"
        headers = {"Content-Type": "application/json"}
        payload = {
          "id": 1000,
          "category": {
            "id": 0,
            "name": "string1000"
          },
          "name": "doggie1000",
          "photoUrls": [
            "string"
          ],
          "tags": [
            {
              "id": 0,
              "name": "string"
            }
          ],
          "status": "available"
        }
        r = requests.post(url, data=json.dumps(payload), headers=headers)
        id = r.json()["id"]
        status_code = r.status_code
        assert status_code == 200, f"Status code: {status_code}"
        self.id = id
        return self

    def get_pet(self, id):
        url = f"https://petstore.swagger.io/v2/pet/{id}"
        r = requests.get(url)
        actual_result = r.json()["id"]
        expected_result = id
        assert actual_result == expected_result, f"Actual result: {actual_result}, Expected result: {expected_result}"
        self.pet_name = r.json()["name"]
        return self


    def change_name(self):
        url = "https://petstore.swagger.io/v2/pet"
        headers = {"Content-Type": "application/json"}
        payload = {
          "id": 1000,
          "category": {
            "id": 0,
            "name": "string1000"
          },
          "name": "vesta1000",
          "photoUrls": [
            "string"
          ],
          "tags": [
            {
              "id": 0,
              "name": "string"
            }
          ],
          "status": "available"
        }
        r = requests.put(url, data=json.dumps(payload), headers=headers)
        actual_name = r.json()["name"]
        expected_name = "vesta1000"
        assert actual_name == expected_name, f"actual_name: {actual_name} expected_name: {expected_name}"
        self.pet_name = actual_name
        return self

    def delete_item(self, id):
        url = f"https://petstore.swagger.io/v2/pet/{id}"
        r = requests.delete(url)
        status_code = r.status_code
        if status_code == 200:
            assert status_code == 200, f"Status code: {status_code}"
            print("Object removed successfully")
        else:
            assert status_code == 404, f"Status code: {status_code}"
            print("Object not found")