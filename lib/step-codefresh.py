import json
import os
from pickle import NONE
from dotenv import find_dotenv, load_dotenv

ENV_FILE = find_dotenv()
if ENV_FILE:
    load_dotenv(ENV_FILE)

def read_json(path):
    arq = open(path)
    arq_check = arq.read().replace("\n", "")
    print(f"conteudo = {arq_check}")
    return json.loads(arq_check)
    
def writer_json(date, path):
    with open(path, "w") as outfile:
        outfile.write(json.dumps(date))


path_configmap=os.getenv("PATH_CONFIGMAP",None)
path_secret=os.getenv("PATH_SECRET",None)
envs_configmap=os.getenv("CONFIGMAP",None)
envs_secret=os.getenv("SECRET",None)


if path_configmap and envs_configmap:
    list_configmap=read_json(path_configmap)
    for item in envs_configmap.split(","):
        key=item.split("=")[0]
        value=item.split("=")[1]
        list_configmap.get('data')[key]=value
    writer_json(list_configmap, path_configmap)
    print(list_configmap)

if path_secret and envs_secret:
    list_secret=read_json(path_secret)
    for item in envs_secret.split(","):
        key=item.split("=")[0]
        value=item.split("=")[1]
        list_secret.get('stringData')[key]=value   
    writer_json(list_secret, path_secret)
    print(list_secret)
    
# path_configmap=getEnvs("path_configmap","/codefresh/volume/nome.json")
# path_secret=getEnvs("path_secret","/codefresh/volume/nome.json")