# -*- coding:utf-8 -*-
import yaml
with open("test_yaml.yaml",mode="r",encoding="utf-8") as file:
        value=yaml.safe_load(file)
        print(value)
name=value[0]['name']
name2=value[0]["name2"]
print(name)
print(name2)
import yaml

with open("yaml_test.yaml.py",mode="r",encoding="utf-8") as file:
    value=yaml.safe_load(file)
    
