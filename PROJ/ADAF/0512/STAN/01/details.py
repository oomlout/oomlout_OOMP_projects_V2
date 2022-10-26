
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "ADAF"
    oColor = "0512"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR0512"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Adafruit 9 DOF and 10 DOF PCBs')
    newPart['gitRepo'].append('https://github.com/adafruit/Adafruit-9-DOF-and-10-DOF-PCBs')
    newPart['gitName'].append('Adafruit-9-DOF-and-10-DOF-PCBs')
    newPart['eagleBoard'].append('/Adafuit_10DOF.brd')
    newPart['eagleSchem'].append('/Adafuit_10DOF.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

