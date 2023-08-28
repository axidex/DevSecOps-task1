import requests, json

def to_log(name, url, headers):
    resp = requests.get(url,headers=headers)
    parsed = json.loads(resp.content)
    with open(name, "w") as file:
        file.write(json.dumps(parsed, indent=2, sort_keys=True))

# Must have uuid http://localhost:8081/api/v1/metrics/project/{uuid}/current 
# and api-key from dependency-tracker GUI below
# to execute more cURL commands check htwagger.jtp://localhost:8081/api/sson with SwaggerUI plugin in ur browser

headers = {"X-Api-Key": "TimbOxMatBj7kSlCEq9KYJUoY70AsWmK", "accept": "application/json"}

to_log(name =   'vuln.log', 
       url =    'http://192.168.128.1:8081/api/v1/metrics/project/e561948b-93e1-4f86-8c04-1f10560df992/current',
       headers = headers)
to_log(name =   'vuln_description.log',
       url =    'http://192.168.128.1:8081/api/v1/vulnerability/project/e561948b-93e1-4f86-8c04-1f10560df992',
       headers = headers)
