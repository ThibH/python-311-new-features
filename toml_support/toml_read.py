import tomllib

with open("setup.toml", "rb") as f:
    data = tomllib.load(f)

print(data)
print(data['owner']['name'])
print(data['database']['ports'])
