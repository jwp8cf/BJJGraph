from neo4j import GraphDatabase


class Neo4jConnection:

    def __init__(self, uri, user, password):
        self.__uri = uri
        self.__user = user
        self.__password = password
        self.__driver = None
        try:
            self.__driver = GraphDatabase.driver(self.__uri, auth=(self.__user, self.__password))
        except Exception as e:
            print("Failed to create the driver:", e)

    def close(self):
        if self.__driver is not None:
            self.__driver.close()

    def query(self, query, parameters=None, db=None):
        session = None
        response = None
        try:
            session = self.__driver.session(database=db) if db is not None else self.__driver.session()
            response = list(session.run(query, parameters))
        except Exception as e:
            print("Query failed:", e)
        finally:
            if session is not None:
                session.close()
        return response

#delete init.cypher if it exists
import os
if os.path.exists("neo4j/init.cypher"):
    os.remove("neo4j/init.cypher")


#all cypher queries shall be appended to the file init.cypher
def write_to_file(file_name, text):
    with open(file_name, "a") as file:
        file.write(text + "\n")

# Connect to the Neo4j database
conn = Neo4jConnection(uri="bolt://localhost:7687", user="neo4j", password="letmein4y")

# run MATCH (n) DETACH DELETE n
# to delete all nodes and relationships
conn.query("MATCH (n) DETACH DELETE n")

# Example query to create a node

from nodes.competitions import competitions
create_query = "CREATE (:Competition {name: $name})"
for parameter in competitions:
    result = conn.query(create_query, parameters=parameter)
    write_to_file("init.cypher", "CREATE (:Competition {name: \"" + parameter["name"] + "\"});")

from nodes.practitioners import practitioners
create_query = "CREATE (:Practitioner {name: $name, image: $image, imageShape: $imageShape})"
for parameter in practitioners:
    if "image" not in parameter:
        parameter["image"] = "None"
    if "imageShape" not in parameter:
        parameter["imageShape"] = "None"
    result = conn.query(create_query, parameters=parameter)
    write_to_file("init.cypher", "CREATE (:Practitioner {name: \"" + parameter["name"] + "\", image: \"" + parameter["image"] + "\", imageShape: \"" + parameter["imageShape"] + "\"});")

from nodes.belts import belts, beld_to_beld
create_query = "CREATE (:Belt {name: $name, image: $image, imageShape: $imageShape})"
for parameter in belts:
    result = conn.query(create_query, parameters=parameter)
    write_to_file("init.cypher", "CREATE (:Belt {name: \"" + parameter["name"] + "\", image: \"" + parameter["image"] + "\", imageShape: \"" + parameter["imageShape"] + "\"});")


create_query = ("MATCH (b1:Belt {name: $belt1}), (b2:Belt {name: $belt2}) "
                "CREATE (b1)-[:BeltToBelt]->(b2)")
for parameter in beld_to_beld:
    result = conn.query(create_query, parameters=parameter)
    write_to_file("init.cypher", "MATCH (b1:Belt {name: \"" + parameter["belt1"] + "\"}), (b2:Belt {name: \"" + parameter["belt2"] + "\"}) CREATE (b1)-[:BeltToBelt]->(b2);")

from nodes.principles import principles
create_query = "CREATE (:Principle {name: $name})"
for parameter in principles:
    result = conn.query(create_query, parameters=parameter)
    write_to_file("init.cypher", "CREATE (:Principle {name: \"" + parameter["name"] + "\"});")

from  nodes.positions import positions
create_query = "CREATE (:Position {name: $name, gi: $gi, image: $image})"
for parameter in positions:
    if not "gi" in parameter:
        parameter["gi"] = "false"
    if not "image" in parameter:
        parameter["image"] = "None"
    result = conn.query(create_query, parameters=parameter)
    write_to_file("init.cypher", "CREATE (:Position {name: \"" + parameter["name"] + "\", gi: " + parameter["gi"] + ", image: \"" + parameter["image"] + "\"});")

from nodes.transitions import transitions
create_query = "CREATE (:Transition {name: $name, difficulty: $difficulty, beltLevel: $beltLevel, type: $type, image: $image})"
for parameter in transitions:
    if not "image" in parameter:
        parameter["image"] = "None"
    result = conn.query(create_query, parameters=parameter)
    write_to_file("init.cypher", "CREATE (:Transition {name: \"" + parameter["name"] + "\", difficulty: \"" + parameter["difficulty"] + "\", beltLevel: \"" + parameter["beltLevel"] + "\", type: \"" + parameter["type"] + "\", image: \"" + parameter["image"] + "\"});")

from nodes.escapes import escapes
create_query = "CREATE (:Escape {name: $name})"
for parameter in escapes:
    result = conn.query(create_query, parameters=parameter)
    write_to_file("init.cypher", "CREATE (:Escape {name: \"" + parameter["name"] + "\"});")

from nodes.submissions import submissions
create_query = "CREATE (:Submission {name: $name, difficulty: $difficulty, beltLevel: $beltLevel, type: $type, image: $image})"
for parameter in submissions:
    if not "image" in parameter:
        parameter["image"] = "None"
    result = conn.query(create_query, parameters=parameter)
    write_to_file("init.cypher", "CREATE (:Submission {name: \"" + parameter["name"] + "\", difficulty: \"" + parameter["difficulty"] + "\", beltLevel: \"" + parameter["beltLevel"] + "\", type: \"" + parameter["type"] + "\", image: \"" + parameter["image"] + "\"});")


from nodes.positions import positions_escaping_with_escape
create_query = ("MATCH (e:Escape {name: $escape}), (p:Position {name: $position}) "
                "CREATE (p)-[:ESCAPES_WITH]->(e)")
for parameter in positions_escaping_with_escape:
    result = conn.query(create_query, parameters=parameter)
    write_to_file("init.cypher", "MATCH (e:Escape {name: \"" + parameter["escape"] + "\"}), (p:Position {name: \"" + parameter["position"] + "\"}) CREATE (p)-[:ESCAPES_WITH]->(e);")

from nodes.escapes import escapes_lead_to_position
create_query = ("MATCH (e:Escape {name: $escape}), (p:Position {name: $position}) "
                "CREATE (e)-[:LEADS_TO]->(p)")
for parameter in escapes_lead_to_position:
    result = conn.query(create_query, parameters=parameter)
    write_to_file("init.cypher", "MATCH (e:Escape {name: \"" + parameter["escape"] + "\"}), (p:Position {name: \"" + parameter["position"] + "\"}) CREATE (e)-[:LEADS_TO]->(p);")

from nodes.positions import position_to_submission
create_query = ("MATCH (s:Submission {name: $submission}), (p:Position {name: $position}) "
                "CREATE (p)-[:PositionToSubmission]->(s)")
for parameter in position_to_submission:
    result = conn.query(create_query, parameters=parameter)
    write_to_file("init.cypher", "MATCH (s:Submission {name: \"" + parameter["submission"] + "\"}), (p:Position {name: \"" + parameter["position"] + "\"}) CREATE (p)-[:PositionToSubmission]->(s);")


# Technique DISLOCATE from Position
create_query = ("MATCH (a:Technique {name: $technique}), (p:Position {name: $position}) "
                "CREATE (a)-[:DISLOCATE]->(p)")

parameters = [
#single leg against standing
    {"technique": 'Single Leg Takedown', "position": 'Standing'},
    #double leg against standing
    {"technique": 'Double Leg Takedown', "position": 'Standing'},
    {"technique": 'Scooping', "position1": 'Back Control (taken)', "position": 'Scoop Position'},
    {"technique": 'Hip Escape', "position1": 'Side Control (bottom)', "position": 'Knee Shield'},
    #scooping against back mount
    {"technique": 'Scooping', "position": 'Back Control (taken)'},
]

for parameter in parameters:
    result = conn.query(create_query, parameters=parameter)
    write_to_file("init.cypher", "MATCH (a:Technique {name: \"" + parameter["technique"] + "\"}), (p:Position {name: \"" + parameter["position"] + "\"}) CREATE (a)-[:DISLOCATE]->(p);")




create_query = ("MATCH (a:Technique {name: $technique}), (c:Technique {name: $counter}) "
                "CREATE (c)-[:COUNTERS]->(a)")

parameters = [
    {"technique": 'Deep Half Guard', "counter": 'Cross Face'},
]

for parameter in parameters:
    result = conn.query(create_query, parameters=parameter)
    write_to_file("init.cypher", "MATCH (a:Technique {name: \"" + parameter["technique"] + "\"}), (c:Technique {name: \"" + parameter["counter"] + "\"}) CREATE (c)-[:COUNTERS]->(a);")

create_query = ("MATCH (s:Submission {name: $submission}), (c:Technique {name: $counter}) "
                "CREATE (c)-[:DEFENCES]->(s)")

parameters = [
    {"submission": 'Armbar', "counter": 'Stack Defense'},
    {"submission": 'Triangle-Choke', "counter": 'Stack Defense'},
]

for parameter in parameters:
    result = conn.query(create_query, parameters=parameter)
    write_to_file("init.cypher", "MATCH (s:Submission {name: \"" + parameter["submission"] + "\"}), (c:Technique {name: \"" + parameter["counter"] + "\"}) CREATE (c)-[:DEFENCES]->(s);")


from nodes.positions import positions_using_transition
create_query = (
   "MATCH (t:Transition {name: $transition}), (p:Position {name: $position}) "
   "CREATE (p)-[:Transition]->(t)"
)
for parameter in positions_using_transition:
    result = conn.query(create_query, parameters=parameter)
    write_to_file("init.cypher", "MATCH (t:Transition {name: \"" + parameter["transition"] + "\"}), (p:Position {name: \"" + parameter["position"] + "\"}) CREATE (p)-[:Transition]->(t);")
#

from nodes.transitions import transitions_leading_to_position
create_query = (
    "MATCH (t:Transition {name: $transition}), (p2:Position {name: $position2}) "
    "CREATE (t)-[:LEADS_TO]->(p2)")
for parameter in transitions_leading_to_position:
    result = conn.query(create_query, parameters=parameter)
    write_to_file("init.cypher", "MATCH (t:Transition {name: \"" + parameter["transition"] + "\"}), (p2:Position {name: \"" + parameter["position2"] + "\"}) CREATE (t)-[:LEADS_TO]->(p2);")

create_query = (
    "MATCH (t:Technique {name: $technique}), (p2:Position {name: $position2}) "
    "CREATE (t)-[:STABILIZES]->(p2)")

parameters = [
    {"technique": 'Cross Face', "position2": 'Side Control (top)'},
]

for parameter in parameters:
    result = conn.query(create_query, parameters=parameter)
    write_to_file("init.cypher", "MATCH (t:Technique {name: \"" + parameter["technique"] + "\"}), (p2:Position {name: \"" + parameter["position2"] + "\"}) CREATE (t)-[:STABILIZES]->(p2);")


from nodes.positions import positions_to_position
create_query = (
    "MATCH (p1:Position {name: $position1}), (p2:Position {name: $position2}) "
    "CREATE (p1)-[:PositionToPosition]->(p2)")
for parameter in positions_to_position:
    result = conn.query(create_query, parameters=parameter)
    write_to_file("init.cypher", "MATCH (p1:Position {name: \"" + parameter["position1"] + "\"}), (p2:Position {name: \"" + parameter["position2"] + "\"}) CREATE (p1)-[:PositionToPosition]->(p2);")






# Don't forget to close the connection
conn.close()

# //Defense Techniques
#
