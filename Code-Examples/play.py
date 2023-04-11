import os

print(os.system)

def testme(name):
    def fistname():
        print("From insite firstname", name)
    
    print("control check")
    fistname()

testme("partha")