
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "ADAF"
    oColor = "0572"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR0572"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Adafruit BeagleBone ProtoBoard PCB')
    newPart['gitRepo'].append('https://github.com/adafruit/Adafruit-BeagleBone-ProtoBoard-PCB')
    newPart['gitName'].append('Adafruit-BeagleBone-ProtoBoard-PCB')
    newPart['eagleBoard'].append('/Adafruit-BeagleBone-ProtoBoard-v0.1.brd')
    newPart['eagleSchem'].append('/Adafruit-BeagleBone-ProtoBoard-v0.1.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

