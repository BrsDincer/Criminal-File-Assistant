from __tempinitparameters import CLASSINIT,RULESOF,USERWARNINGINITIAL,RESPONSES,RESULTS,TYPEERROR,FILEERROR
from __recommodel import RECOMMENDATIONFROM
from __gptreview import GPTREVIEW
from __loadanimation import LOADANIMATION
import streamlit as st
import pandas as pd

class APPRUN(object):
    def __init__(self)->CLASSINIT:
        self.__p = "AE-ASSISTANT"
        self.__l = "wide"
        self.__s = "expanded"
    def __str__(self)->str:
        return "APP ACTIVATION - PROCESS"
    def __call__(self)->None:
        return None
    def __getstate__(self)->CLASSINIT:
        raise TypeError(TYPEERROR)
    def __repr__(self)->str:
        return APPRUN.__doc__
    def _CONVERT(self,bdata:str)->RESPONSES:
        if bdata is not None:
            try:
                return pd.read_csv(bdata)
            except:
                FILEERROR().print()
    def _CONF(self)->RESPONSES:
        st.set_page_config(page_title=self.__p,
                           layout=self.__l,
                           initial_sidebar_state=self.__s,
                           menu_items={"About":"Criminal File Investigation"})
    def _INITIALPROCESS(self)->RESULTS:
        mol1,mol2,mol3 = st.columns(3)
        with mol1:
            st.title("Criminal File Investigation")
            st.subheader("Artificial Intelligence Assistant")
        with mol2:
            LOADANIMATION()._RUNMAIN()
        with mol3:
            LOADANIMATION()._RUNADS()
        st.caption(USERWARNINGINITIAL)
        st.caption(RULESOF)
        col1,col2 = st.columns(2)
        with col1:
            apikey = st.text_input("Type your OPENAI API KEY",key="apikeyname",type="password")
        with col2:
            upfile = st.file_uploader("Browse")
        if (upfile is not None) and (apikey is not None) and (apikey != "") and (apikey != " "):
            pass
        else:
            st.info("You need to enter API key parameter and upload a file to continue",
                    icon="🟢")
        if (upfile is not None) and (apikey is not None) and (apikey != "") and (apikey != " "):
            dtfile = self._CONVERT(upfile)
            scol1,scol2 = st.columns(2)
            with scol1:
                clmn = st.text_input("What is your target column?",key="columnname")
            with scol2:
                usrt = st.text_input("What do you want to search?",key="targetname")
            with st.spinner("Loading data..."):
                st.success('Upload has been completed',icon="✅")
                st.dataframe(dtfile,use_container_width=True)
            st.divider()
            kneval = st.slider("How many similar proofs related to your target do you want?",
                               1,int(len(dtfile))-2,1)
            runbt = st.button("Search")
            isres = ""
            if (clmn != None) and (clmn != "") and (clmn != " ") and (usrt != None) and (usrt != "") and (usrt != " "):
                if runbt:
                    st.info('Collection of replies may be delayed when the file size is large',icon="🟢")
                    with st.spinner("Waiting for results..."):
                        try:
                            responsemodel,messagemodel = RECOMMENDATIONFROM()._RUN(apikey=str(apikey),
                                                                                   query=str(usrt),
                                                                                   datainit=dtfile,
                                                                                   target=str(clmn),
                                                                                   kne=int(kneval))
                            for ix_,mx_ in zip(responsemodel,messagemodel):
                                rmsg = GPTREVIEW(str(apikey))._CREATE(str(mx_))
                                isres += f"""
    
:small_blue_diamond:
    
**ORIGINAL TEXT** :scroll:
        
{str(mx_)}
    
**FOUND** :mag_right:
        
{str(ix_)}
    
**REVIEW** :small_red_triangle_down:
    
{str(rmsg)}
    
                              
                                
                                """
                            st.divider()
                            st.title(":triangular_flag_on_post: Results")
                            st.write(isres)
                            st.divider()
                        except Exception as err:
                            st.error(str(err))
                            pass
            
            
if __name__ == "__main__":
    APPRUN()._CONF()
    APPRUN()._INITIALPROCESS()
            
