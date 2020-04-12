import PythonHelper

def Purple(input):
    print("AIR IS PURPLE")

time =PythonHelper.Clock.Time() 
Inputer = PythonHelper.modifiedTools.Input("quitFile")
Inputer.addFunction("purple",Purple)

while True:
    time.UpdateTimesStuff()
    Inputer.input("input: ")
    print("you waited:"+ str(time.DeltaTime) + " seconds")
