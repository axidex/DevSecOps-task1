import requests, json, sys

project_name = sys.argv[1]
project_branch = sys.argv[2]

def to_log(name, url, headers):
    resp = requests.get(url, headers=headers)
    parsed = json.loads(resp.content)
    with open(name, "w") as file:
        file.write(json.dumps(parsed, indent=2, sort_keys=True))

def uuid_get(name, branch, url, headers):
    resp = requests.get(url,headers=headers)
    parsed = json.loads(resp.content)
    for el in parsed:
        if el['name'] == name and el['version'] == branch:
            return el["uuid"]
        
# Must have uuid http://localhost:8081/api/v1/metrics/project/{uuid}/current 
# and api-key from dependency-tracker GUI below
# to execute more cURL commands check htwagger.jtp://localhost:8081/api/sson with SwaggerUI plugin in ur browser
headers = {"X-Api-Key": "TimbOxMatBj7kSlCEq9KYJUoY70AsWmK", "accept": "application/json"}
uuid = uuid_get( project_name, project_branch,
                 'http://192.168.128.1:8081/api/v1/project', 
                 headers=headers )

to_log( name =   'vuln.log', 
        url =    'http://192.168.128.1:8081/api/v1/metrics/project/' + str(uuid) + '/current',
        headers = headers )

to_log( name =   'vuln_description.log',
        url =    'http://192.168.128.1:8081/api/v1/vulnerability/project/' + str(uuid),
        headers = headers )
