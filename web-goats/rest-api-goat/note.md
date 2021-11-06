# rest-api-goat

## Installation (Ubuntu)
```
apt install docker.io
systemctl start docker
systemctl enable docker
git clone https://github.com/optiv/rest-api-goat.git
cd rest-api-gota
docker run -d -p 5000:5000 rest-api-goat
```
The rest-api-goat will run on `http://127.0.0.1:5000`

## Import Repository to Postman
```
1) Create a new workspace 
2) Donwload master.zip from https://github.com/optiv/rest-api-goat.git
3) Import the unziped folder to the newly created worksapce in Postman
```

