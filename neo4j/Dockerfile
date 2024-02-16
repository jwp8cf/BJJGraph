FROM neo4j:4.3
COPY ./init.cypher /var/lib/neo4j/import/init.cypher
COPY ./entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh
ENTRYPOINT ["/entrypoint.sh"]
CMD ["neo4j"]
