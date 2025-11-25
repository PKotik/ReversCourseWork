import json

with open("sbom.json") as f:
    sbom = json.load(f)

print("Компоненты проекта:")
for comp in sbom.get("components", []):
    name = comp["name"]
    version = comp["version"]
    comp_type = comp.get("type", "library")
    print(f"- {name} ({comp_type}): {version}")
