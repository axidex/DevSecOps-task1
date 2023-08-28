mkdir app
cd app

rm -rf *
git clone https://github.com/netlify/gocommerce
mv gocommerce src

cd src && go build
cd ..
wget https://github.com/CycloneDX/cyclonedx-gomod/releases/download/v1.4.1/cyclonedx-gomod_1.4.1_linux_arm64.tar.gz
tar -xvzf cyclonedx-gomod_1.4.1_linux_arm64.tar.gz
cyclonedx-gomod app -output ./sbom.xml src

curl -v -X "PUT" \
    "http://localhost:8081/api/v1/bom" \
    -d @out.json
    -H 'X-API-Key: TimbOxMatBj7kSlCEq9KYJUoY70AsWmK' \
    -H 'Content-Type: application/json'

cp ../logger.py .
python3.10 logger.py
cat vuln.log

