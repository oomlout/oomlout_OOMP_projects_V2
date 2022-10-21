
######  Auto translated oomp file

def load(newPart):
    oType = "PROJ"
    oSize = "ADAF"
    oColor = "4569"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR4569"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Adafruit ISM330DHCX LIS3MDL FeatherWing PCB')
    newPart['gitRepo'].append('https://github.com/adafruit/Adafruit-ISM330DHCX-LIS3MDL-FeatherWing-PCB')
    newPart['gitName'].append('Adafruit-ISM330DHCX-LIS3MDL-FeatherWing-PCB')
    newPart['eagleBoard'].append('/Adafruit ISM330DHCX + LIS3MDL FeatherWing.brd')
    newPart['eagleSchem'].append('/Adafruit ISM330DHCX + LIS3MDL FeatherWing.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

