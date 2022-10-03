from os.path import realpath, dirname
import json

# 读取配置json文件
def get_university_information(name):
    path = dirname(realpath(__file__)) + '/universityInfo/' + name + '.json'
    with open(path, 'r', encoding='utf-8') as f:
        return json.loads(f.read())