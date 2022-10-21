
######  Auto translated oomp file

def load(newPart):
    oType = "PROJ"
    oSize = "ADAF"
    oColor = "3386"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR3386"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Adafruit PiRTC RTC for Raspberry Pi PCB')
    newPart['gitRepo'].append('https://github.com/adafruit/Adafruit-PiRTC-RTC-for-Raspberry-Pi-PCB')
    newPart['gitName'].append('Adafruit-PiRTC-RTC-for-Raspberry-Pi-PCB')
    newPart['eagleBoard'].append('/Adafruit PiRTC PCF8523.brd')
    newPart['eagleSchem'].append('/Adafruit PiRTC PCF8523.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

