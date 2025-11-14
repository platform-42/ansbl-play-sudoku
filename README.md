MATCH (c:Cell {entity_name:'C11'})-[:SEES]->(n)
SET n.domain = [x IN n.domain WHERE x <> c.value]



MATCH (c:Cell {entity_name:'C11'})-[:SEES]->(n)
SET n.domain = [x IN n.domain WHERE x <> c.value]


MATCH (c:Cell {entity_name: 'C11'})
SET c.value = '5', c.domain = ['5']
WITH c, '5' AS value
MATCH (c)-[:SEES]->(n:Cell)
WHERE n.value = 0
SET n.domain = [x IN n.domain WHERE x <> value]
RETURN c, n

MATCH (c:Cell {entity_name: 'C12'})
SET c.domain = [x IN c.domain WHERE x <> 5]
RETURN c

MATCH (c:Cell {entity_name: 'C11'})
SET c.value = 5, c.domain = 5
WITH c, 5 AS pp
MATCH p = (c)-[:SEES]->(n:Cell)
WHERE n.value = 0
SET n.domain = [x IN n.domain WHERE x <> pp]
RETURN c, n
