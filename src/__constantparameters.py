import os
BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA = os.path.join(BASE,"data")
CONTENT = os.path.join(BASE,"pckfile")
TYPEERROR = "[PROJECT BASED - RELATIONS WITH SCRIPT]"
ANIMATIONURL = "https://assets1.lottiefiles.com/packages/lf20_yhTqG2.json"
ANIMATIONAND = "https://assets2.lottiefiles.com/private_files/lf30_5idufzr4.json"
EMBEDDINGFILE = os.path.join(CONTENT,"build_cache.pkl")
EMBEDDINGMODEL = "text-embedding-ada-002"
TEXTENGINE = "text-davinci-003"
GPTMODEL = "gpt-3.5-turbo"

SYSTEMMESSAGE = ""
SYSTEMMESSAGE += "You are a world famous most successful detective,"
SYSTEMMESSAGE += "and you are trying to learn and predict the outcome of the event"
SYSTEMMESSAGE += "from the news headlines given to you."
SYSTEMMESSAGE += "If it has a historical background,"
SYSTEMMESSAGE += "quote it within the framework of the evidence."
SYSTEMMESSAGE += "You report your examinations and evidence in descriptive language"
SYSTEMMESSAGE += "after you have finished your examination."

USERWARNINGINITIAL = ":loudspeaker: This system is algorithmically orchestrated, "
USERWARNINGINITIAL += "architected to meticulously _parse_, _decipher_, "
USERWARNINGINITIAL += "and _extrapolate_ the intricate nuances you seek based on your specified research paradigm, "
USERWARNINGINITIAL += "from within the labyrinthine, multi-layered repositories of evidentiary documents."

RULESOF = ":loudspeaker: Only **csv** files are accepted as the first sharing stage. "
RULESOF += "Make sure that the file you upload is **csv** and enter the column names correctly."
