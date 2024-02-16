# BJJ Graph Neo4j

## Run docker-compose
```bash
docker-compose up
```

## Install python dependencies
```bash
pip3 install -r requirements.txt
```


## Run python script
```bash
python3 setup.py
```

## Open Neo4j Browser
Open [http://localhost:7474/browser/](http://localhost:7474/browser/)

Login with `neo4j` and password `letmein4y`

## Run queries
```MATCH (n)
OPTIONAL MATCH (n)-[r]->(m)
RETURN n, r, m
```