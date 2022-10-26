
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "18708"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR18708"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('MicroMod Function Ethernet W5500')
    newPart['gitRepo'].append('https://github.com/sparkfun/MicroMod_Function_Ethernet-W5500')
    newPart['gitName'].append('MicroMod_Function_Ethernet-W5500')
    newPart['eagleBoard'].append('/Hardware/MicroMod-Ethernet-Function-Board-W5500.brd')
    newPart['eagleSchem'].append('/Hardware/MicroMod-Ethernet-Function-Board-W5500.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

