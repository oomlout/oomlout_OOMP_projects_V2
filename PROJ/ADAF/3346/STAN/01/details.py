
######  Auto translated oomp file

def load(newPart):
    oType = "PROJ"
    oSize = "ADAF"
    oColor = "3346"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR3346"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Adafruit Stereo Speaker Bonnet PCB')
    newPart['gitRepo'].append('https://github.com/adafruit/Adafruit-Stereo-Speaker-Bonnet-PCB')
    newPart['gitName'].append('Adafruit-Stereo-Speaker-Bonnet-PCB')
    newPart['eagleBoard'].append('/Adafruit Speaker Bonnet Original.brd')
    newPart['eagleSchem'].append('/Adafruit Speaker Bonnet Original.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

