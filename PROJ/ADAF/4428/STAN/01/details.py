
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "ADAF"
    oColor = "4428"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR4428"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Adafruit Circuit Playground Tri Color E Ink Gizmo PCB')
    newPart['gitRepo'].append('https://github.com/adafruit/Adafruit-Circuit-Playground-Tri-Color-E-Ink-Gizmo-PCB')
    newPart['gitName'].append('Adafruit-Circuit-Playground-Tri-Color-E-Ink-Gizmo-PCB')
    newPart['eagleBoard'].append('/Circuit Playground Tri-color E-Ink Gizmo.brd')
    newPart['eagleSchem'].append('/Circuit Playground Tri-color E-Ink Gizmo.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

