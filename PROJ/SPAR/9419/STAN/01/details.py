
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "9419"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR9419"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('MicroSD Sniffer')
    newPart['gitRepo'].append('https://github.com/sparkfun/MicroSD_Sniffer')
    newPart['gitName'].append('MicroSD_Sniffer')
    newPart['eagleBoard'].append('/Hardware/SparkFun_MicroSD_Sniffer.brd')
    newPart['eagleSchem'].append('/Hardware/SparkFun_MicroSD_Sniffer.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

