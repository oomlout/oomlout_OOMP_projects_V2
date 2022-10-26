
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "13717"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR13717"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Pi Wedge 40 Pin PreAssembled')
    newPart['gitRepo'].append('https://github.com/sparkfun/Pi_Wedge_40-Pin_PreAssembled')
    newPart['gitName'].append('Pi_Wedge_40-Pin_PreAssembled')
    newPart['eagleBoard'].append('/hardware/SparkFun_Pi_Wedge_40-Pin_PreAssembled.brd')
    newPart['eagleSchem'].append('/hardware/SparkFun_Pi_Wedge_40-Pin_PreAssembled.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

