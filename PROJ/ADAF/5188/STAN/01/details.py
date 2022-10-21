
######  Auto translated oomp file

def load(newPart):
    oType = "PROJ"
    oSize = "ADAF"
    oColor = "5188"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR5188"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Adafruit DS3231 Precision RTC Breakout PCB')
    newPart['gitRepo'].append('https://github.com/adafruit/Adafruit-DS3231-Precision-RTC-Breakout-PCB')
    newPart['gitName'].append('Adafruit-DS3231-Precision-RTC-Breakout-PCB')
    newPart['eagleBoard'].append('/Adafruit DS3231 RTC Breakout.brd')
    newPart['eagleSchem'].append('/Adafruit DS3231 RTC Breakout.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

