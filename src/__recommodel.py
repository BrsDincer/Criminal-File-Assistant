from __tempinitparameters import CLASSINIT,TYPEERROR,FILES,FILEERROR,EMBEDDINGMODEL,RESPONSES,RESULTS
from __createembedding import BUILDCACHEEMBEDDING
from __clustering import CLUSTERINGMODEL
from openai.embeddings_utils import distances_from_embeddings
from openai.embeddings_utils import indices_of_nearest_neighbors_from_distances
import pandas as pd

class RECOMMENDATIONFROM(object):
    def __init__(self)->CLASSINIT:
        self.__mod = EMBEDDINGMODEL
        self.__kcn = 0
    def __str__(self)->str:
        return "RECOMMENDATION MODEL - PROCESS"
    def __call__(self)->None:
        return None
    def __getstate__(self)->CLASSINIT:
        raise TypeError(TYPEERROR)
    def __repr__(self)->str:
        return RECOMMENDATIONFROM.__doc__
    def _READDATA(self,datainit:str)->FILES:
        try:
            return pd.read_csv(datainit)
        except:
            FILEERROR().print()
    def _RETURNDATA(self,datainit:str,target:str)->RESPONSES:
        dt = self._READDATA(datainit)[target]
        return dt.tolist()
    def _RUN(self,
             apikey:str,
             query:str,
             datainit:str,
             target:str,
             kne:int=1)->RESULTS:
        if isinstance(datainit,str):
            strings = self._RETURNDATA(datainit,target)
        else:
            strings = datainit[target]
        emb = [BUILDCACHEEMBEDDING(apikey)._BUILD(string) for string in strings]
        qry = BUILDCACHEEMBEDDING(apikey)._FROMSINGLE(query)
        dst = distances_from_embeddings(qry,emb,distance_metric="cosine")
        mdx = indices_of_nearest_neighbors_from_distances(dst)
        reslist = []
        msglist = []
        for _i in mdx:
            if query == strings[_i]:
                continue
            if self.__kcn >= kne:
                break
            self.__kcn += 1
            res = CLUSTERINGMODEL(apikey)._LOADMODEL(strings[_i],str(query))
            reslist.append(res)
            msglist.append(strings[_i])
        return reslist,msglist