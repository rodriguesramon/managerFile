def readMyFileAndReturnContentInArray(file) :
    f = open(file,"r")
    result = []
    for x in open(file,"r").readlines(): 
        if(x.__contains__("Nome Saldo")) or (x.__contains__("Nome Historico")) :
            print("...")
        else :
            result.append(x.split(' '))     
    f.close()
    checkHeader(file)
    return result

def checkHeader(file):
    f = open(file,"r")
    firstLine = f.readline()
    if (firstLine.__contains__("Nome Saldo")) or (firstLine.__contains__("Nome Historico")) :
        print("firstLine: Tem")
    else:
        addFirstLine(file)
    f.close()

def addFirstLine(file) :
    with open(file, "r+") as f:
        a = f.read()
    with open(file, "w+") as f:
        if(file == "clientes.txt") :
            secondCol = "Saldo"
        else:
            secondCol = "Historico"
        f.write("Nome "+ secondCol +" \n" + a)
        
        