
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "10587"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR10587"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Music Instrument Shield')
    newPart['gitRepo'].append('https://github.com/sparkfun/Music_Instrument_Shield')
    newPart['gitName'].append('Music_Instrument_Shield')
    newPart['eagleBoard'].append('/Hardware/SparkFun_Music_Instrument_Shield.brd')
    newPart['eagleSchem'].append('/Hardware/SparkFun_Music_Instrument_Shield.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

