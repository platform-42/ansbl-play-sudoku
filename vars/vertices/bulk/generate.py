import yaml

cells = []

for row in range(1, 10):
    for col in range(1, 10):
        cell = {
            "label": "Cell",
            "entity_name": f"C{row}{col}",
            "properties": {
                "row": {
                    "value": row,
                    "type": "int"
                },
                "column": {
                    "value": col,
                    "type": "int"
                },
                "domain": {
                    "value": [1,2,3,4,5,6,7,8,9],
                    "type": "list",
                    "element_type": "int"
                },
                "color": {
                    "value": 0,
                    "type": "int"
                },
                "color_backup": {
                    "value": 0,
                    "type": "int"
                },
                "domain_backup": {
                    "value": [],
                    "type": "list",
                    "element_type": "int"
                },
                "tried_colors" : {
                    "value": [],
                    "type": "list",
                    "element_type": "int"
                },
                "assigned_by_guess" : {
                    "value": False,
                    "type": "bool"
                }
            }
        }
        cells.append(cell)

# Dump YAML
print(yaml.dump(cells, sort_keys=False))
