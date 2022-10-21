
######  Auto translated oomp file

def load(newPart):
    oType = "PROJ"
    oSize = "ADAF"
    oColor = "1465"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR1465"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Adafruit ISP SWD and JTAG Breakout PCBs')
    newPart['gitRepo'].append('https://github.com/adafruit/Adafruit-ISP-SWD-and-JTAG-Breakout-PCBs')
    newPart['gitName'].append('Adafruit-ISP-SWD-and-JTAG-Breakout-PCBs')
    newPart['eagleBoard'].append('/Adafruit 6-ISP AVR.brd')
    newPart['eagleSchem'].append('/Adafruit 6-ISP AVR.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

