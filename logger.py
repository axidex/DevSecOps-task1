import requests, json, sys

project_name = sys.argv[1]

def to_log(name, url, headers):
    resp = requests.get(url,headers=headers)
    parsed = json.loads(resp.content)
    with open(name, "w") as file:
        file.write(json.dumps(parsed, indent=2, sort_keys=True))

def uuid_get(name, url, headers):
    resp = requests.get(url,headers=headers)
    parsed = json.loads(resp.content)
    for el in parsed:
        if el['name'] == name:
            return el["uuid"]
uuid = uuid_get( project_name, 'http://192.168.128.1:8081/api/v1/project', {"X-Api-Key": "TimbOxMatBj7kSlCEq9KYJUoY70AsWmK", "accept": "application/json"})
# Must have uuid http://localhost:8081/api/v1/metrics/project/{uuid}/current 
# and api-key from dependency-tracker GUI below
# to execute more cURL commands check htwagger.jtp://localhost:8081/api/sson with SwaggerUI plugin in ur browser

headers = {"X-Api-Key": "TimbOxMatBj7kSlCEq9KYJUoY70AsWmK", "accept": "application/json"}

to_log(name =   'vuln.log', 
       url =    'http://192.168.128.1:8081/api/v1/metrics/project/' + uuid + '/current',
       headers = headers)
to_log(name =   'vuln_description.log',
       url =    'http://192.168.128.1:8081/api/v1/vulnerability/project/' + uuid,
       headers = headers)
