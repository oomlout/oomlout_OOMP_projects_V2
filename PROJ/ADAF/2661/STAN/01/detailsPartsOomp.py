def load(newPart,it):
    it['PROJ-ADAF-2661-STAN-01']['oompParts'] = [{'JP3': {'OOMPID': 'HEAD-I01-X-PI16-01', 'FULL': {'DESC': '', 'PART': 'JP3', 'DEVICE': '1X16_ROUND ', 'PACKAGE': '1X16_ROUND', 'PARTLETTER': 'JP', 'VALUE': '', 'VALUENUMBER': '', 'PACKAGENUMBER': '116', 'BOM': '', 'OWNER': 'ADAF', 'FULL': 'JP3,,1X16_ROUND ,1X16_ROUND,,,'}},
       'JP1': {'OOMPID': 'HEAD-I01-X-PI16-01', 'FULL': {'DESC': '', 'PART': 'JP1', 'DEVICE': '1X16_ROUND ', 'PACKAGE': '1X16_ROUND', 'PARTLETTER': 'JP', 'VALUE': '', 'VALUENUMBER': '', 'PACKAGENUMBER': '116', 'BOM': '', 'OWNER': 'ADAF', 'FULL': 'JP1,,1X16_ROUND ,1X16_ROUND,,,'}},
       'R1': {'OOMPID': 'RESE-0805-X-O222-01', 'FULL': {'DESC': '', 'PART': 'R1', 'DEVICE': '0805-NO 2.2K', 'PACKAGE': '0805-NO', 'PARTLETTER': 'R', 'VALUE': '2.2K', 'VALUENUMBER': '2.2', 'PACKAGENUMBER': '0805', 'BOM': '', 'OWNER': 'ADAF', 'FULL': 'R1,2.2K,0805-NO 2.2K,0805-NO,,,'}},
       'R10': {'OOMPID': 'RESE-0805-X-O222-01', 'FULL': {'DESC': '', 'PART': 'R10', 'DEVICE': '0805-NO 2.2K', 'PACKAGE': '0805-NO', 'PARTLETTER': 'R', 'VALUE': '2.2K', 'VALUENUMBER': '2.2', 'PACKAGENUMBER': '0805', 'BOM': '', 'OWNER': 'ADAF', 'FULL': 'R10,2.2K,0805-NO 2.2K,0805-NO,,,'}},
       'R7': {'OOMPID': 'RESE-0805-X-O222-01', 'FULL': {'DESC': '', 'PART': 'R7', 'DEVICE': '0805-NO 2.2K', 'PACKAGE': '0805-NO', 'PARTLETTER': 'R', 'VALUE': '2.2K', 'VALUENUMBER': '2.2', 'PACKAGENUMBER': '0805', 'BOM': '', 'OWNER': 'ADAF', 'FULL': 'R7,2.2K,0805-NO 2.2K,0805-NO,,,'}},
       'R6': {'OOMPID': 'RESE-0805-X-O222-01', 'FULL': {'DESC': '', 'PART': 'R6', 'DEVICE': '0805-NO 2.2K', 'PACKAGE': '0805-NO', 'PARTLETTER': 'R', 'VALUE': '2.2K', 'VALUENUMBER': '2.2', 'PACKAGENUMBER': '0805', 'BOM': '', 'OWNER': 'ADAF', 'FULL': 'R6,2.2K,0805-NO 2.2K,0805-NO,,,'}},
       'IC1': {'OOMPID': 'UNMATCHED-UNMATCHED-X-UNMATCHED-01', 'FULL': {'DESC': '', 'PART': 'IC1', 'DEVICE': 'TQFP44 ATMEGA32U4-AU', 'PACKAGE': 'TQFP44', 'PARTLETTER': 'IC', 'VALUE': 'ATMEGA32U4-AU', 'VALUENUMBER': '324-', 'PACKAGENUMBER': '44', 'BOM': '', 'OWNER': 'ADAF', 'FULL': 'IC1,ATMEGA32U4-AU,TQFP44 ATMEGA32U4-AU,TQFP44,,,'}},
       'C9': {'OOMPID': 'CAPC-0805-X-UF1-V25', 'FULL': {'DESC': '', 'PART': 'C9', 'DEVICE': '0805-NO 1uF', 'PACKAGE': '0805-NO', 'PARTLETTER': 'C', 'VALUE': '1uF', 'VALUENUMBER': '1', 'PACKAGENUMBER': '0805', 'BOM': '', 'OWNER': 'ADAF', 'FULL': 'C9,1uF,0805-NO 1uF,0805-NO,,,'}},
       'C2': {'OOMPID': 'CAPC-0805-X-UF1-V25', 'FULL': {'DESC': '', 'PART': 'C2', 'DEVICE': '0805-NO 1uF', 'PACKAGE': '0805-NO', 'PARTLETTER': 'C', 'VALUE': '1uF', 'VALUENUMBER': '1', 'PACKAGENUMBER': '0805', 'BOM': '', 'OWNER': 'ADAF', 'FULL': 'C2,1uF,0805-NO 1uF,0805-NO,,,'}},
       'R4': {'OOMPID': 'RESE-0805-X-O220-01', 'FULL': {'DESC': '', 'PART': 'R4', 'DEVICE': '0805-NO 22', 'PACKAGE': '0805-NO', 'PARTLETTER': 'R', 'VALUE': '22', 'VALUENUMBER': '22', 'PACKAGENUMBER': '0805', 'BOM': '', 'OWNER': 'ADAF', 'FULL': 'R4,22,0805-NO 22,0805-NO,,,'}},
       'R5': {'OOMPID': 'RESE-0805-X-O220-01', 'FULL': {'DESC': '', 'PART': 'R5', 'DEVICE': '0805-NO 22', 'PACKAGE': '0805-NO', 'PARTLETTER': 'R', 'VALUE': '22', 'VALUENUMBER': '22', 'PACKAGENUMBER': '0805', 'BOM': '', 'OWNER': 'ADAF', 'FULL': 'R5,22,0805-NO 22,0805-NO,,,'}},
       'C14': {'OOMPID': 'CAPC-0805-X-NF100-V50', 'FULL': {'DESC': '', 'PART': 'C14', 'DEVICE': '0805-NO 0.1uF', 'PACKAGE': '0805-NO', 'PARTLETTER': 'C', 'VALUE': '0.1uF', 'VALUENUMBER': '0.1', 'PACKAGENUMBER': '0805', 'BOM': '', 'OWNER': 'ADAF', 'FULL': 'C14,0.1uF,0805-NO 0.1uF,0805-NO,,,'}},
       'C15': {'OOMPID': 'CAPC-0805-X-NF100-V50', 'FULL': {'DESC': '', 'PART': 'C15', 'DEVICE': '0805-NO 0.1uF', 'PACKAGE': '0805-NO', 'PARTLETTER': 'C', 'VALUE': '0.1uF', 'VALUENUMBER': '0.1', 'PACKAGENUMBER': '0805', 'BOM': '', 'OWNER': 'ADAF', 'FULL': 'C15,0.1uF,0805-NO 0.1uF,0805-NO,,,'}},
       'C8': {'OOMPID': 'CAPC-0805-X-UNMATCHED-01', 'FULL': {'DESC': '', 'PART': 'C8', 'DEVICE': '0805-NO 10ÂµF', 'PACKAGE': '0805-NO', 'PARTLETTER': 'C', 'VALUE': '10ÂUF', 'VALUENUMBER': '10Âµ', 'PACKAGENUMBER': '0805', 'BOM': '', 'OWNER': 'ADAF', 'FULL': 'C8,10ÂµF,0805-NO 10ÂµF,0805-NO,,,'}},
       'C7': {'OOMPID': 'CAPC-0805-X-UNMATCHED-01', 'FULL': {'DESC': '', 'PART': 'C7', 'DEVICE': '0805-NO 10ÂµF', 'PACKAGE': '0805-NO', 'PARTLETTER': 'C', 'VALUE': '10ÂUF', 'VALUENUMBER': '10Âµ', 'PACKAGENUMBER': '0805', 'BOM': '', 'OWNER': 'ADAF', 'FULL': 'C7,10ÂµF,0805-NO 10ÂµF,0805-NO,,,'}},
       'C10': {'OOMPID': 'CAPC-0805-X-NF100-V50', 'FULL': {'DESC': '', 'PART': 'C10', 'DEVICE': '0805_10MGAP 0.1uF', 'PACKAGE': '0805_10MGAP', 'PARTLETTER': 'C', 'VALUE': '0.1uF', 'VALUENUMBER': '0.1', 'PACKAGENUMBER': '080510', 'BOM': '', 'OWNER': 'ADAF', 'FULL': 'C10,0.1uF,0805_10MGAP 0.1uF,0805_10MGAP,,,'}},
       'X3': {'OOMPID': 'UNMATCHED-UNMATCHED-X-UNMATCHED-01', 'FULL': {'DESC': '', 'PART': 'X3', 'DEVICE': '4UCONN_20329 microUSB', 'PACKAGE': '4UCONN_20329', 'PARTLETTER': 'X', 'VALUE': 'microUSB', 'VALUENUMBER': '', 'PACKAGENUMBER': '420329', 'BOM': '', 'OWNER': 'ADAF', 'FULL': 'X3,microUSB,4UCONN_20329 microUSB,4UCONN_20329,,,'}},
       'Y1': {'OOMPID': 'UNMATCHED-UNMATCHED-X-UNMATCHED-01', 'FULL': {'DESC': '', 'PART': 'Y1', 'DEVICE': 'RESONATOR-SMD 8MHz', 'PACKAGE': 'RESONATOR-SMD', 'PARTLETTER': 'Y', 'VALUE': '8MHz', 'VALUENUMBER': '8', 'PACKAGENUMBER': '', 'BOM': '', 'OWNER': 'ADAF', 'FULL': 'Y1,8MHz,RESONATOR-SMD 8MHz,RESONATOR-SMD,,,'}},
       'L0': {'OOMPID': 'UNMATCHED-0805-X-UNMATCHED-01', 'FULL': {'DESC': '', 'PART': 'L0', 'DEVICE': 'CHIPLED_0805_NOOUTLINE RED', 'PACKAGE': 'CHIPLED_0805_NOOUTLINE', 'PARTLETTER': 'L', 'VALUE': 'RED', 'VALUENUMBER': '', 'PACKAGENUMBER': '0805', 'BOM': '', 'OWNER': 'ADAF', 'FULL': 'L0,RED,CHIPLED_0805_NOOUTLINE RED,CHIPLED_0805_NOOUTLINE,,,'}},
       'D1': {'OOMPID': 'LEDS-0805-R-STAN-01', 'FULL': {'DESC': '', 'PART': 'D1', 'DEVICE': 'CHIPLED_0805_NOOUTLINE RED', 'PACKAGE': 'CHIPLED_0805_NOOUTLINE', 'PARTLETTER': 'D', 'VALUE': 'RED', 'VALUENUMBER': '', 'PACKAGENUMBER': '0805', 'BOM': '', 'OWNER': 'ADAF', 'FULL': 'D1,RED,CHIPLED_0805_NOOUTLINE RED,CHIPLED_0805_NOOUTLINE,,,'}},
       'C6': {'OOMPID': 'CAPC-0805-X-UNMATCHED-01', 'FULL': {'DESC': '', 'PART': 'C6', 'DEVICE': '_0805MP 10ÂµF', 'PACKAGE': '_0805MP', 'PARTLETTER': 'C', 'VALUE': '10ÂUF', 'VALUENUMBER': '10Âµ', 'PACKAGENUMBER': '0805', 'BOM': '', 'OWNER': 'ADAF', 'FULL': 'C6,10ÂµF,_0805MP 10ÂµF,_0805MP,,,'}},
       'D4': {'OOMPID': 'DIOD-S123-X-KMBR120-01', 'FULL': {'DESC': '', 'PART': 'D4', 'DEVICE': 'SOD-123 MBR120', 'PACKAGE': 'SOD-123', 'PARTLETTER': 'D', 'VALUE': 'MBR120', 'VALUENUMBER': '120', 'PACKAGENUMBER': '123', 'BOM': '', 'OWNER': 'ADAF', 'FULL': 'D4,MBR120,SOD-123 MBR120,SOD-123,,,'}},
       'D3': {'OOMPID': 'DIOD-S123-X-KMBR120-01', 'FULL': {'DESC': '', 'PART': 'D3', 'DEVICE': 'SOD-123 MBR120', 'PACKAGE': 'SOD-123', 'PARTLETTER': 'D', 'VALUE': 'MBR120', 'VALUENUMBER': '120', 'PACKAGENUMBER': '123', 'BOM': '', 'OWNER': 'ADAF', 'FULL': 'D3,MBR120,SOD-123 MBR120,SOD-123,,,'}},
       'PWR0': {'OOMPID': 'UNMATCHED-0805-X-UNMATCHED-01', 'FULL': {'DESC': '', 'PART': 'PWR0', 'DEVICE': 'CHIPLED_0805_NOOUTLINE GREEN', 'PACKAGE': 'CHIPLED_0805_NOOUTLINE', 'PARTLETTER': 'PWR', 'VALUE': 'GREEN', 'VALUENUMBER': '', 'PACKAGENUMBER': '0805', 'BOM': '', 'OWNER': 'ADAF', 'FULL': 'PWR0,GREEN,CHIPLED_0805_NOOUTLINE GREEN,CHIPLED_0805_NOOUTLINE,,,'}},
       'D2': {'OOMPID': 'LEDS-0805-L-STAN-01', 'FULL': {'DESC': '', 'PART': 'D2', 'DEVICE': 'CHIPLED_0805_NOOUTLINE BLUE', 'PACKAGE': 'CHIPLED_0805_NOOUTLINE', 'PARTLETTER': 'D', 'VALUE': 'BLUE', 'VALUENUMBER': '', 'PACKAGENUMBER': '0805', 'BOM': '', 'OWNER': 'ADAF', 'FULL': 'D2,BLUE,CHIPLED_0805_NOOUTLINE BLUE,CHIPLED_0805_NOOUTLINE,,,'}},
       'U1': {'OOMPID': 'UNMATCHED-UNMATCHED-X-UNMATCHED-01', 'FULL': {'DESC': '', 'PART': 'U1', 'DEVICE': 'BLE_MODULE_RAYTAC_MDBT40 MBT40', 'PACKAGE': 'BLE_MODULE_RAYTAC_MDBT40', 'PARTLETTER': 'U', 'VALUE': 'MBT40', 'VALUENUMBER': '40', 'PACKAGENUMBER': '40', 'BOM': '', 'OWNER': 'ADAF', 'FULL': 'U1,MBT40,BLE_MODULE_RAYTAC_MDBT40 MBT40,BLE_MODULE_RAYTAC_MDBT40,,,'}},
       'SW1': {'OOMPID': 'BUTA-UNMATCHED-X-STAN-01', 'FULL': {'DESC': '', 'PART': 'SW1', 'DEVICE': 'KMR2 SPST_TACT-KMR2', 'PACKAGE': 'KMR2', 'PARTLETTER': 'SW', 'VALUE': 'SPST_TACT-KMR2', 'VALUENUMBER': '_-2', 'PACKAGENUMBER': '2', 'BOM': '', 'OWNER': 'ADAF', 'FULL': 'SW1,SPST_TACT-KMR2,KMR2 SPST_TACT-KMR2,KMR2,,,'}},
       'U2': {'OOMPID': 'VREG-SO235-X-KMIC5225-V33D', 'FULL': {'DESC': '', 'PART': 'U2', 'DEVICE': 'SOT23-5 MIC5225-3.3', 'PACKAGE': 'SOT23-5', 'PARTLETTER': 'U', 'VALUE': 'MIC5225-3.3', 'VALUENUMBER': '5225-3.3', 'PACKAGENUMBER': '235', 'BOM': '', 'OWNER': 'ADAF', 'FULL': 'U2,MIC5225-3.3,SOT23-5 MIC5225-3.3,SOT23-5,,,'}},
       'X1': {'OOMPID': 'HEAD-JSTPH-X-UNMATCHED-01', 'FULL': {'DESC': '', 'PART': 'X1', 'DEVICE': 'JSTPH2 JSTPH', 'PACKAGE': 'JSTPH2', 'PARTLETTER': 'X', 'VALUE': 'JSTPH', 'VALUENUMBER': '', 'PACKAGENUMBER': '2', 'BOM': '', 'OWNER': 'ADAF', 'FULL': 'X1,JSTPH,JSTPH2 JSTPH,JSTPH2,,,'}}}]
