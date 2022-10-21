
######  Auto translated oomp file

def load(newPart):
    oType = "PROJ"
    oSize = "ADAF"
    oColor = "3056"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR3056"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Adafruit WICED WiFi Feather PCB')
    newPart['gitRepo'].append('https://github.com/adafruit/Adafruit-WICED-WiFi-Feather-PCB')
    newPart['gitName'].append('Adafruit-WICED-WiFi-Feather-PCB')
    newPart['eagleBoard'].append('/Adafruit WICED WiFi Feather.brd')
    newPart['eagleSchem'].append('/Adafruit WICED WiFi Feather.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

