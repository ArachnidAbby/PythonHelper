class Input:
    def __init__(self, quitWord):
        self.quit = quitWord
        self.funcs = []
    def input(self,*args):
        string = ""
        for x in args:string +=x
        preoutput = input((string))
        if self.quit == preoutput: quit()
        for x in self.funcs:
            if x[0]==preoutput:
                x[1](preoutput)

    def addFunction(self, Name, func):
        self.funcs.append((Name,func))
