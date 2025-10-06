import yaml

config= {
    "model" : "RandomForest",
    "params" : {
    "n_estimators" : 100,
    "max_depth" : 5
    },
"dataset": "student.csv"
}


with open("config.yml", "w") as f:
    yaml.dump(config, f)

with open("config.yml", "r") as f:
    data= yaml.safe_load(f)

print(data["params"]["n_estimators"])