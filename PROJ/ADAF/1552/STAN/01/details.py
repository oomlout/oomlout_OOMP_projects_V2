
######  Auto translated oomp file

def load(newPart):
    oType = "PROJ"
    oSize = "ADAF"
    oColor = "1552"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR1552"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Adafruit TPA2012 or TS2012 Breakout PCB')
    newPart['gitRepo'].append('https://github.com/adafruit/Adafruit-TPA2012-or-TS2012-Breakout-PCB')
    newPart['gitName'].append('Adafruit-TPA2012-or-TS2012-Breakout-PCB')
    newPart['eagleBoard'].append('/Adafruit TS2012 TPA2012 Class D Audio Amp.brd')
    newPart['eagleSchem'].append('/Adafruit TS2012 TPA2012 Class D Audio Amp.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

