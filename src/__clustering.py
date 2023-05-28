from __tempinitparameters import CLASSINIT,TYPEERROR,TEXTENGINE,RESPONSES
import openai

class CLUSTERINGMODEL(object):
    def __init__(self,apikey:str)->CLASSINIT:
        self.__api = apikey
        self.__md = TEXTENGINE
        self.__rv = 'Use that format "I found evidence about {userinputinit}". Describe the main subject and emotion of this text presented to you, give a summary, dont leave your comment missing.Text:\n"""\n{reviewsinit}\n"""\n"""\nEmotion: \n"""\nSubject: \n"""\n'
        openai.api_key = self.__api
    def __str__(self)->str:
        return "CLUSTERING MODEL - PROCESS"
    def __call__(self)->None:
        return None
    def __getstate__(self)->CLASSINIT:
        raise TypeError(TYPEERROR)
    def __repr__(self)->str:
        return CLUSTERINGMODEL.__doc__
    def _RETURNPROMPT(self,tpinit:str,usinit:str)->RESPONSES:
        return self.__rv.format(reviewsinit=tpinit,
                                userinputinit=usinit)
    def _LOADMODEL(self,
                   pr:str,
                   iu:str,
                   tp:int=0,
                   mt:int=1024,
                   pt:int=1,
                   fq:int=0,
                   pq:int=0)->RESPONSES:
        try:
            prompt = self._RETURNPROMPT(pr,iu)
            rp = openai.Completion.create(engine=self.__md,
                                          prompt=prompt,
                                          temperature=tp,
                                          max_tokens=mt,
                                          top_p=pt,
                                          frequency_penalty=fq,
                                          presence_penalty=pq)
            return rp["choices"][0]["text"]
        except:
            pass
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        