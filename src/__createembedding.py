from __tempinitparameters import CLASSINIT,RESPONSES,FILES,TYPEERROR,EMBEDDINGFILE,EMBEDDINGMODEL
import pickle,openai,pandas as pd
from openai.embeddings_utils import get_embedding

class BUILDCACHEEMBEDDING(object):
    def __init__(self,apikey:str)->CLASSINIT:
        self.__api = apikey
        self.__dir = EMBEDDINGFILE
        self.__mod = EMBEDDINGMODEL
        openai.api_key = self.__api
    def __str__(self)->str:
        return "BUILD CACHE EMBEDDING - PROCESS"
    def __call__(self)->None:
        return None
    def __getstate__(self)->CLASSINIT:
        raise TypeError(TYPEERROR)
    def __repr__(self)->str:
        return BUILDCACHEEMBEDDING.__doc__
    def _CONTROL(self)->RESPONSES:
        try:
            cache = pd.read_pickle(self.__dir)
        except FileNotFoundError:
            cache = {}
        return cache
    def _FROMSINGLE(self,string:str)->list:
        return get_embedding(string,self.__mod)
    def _FROMDATA(self,string:str,cache:FILES)->list:
        if (string,self.__mod) not in cache.keys():
            cache[(string,self.__mod)] = get_embedding(string,self.__mod)
            with open(self.__dir,"wb") as cfile:
                pickle.dump(cache,cfile)
        return cache[(string,self.__mod)]
    def _BUILD(self,string:str)->RESPONSES:
        try:
            cache = self._CONTROL()
            with open(self.__dir,"wb") as cfile:
                pickle.dump(cache,cfile)
            cache = self._FROMDATA(string,cache)
            return cache
        except:
            pass