
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "ADAF"
    oColor = "5568"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR5568"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Adafruit WCH CH9102F Friend PCB')
    newPart['gitRepo'].append('https://github.com/adafruit/Adafruit-WCH-CH9102F-Friend-PCB')
    newPart['gitName'].append('Adafruit-WCH-CH9102F-Friend-PCB')
    newPart['eagleBoard'].append('/Adafruit CH9102F.brd')
    newPart['eagleSchem'].append('/Adafruit CH9102F.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

