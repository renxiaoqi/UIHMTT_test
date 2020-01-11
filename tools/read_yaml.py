import os

import yaml

from config import BASE_URL


def read_yaml(filename):
    my_list = []
    with open(BASE_URL+os.sep+"data"+os.sep+filename,"r",encoding="utf-8") as f:
        for data in yaml.load(f,Loader=yaml.FullLoader).values():
            my_list.append(tuple(data.values()))
        return my_list
if __name__ == '__main__':
    print(read_yaml("mp_article.yml"))