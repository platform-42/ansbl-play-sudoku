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


    "sudoku_board": 
    
    5 3 4   6 7 8   9 1 2
    6 7 2   1 9 5   3 4 8
    1 9 8   3 4 2   5 6 7

    8 5 9   7 6 1   4 2 3
    4 2 6   8 5 3   7 9 1
    7 1 3   9 2 4   8 5 6
    
    9 6 1   5 3 7   2 8 4
    2 8 7   4 1 9   6 3 5
    3 4 5   2 8 6   1 7 9