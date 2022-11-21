from jinja2 import Environment, FileSystemLoader
import yaml

with open("r1.yaml", "r") as f:
    data = yaml.safe_load(f)

with open("ios_final.j2", "r") as f:
    template_string = f.read()

template = Environment(loader=FileSystemLoader("./")).from_string(template_string)
config = template.render(data)
print(config)