#!__author__ = "yf"
"""
pycharm
"""
import yaml
import os

# curPath = os.path.dirname(os.path.realpath(__file__))
# yamlFile = os.path.join(curPath, "data.yaml")
# file_stream = open(yamlFile)
# yaml_data= yaml.load(file_stream, Loader=yaml.FullLoader)
# print(yaml_data)
# print(type(yaml_data))


def getYamlData():
    curPath = os.path.dirname(os.path.realpath(__file__))
    yamlFile = os.path.join(curPath, "data.yaml")
    file_stream = open(yamlFile)
    yaml_data = yaml.load(file_stream, Loader=yaml.FullLoader)
    # print(yaml_data)
    # print(type(yaml_data))
    return yaml_data