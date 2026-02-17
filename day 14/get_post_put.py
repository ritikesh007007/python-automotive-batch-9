import requests

base_url = "https://jsonplaceholder.typicode.com/users"  

get_response = requests.get(base_url)
print("GET Status:", get_response.status_code)  # 200


post_data = {"name": "Ritikesh", "role": "Student"}
post_response = requests.post(base_url, json=post_data)
print("POST Status:", post_response.status_code)  # 201


put_data = {"name": "Ritikesh ", "role": "College student"}
put_response = requests.put(f"{base_url}/1", json=put_data)
print("PUT Status:", put_response.status_code)  # 200


patch_data = {"role": "Graduate Student"}
patch_response = requests.patch(f"{base_url}/1", json=patch_data)
print("PATCH Status:", patch_response.status_code)  # 200


delete_response = requests.delete(f"{base_url}/1")
print("DELETE Status:", delete_response.status_code)  # 200
