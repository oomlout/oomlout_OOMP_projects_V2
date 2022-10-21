
######  Auto translated oomp file

def load(newPart):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "16281"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR16281"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('SparkFun Real Time Clock Module RV 8803')
    newPart['gitRepo'].append('https://github.com/sparkfun/SparkFun_Real_Time_Clock_Module_RV-8803')
    newPart['gitName'].append('SparkFun_Real_Time_Clock_Module_RV-8803')
    newPart['eagleBoard'].append('/Hardware/Qwiic_RTC_RV8803.brd')
    newPart['eagleSchem'].append('/Hardware/Qwiic_RTC_RV8803.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

