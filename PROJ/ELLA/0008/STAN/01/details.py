
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "ELLA"
    oColor = "0008"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR0008"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('pic16-usb-module')
    newPart['gitRepo'].append('https://github.com/electrolama/pic16-usb-module')
    newPart['gitName'].append('pic16-usb-module')
    newPart['eagleBoard'].append('pum.brd')
    newPart['eagleSchem'].append('pum.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

