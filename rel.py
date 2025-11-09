#!/usr/bin/env python3
import yaml

edges = []

# Generate all SEES relationships for Sudoku cells
for r1 in range(1, 10):
    for c1 in range(1, 10):
        for r2 in range(1, 10):
            for c2 in range(1, 10):
                # Skip same cell
                if (r1, c1) == (r2, c2):
                    continue

                # Cells see each other if same row, column, or 3x3 box
                same_row = r1 == r2
                same_col = c1 == c2
                same_box = (r1 - 1)//3 == (r2 - 1)//3 and (c1 - 1)//3 == (c2 - 1)//3

                if same_row or same_col or same_box:
                    # Only include one direction (lexicographic ordering)
                    if (r1, c1) < (r2, c2):
                        edges.append({
                            "from": {"row": r1, "column": c1},
                            "to": {"row": r2, "column": c2}
                        })

# Write to YAML
with open("sudoku_sees.yml", "w") as f:
    yaml.safe_dump({"sudoku_sees": edges}, f, sort_keys=False)

print(f"Generated {len(edges)} unique SEES relationships (bi-directional handled by module).")

