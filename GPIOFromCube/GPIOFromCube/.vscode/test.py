with open("test.txt","r") as f:
    fcontent = f.read()
    print(fcontent)
    fcontent = fcontent.replace("buld/swj-dp.tcl","swj-dp.tcl")
with open("test.txt","w") as f:
    print(fcontent)
    f.write(fcontent)
