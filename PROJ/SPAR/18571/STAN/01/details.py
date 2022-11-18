
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "18571"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR18571"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Inline DC Panel Meter')
    newPart['gitRepo'].append('https://github.com/sparkfun/Inline-DC-Panel-Meter')
    newPart['gitName'].append('Inline-DC-Panel-Meter')
    newPart['eagleBoard'].append('/Hardware/Inline DC Panel Meter - Display Holder.brd')
    newPart['eagleSchem'].append('/Hardware/Inline DC Panel Meter - Display Holder.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

