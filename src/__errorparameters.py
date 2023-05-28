class NETWORKERROR(object):
    n_ = "[NETWORK ERROR - CHECK YOUR CONNECTION]"
    def print(self):
        raise SystemError(self.n_)
class FILEERROR(object):
    n_ = "[FILE ERROR - CHECK YOUR FILE TYPE OR LOCATION]"
    def print(self):
        raise FileNotFoundError(self.n_)
class PACKAGEERROR(object):
    n_ = "[PACKAGE ERROR - CHECK YOUR REQUIREMENTS]"
    def print(self):
        raise ModuleNotFoundError(self.n_)
class SYSTEMERROR(object):
    n_ = "[SYSTEM ERROR - CHECK YOUR SYSTEM]"
    def print(self):
        raise OSError(self.n_)