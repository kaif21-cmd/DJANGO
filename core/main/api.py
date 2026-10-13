import requests
url ="https://jsonplaceholder.typicode.com/users"
response=requests.get(url)
print(response.status_code)
data=response.json()
print(data)
for user in data :
    print("----user details----")
    print("ID",user["id"])
    print("Website",user["website"])