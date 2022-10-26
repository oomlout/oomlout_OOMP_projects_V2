
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "0449"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR0449"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('RS232 Shifter SMD')
    newPart['gitRepo'].append('https://github.com/sparkfun/RS232_Shifter_SMD')
    newPart['gitName'].append('RS232_Shifter_SMD')
    newPart['eagleBoard'].append('/Hardware/Sparkfun_RS232.brd')
    newPart['eagleSchem'].append('/Hardware/Sparkfun_RS232.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

