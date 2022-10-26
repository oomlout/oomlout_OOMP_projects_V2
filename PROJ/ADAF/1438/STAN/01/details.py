
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "ADAF"
    oColor = "1438"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR1438"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Adafruit Motor Shield V2 PCB')
    newPart['gitRepo'].append('https://github.com/adafruit/Adafruit-Motor-Shield-V2-PCB')
    newPart['gitName'].append('Adafruit-Motor-Shield-V2-PCB')
    newPart['eagleBoard'].append('/Adafruit Motor Shield v2.3.brd')
    newPart['eagleSchem'].append('/Adafruit Motor Shield v2.3.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

