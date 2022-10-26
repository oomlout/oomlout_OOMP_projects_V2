
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "12081"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR12081"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('USB Weather Board')
    newPart['gitRepo'].append('https://github.com/sparkfun/USB_Weather_Board')
    newPart['gitName'].append('USB_Weather_Board')
    newPart['eagleBoard'].append('/hardware/USB-Weather-v31.brd')
    newPart['eagleSchem'].append('/hardware/USB-Weather-v31.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

