from __tempinitparameters import CLASSINIT,RESPONSES,RESULTS,TYPEERROR,GPTMODEL,SYSTEMMESSAGE
import openai

class GPTREVIEW(object):
    def __init__(self,apikey:str)->CLASSINIT:
        self.__api = apikey
        self.__mod = GPTMODEL
        self.__rev = "Share with me all your findings about this {textinit} I gave you"
        openai.api_key = self.__api
    def __str__(self)->str:
        return "GPT REVIEW - PROCESS"
    def __call__(self)->None:
        return None
    def __getstate__(self)->CLASSINIT:
        raise TypeError(TYPEERROR)
    def __repr__(self)->str:
        return GPTREVIEW.__doc__
    def _RETURNMESSAGE(self,inittext:str)->RESPONSES:
        usrmsg = self.__rev.format(textinit=inittext)
        sysmsg = SYSTEMMESSAGE
        sys_all = [{"role":"system","content":sysmsg}]
        usr_all = [{"role":"user","content":usrmsg}]
        return sys_all+usr_all
    def _CREATE(self,inittext:str)->RESULTS:
        msg = self._RETURNMESSAGE(inittext)
        try:
            cn = openai.ChatCompletion.create(model=self.__mod,
                                              messages=msg,
                                              temperature=0.1,
                                              n=1)
            if cn["choices"][0]["finish_reason"].lower() == "stop":
                ans = cn["choices"][0]["message"]["content"]
            else:
                ans = "Sorry, cannot response for that"
            return ans
        except Exception as err:
            print(str(err))
            pass