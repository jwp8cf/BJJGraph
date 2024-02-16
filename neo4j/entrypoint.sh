#!/bin/bash
neo4j start
# Wait for Neo4j to start. Adjust the sleep as needed.
sleep 10
cypher-shell -u neo4j -p password < /var/lib/neo4j/import/init.cypher
# Keep the container running.
tail -f /dev/null
