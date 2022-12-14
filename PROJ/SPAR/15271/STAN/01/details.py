
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "15271"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR15271"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('gator particle')
    newPart['gitRepo'].append('https://github.com/sparkfun/gator_particle')
    newPart['gitName'].append('gator_particle')
    newPart['eagleBoard'].append('/Hardware/GatorParticle.brd')
    newPart['eagleSchem'].append('/Hardware/GatorParticle.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

