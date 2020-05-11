# testtask
'python3 -m venv venv'
'source venv/bin/activate'
'pip install -r requirements.txt'

curl request on localhost:
CURL Request Sample Type :
curl --header "Content-Type: application/json" \
  --request POST \
  --data '{"username":"xyz","password":"xyz"}' \
  http://127.0.0.1:8000/tasks/request/
Output: 
{"username": "xyz", "password": "xyz"}
