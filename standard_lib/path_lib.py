from pathlib import Path

p = Path("/Users/thibh/python-311-new-features/standard_lib/paths_tests")

print("Fichiers et dossiers")
dirs = p.glob("*")
for d in dirs:
    print(d)

print("Dossiers seulement")
dirs = p.glob("*/")
for d in dirs:
    print(d)
