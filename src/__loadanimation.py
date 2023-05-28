from __tempinitparameters import CLASSINIT,TYPEERROR,RESPONSES,RESULTS,ANIMATIONURL,ANIMATIONAND
import requests
from streamlit_lottie import st_lottie

class LOADANIMATION(object):
    def __init__(self)->CLASSINIT:
        self.__url = ANIMATIONURL
        self.__mrl = ANIMATIONAND
        self.__ujs = dict()
        self.__mjs = dict()
    def __str__(self)->str:
        return "LOAD ANIMATION - PROCESS"
    def __call__(self)->None:
        return None
    def __getstate__(self)->CLASSINIT:
        raise TypeError(TYPEERROR)
    def __repr__(self)->str:
        return LOADANIMATION.__doc__
    def _GETMAIN(self)->RESPONSES:
        uget = requests.get(self.__url)
        if uget.status_code == 200:
            self.__ujs = uget.json()
        else:
            pass
    def _GETADS(self)->RESPONSES:
        umgt = requests.get(self.__mrl)
        if umgt.status_code == 200:
            self.__mjs = umgt.json()
        else:
            pass
    def _RUNMAIN(self)->RESULTS:
        try:
            self._GETMAIN()
            return st_lottie(self.__ujs,
                             loop=True,
                             quality="high",
                             key="mainlogo",
                             height=200,
                             width=200)
        except Exception as err:
            print(str(err))
            pass
    def _RUNADS(self)->RESULTS:
        try:
            self._GETADS()
            return st_lottie(self.__mjs,
                             loop=True,
                             quality="high",
                             key="adslogo",
                             height=200,
                             width=200)
        except Exception as err:
            print(str(err))
            pass