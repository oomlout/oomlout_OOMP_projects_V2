
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "12924"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR12924"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('MicroView USB Programmer')
    newPart['gitRepo'].append('https://github.com/sparkfun/MicroView_USB_Programmer')
    newPart['gitName'].append('MicroView_USB_Programmer')
    newPart['eagleBoard'].append('/Hardware/SparkFun_MicroViewUSB.brd')
    newPart['eagleSchem'].append('/Hardware/SparkFun_MicroViewUSB.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

