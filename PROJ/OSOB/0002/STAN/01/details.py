
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "OSOB"
    oColor = "0002"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR0002"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Lcd featherwing')
    newPart['gitRepo'].append('https://github.com/joeycastillo/LCD-FeatherWing')
    newPart['gitName'].append('LCD-FeatherWing')
    newPart['eagleBoard'].append('OSO-WILD-A3/OSO-WILD-A3.brd')
    newPart['eagleSchem'].append('OSO-WILD-A3/OSO-WILD-A3.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

