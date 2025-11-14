MATCH (c:Cell {entity_name:'C11'})-[:SEES]->(n)
SET n.domain = [x IN n.domain WHERE x <> c.value]



MATCH (c:Cell {entity_name:'C11'})-[:SEES]->(n)
SET n.domain = [x IN n.domain WHERE x <> c.value]