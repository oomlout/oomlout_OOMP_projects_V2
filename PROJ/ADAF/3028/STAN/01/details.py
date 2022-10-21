
######  Auto translated oomp file

def load(newPart):
    oType = "PROJ"
    oSize = "ADAF"
    oColor = "3028"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR3028"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Adafruit DS3231 Precision RTC FeatherWing PCB')
    newPart['gitRepo'].append('https://github.com/adafruit/Adafruit-DS3231-Precision-RTC-FeatherWing-PCB')
    newPart['gitName'].append('Adafruit-DS3231-Precision-RTC-FeatherWing-PCB')
    newPart['eagleBoard'].append('/Adafruit DS3231 RTC FeatherWing.brd')
    newPart['eagleSchem'].append('/Adafruit DS3231 RTC FeatherWing.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

