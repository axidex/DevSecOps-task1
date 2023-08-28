mkdir app
cd app

rm -rf *
git clone https://github.com/0c34/govwa  src # https://github.com/0c34/govwa https://github.com/netlify/gocommerce
# mv govwa src

cd src && go build
cd ..
# wget https://github.com/CycloneDX/cyclonedx-gomod/releases/download/v1.4.1/cyclonedx-gomod_1.4.1_linux_arm64.tar.gz
# tar -xvzf cyclonedx-gomod_1.4.1_linux_arm64.tar.gz
cyclonedx-gomod app -output ./sbom.xml src

curl -v -X "POST" \
    "http://localhost:8081/api/v1/bom" \
    -H "X-API-Key: TimbOxMatBj7kSlCEq9KYJUoY70AsWmK" \
    -H "Content-Type: multipart/form-data" \
    -F "autoCreate=true" \
    -F "projectName=tmp" \
    -F "projectVersion=0.1" \
    -F "bom=@./sbom.xml"

# application/json
#-H "Body: {project: e561948b-93e1-4f86-8c04-1f10560df992, bom: out.json}"
sleep 10
cp ../logger.py .
python3.10 logger.py
cat vuln.log

