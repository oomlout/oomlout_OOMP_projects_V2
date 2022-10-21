
######  Auto translated oomp file

def load(newPart):
    oType = "PROJ"
    oSize = "ADAF"
    oColor = "4836"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR4836"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Adafruit Wii Nunchuck Breakout Adapter PCB')
    newPart['gitRepo'].append('https://github.com/adafruit/Adafruit-Wii-Nunchuck-Breakout-Adapter-PCB')
    newPart['gitName'].append('Adafruit-Wii-Nunchuck-Breakout-Adapter-PCB')
    newPart['eagleBoard'].append('/Adafruit Wii Nunchuck Breakout Adapter.brd')
    newPart['eagleSchem'].append('/Adafruit Wii Nunchuck Breakout Adapter.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

