import yaml

fp = open("demo.yaml")
data = yaml.load(fp)
print(data["AccountTestcases"]["login with valid account"][0])