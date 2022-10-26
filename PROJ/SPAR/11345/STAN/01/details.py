
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "11345"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR11345"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Geiger Counter')
    newPart['gitRepo'].append('https://github.com/sparkfun/Geiger_Counter')
    newPart['gitName'].append('Geiger_Counter')
    newPart['eagleBoard'].append('/Hardware/Geiger_Counter.brd')
    newPart['eagleSchem'].append('/Hardware/Geiger_Counter.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

