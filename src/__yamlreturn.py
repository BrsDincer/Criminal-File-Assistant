from __tempinitparameters import CLASSINIT,RESPONSES,FILES,TYPEERROR,YAMLFILE
import yaml

class READYAMLFILE(object):
    def __init__(self)->CLASSINIT:
        self.__file = YAMLFILE
    def __str__(self)->CLASSINIT:
        return "READ YAML FILE - PROCESS"
    def __call__(self)->None:
        return None
    def __getstate__(self)->CLASSINIT:
        raise TypeError(TYPEERROR)
    def __repr__(self)->str:
        return READYAMLFILE.__doc__
    def _GET(self,er:str="replace",en:str="utf-8")->FILES:
        return yaml.safe_load(open(self.__file,
                                   errors=er,
                                   encoding=en))
    def _API(self)->RESPONSES:
        return self._GET()["apikey"]["OPENAI_API_KEY"]