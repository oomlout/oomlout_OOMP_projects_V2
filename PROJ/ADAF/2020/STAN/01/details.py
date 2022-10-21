
######  Auto translated oomp file

def load(newPart):
    oType = "PROJ"
    oSize = "ADAF"
    oColor = "2020"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR2020"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Adafruit Flora LSM9DS0 9DOF PCB')
    newPart['gitRepo'].append('https://github.com/adafruit/Adafruit-Flora-LSM9DS0-9DOF-PCB')
    newPart['gitName'].append('Adafruit-Flora-LSM9DS0-9DOF-PCB')
    newPart['eagleBoard'].append('/Adafruit Flora LSM9DS0 9DoF.brd')
    newPart['eagleSchem'].append('/Adafruit Flora LSM9DS0 9DoF.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

