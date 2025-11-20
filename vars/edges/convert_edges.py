import yaml
import argparse

# -----------------------------
# CLI arguments
# -----------------------------
parser = argparse.ArgumentParser(description="Convert station YAML to edge format")
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
edge_lists = [
    "sees"
    ]

for edge_list in edge_lists:
    processed_list = []
    for item in data.get(edge_list, []):
        from_dict = item.pop("from")
        to_dict = item.pop("to")

        from_row = from_dict["row"]
        from_col = from_dict["column"]
        from_entity = f"C{from_row}{from_col}"

        to_row = to_dict["row"]
        to_col = to_dict["column"]
        to_entity = f"C{to_row}{to_col}"

        new_from = {}
        new_from["entity_name"] = from_entity
        new_from["label"] = "Cell"

        new_to = {}
        new_to["entity_name"] = to_entity
        new_to["label"] = "Cell"


        new_edge = {}
        new_edge["type"] = "SEES"
        new_edge["bi_directional"] = True
        new_edge["from"] = new_from
        new_edge["to"] = new_to

        print(new_edge)

        processed_list.append(new_edge)
    data[edge_list] = processed_list

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
