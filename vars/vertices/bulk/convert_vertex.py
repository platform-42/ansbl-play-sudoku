import yaml
import argparse

# -----------------------------
# CLI arguments
# -----------------------------
parser = argparse.ArgumentParser(description="Convert station YAML to vertex format")
parser.add_argument("--input", "-i", required=True, help="Input YAML file")
parser.add_argument("--output", "-o", required=True, help="Output YAML file")
args = parser.parse_args()

input_file = args.input
output_file = args.output

# -----------------------------
# Load YAML
# -----------------------------
with open(input_file, "r", encoding="utf-8") as f:
    data = yaml.safe_load(f)

# -----------------------------
# Process station lists
# -----------------------------
vertex_lists = [
    "cells"
    ]

for vertex_list in vertex_lists:
    processed_list = []
    for item in data.get(vertex_list, []):
        row = item.pop("row", None)
        column = item.pop("column", None)
        entity_name = f"C{row}{column}"
        domain = [1,2,3,4,5,6,7,8,9]
        label = "Cell"

        new_row = {}
        new_row["value"] = row
        new_row["type"] = "int"

        new_column = {}
        new_column["value"] = column
        new_column["type"] = "int"

        new_domain = {}
        new_domain["value"] = domain
        new_domain["type"] = "list"
        new_domain["element_type"] = "int"

        new_color = {}
        new_color["value"] = 0
        new_color["type"] = "int"

        new_properties = {}
        new_properties["row"] = new_row
        new_properties["column"] = new_column
        new_properties["domain"] = new_domain
        new_properties["color"] = new_color

        new_vertex = {}
        new_vertex["label"] = label
        new_vertex["entity_name"] = entity_name
        new_vertex["properties"] = new_properties

        print(new_vertex)

        processed_list.append(new_vertex)
    data[vertex_list] = processed_list

# -----------------------------
# Write YAML
# -----------------------------
with open(output_file, "w", encoding="utf-8") as f:
    yaml.safe_dump(
        data,
        f,
        sort_keys=False,
        default_flow_style=False,
        allow_unicode=True
    )

print(f"Processed {input_file} -> {output_file}")
