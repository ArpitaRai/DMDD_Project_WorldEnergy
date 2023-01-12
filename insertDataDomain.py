
import pymysql
pymysql.install_as_MySQLdb()
import MySQLdb
import xlrd

#-------------------------------------------------------------------------------------------------
# MySql DB Connection
# ------------------------------------------------------------------------------------------------


database = MySQLdb.connect (host="localhost" , user="root" , password="9125arpitarai" ,db="DMDDWorldEnergy")
cursor = database.cursor()
#-------------------------------------------------------------------------------------------------
# Domain DB Creation 
# ------------------------------------------------------------------------------------------------

createDB = "CREATE DATABASE IF NOT EXISTS `DMDDWorldEnergy`;"
cursor.execute(createDB) 


#-------------------------------------------------------------------------------------------------
# Domain Table Creation 
# ------------------------------------------------------------------------------------------------

Domain_CountryAndCode = "CREATE TABLE IF NOT EXISTS `Domain_CountryAndCode` (`idCountryAndCode` int NOT NULL, `CountryName` varchar(45) NOT NULL,  `Area` varchar(45) NOT NULL,  PRIMARY KEY (`idCountryAndCode`)) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;"
cursor.execute(Domain_CountryAndCode)

Domain_CO2Emission= "CREATE TABLE IF NOT EXISTS `Domain_CO2Emission` ( `idCO2EmissionDomain` int NOT NULL, `CO2CountryID` int NOT NULL,  `CO2Emission` decimal(20,4) DEFAULT NULL,  PRIMARY KEY (`idCO2EmissionDomain`),  KEY `CountryID_idx` (`CO2CountryID`), CONSTRAINT `CO2CountryID` FOREIGN KEY (`CO2CountryID`) REFERENCES `Domain_CountryAndCode` (`idCountryAndCode`) ON DELETE CASCADE ON UPDATE CASCADE) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;"
cursor.execute(Domain_CO2Emission)

Domain_PrimaryEnergyConsumption= "CREATE TABLE IF NOT EXISTS `Domain_PrimaryEnergyConsumption` (`idPrimaryEnergyConsumption` int NOT NULL,  `PECCountryID` int DEFAULT NULL,  `Consumption` decimal(20,4) DEFAULT NULL,  PRIMARY KEY (`idPrimaryEnergyConsumption`),  KEY `PECCountryID_idx` (`PECCountryID`),  CONSTRAINT `PECCountryID` FOREIGN KEY (`PECCountryID`) REFERENCES `Domain_CountryAndCode` (`idCountryAndCode`) ON DELETE CASCADE ON UPDATE CASCADE) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;"
cursor.execute(Domain_PrimaryEnergyConsumption)

Domain_PrimaryEnergyConsumptionByFuel= "CREATE TABLE IF NOT EXISTS `Domain_PrimaryEnergyConsumptionByFuel` (  `idPrimaryEnergyConsumptionByFuel` int NOT NULL,  `PECBCountryID` int NOT NULL,  `CoalConsumption` decimal(20,4) DEFAULT NULL,  `OilConsumption` decimal(20,4) DEFAULT NULL,  `GasConsumption` decimal(20,4) DEFAULT NULL,  PRIMARY KEY (`idPrimaryEnergyConsumptionByFuel`),  KEY `PECBCountryID_idx` (`PECBCountryID`),  CONSTRAINT `PECBCountryID` FOREIGN KEY (`PECBCountryID`) REFERENCES `Domain_CountryAndCode` (`idCountryAndCode`) ON DELETE CASCADE ON UPDATE CASCADE) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;"
cursor.execute(Domain_PrimaryEnergyConsumptionByFuel)

Domain_PrimaryEnergyConsumptionPerCapita = "CREATE TABLE IF NOT EXISTS `Domain_PrimaryEnergyConsumptionPerCapita` (  `idPrimaryEnergyConsumptionPerCapita` int NOT NULL,  `PEPCCountryID` int NOT NULL,  `Consumption` decimal(20,4) DEFAULT NULL,  PRIMARY KEY (`idPrimaryEnergyConsumptionPerCapita`),  KEY `PEPCCountryID_idx` (`PEPCCountryID`),  CONSTRAINT `PEPCCountryID` FOREIGN KEY (`PEPCCountryID`) REFERENCES `Domain_CountryAndCode` (`idCountryAndCode`) ON DELETE CASCADE ON UPDATE CASCADE) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;"
cursor.execute(Domain_PrimaryEnergyConsumptionPerCapita)

Domain_RenewableEnergyConsumption = "CREATE TABLE IF NOT EXISTS `Domain_RenewableEnergyConsumption` (  `idRenewableEnergyConsumption` int NOT NULL,  `RECCountryID` int NOT NULL,  `EnergyConsumption` decimal(20,4) DEFAULT NULL,  PRIMARY KEY (`idRenewableEnergyConsumption`),  KEY `RECCountryID_idx` (`RECCountryID`),  CONSTRAINT `RECCountryID` FOREIGN KEY (`RECCountryID`) REFERENCES `Domain_CountryAndCode` (`idCountryAndCode`) ON DELETE CASCADE ON UPDATE CASCADE) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;"
cursor.execute(Domain_RenewableEnergyConsumption)

Domain_RenewableEnergyConsumptionByFuelType= "CREATE TABLE IF NOT EXISTS `Domain_RenewableEnergyConsumptionByFuel` ( `idRenewableEnergyConsumptionByFuelType` int NOT NULL,  `RECBFCountryId` int NOT NULL,  `SolarConsumption` decimal(20,4) DEFAULT NULL, `WindConsumption` decimal(20,4) DEFAULT NULL,  `GeoBioMassConsumption` decimal(20,4) DEFAULT NULL, PRIMARY KEY (`idRenewableEnergyConsumptionByFuelType`)) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;"
cursor.execute(Domain_RenewableEnergyConsumptionByFuelType)

Domain_RenewableEnergyGeneration = "CREATE TABLE IF NOT EXISTS `Domain_RenewableEnergyGeneration` (`idRenewableEnergyGeneration` int NOT NULL,  `REGCountryID` int NOT NULL,  `EnergyGeneration` decimal(20,4) DEFAULT NULL,  PRIMARY KEY (`idRenewableEnergyGeneration`), KEY `REGCountryID_idx` (`REGCountryID`),  CONSTRAINT `REGCountryID` FOREIGN KEY (`REGCountryID`) REFERENCES `Domain_CountryAndCode` (`idCountryAndCode`) ON DELETE CASCADE ON UPDATE CASCADE) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;"
cursor.execute(Domain_RenewableEnergyGeneration)

#-------------------------------------------------------------------------------------------------
# Domain Table Data Insertion AND Updation
# ------------------------------------------------------------------------------------------------


excel_sheet= xlrd.open_workbook('DMDDDataSet.xls')
countrySheet = excel_sheet.sheet_by_name("Countries")

deleteQuery= "DELETE FROM `DMDDWorldEnergy`.`Domain_CountryAndCode`WHERE idCountryAndCode BETWEEN 1 AND 99;"
cursor.execute(deleteQuery)

insertQueryCountries= " INSERT INTO `DMDDWorldEnergy`.`Domain_CountryAndCode`(`idCountryAndCode`,`CountryName`,`Area`) VALUES(%s,%s,%s)"
for r in range(0,countrySheet.nrows):
    
        countryID = countrySheet.cell(r,0).value
        countryName = countrySheet.cell(r,1).value
        countryArea = countrySheet.cell(r,2).value
        countryDetailsvalue = (countryID, countryName,countryArea)

        cursor.execute(insertQueryCountries,countryDetailsvalue)
    
#------------------------------------------------------------------------------------------------
deleteQuery= "DELETE FROM `DMDDWorldEnergy`.`Domain_CO2Emission`WHERE idCO2EmissionDomain BETWEEN 1 AND 9;"
cursor.execute(deleteQuery)

co2sheet = excel_sheet.sheet_by_name("CO2Emissions")
insertQueryCO2Emissions= " INSERT INTO `DMDDWorldEnergy`.`Domain_CO2Emission`(`idCO2EmissionDomain`,`CO2CountryID`,`CO2Emission`) VALUES(%s,%s,%s)"
for r in range(0, co2sheet.nrows):

        id   =  co2sheet.cell(r,0).value
        countryid = co2sheet.cell(r,1).value
        co2emission = co2sheet.cell(r,2).value
        co2emissionsvalue = (id,countryid,co2emission)

        cursor.execute(insertQueryCO2Emissions,co2emissionsvalue)
        nullRefactor =  "UPDATE `DMDDWorldEnergy`.`Domain_CO2Emission` SET  CO2Emission = NULL WHERE CO2Emission = '0';"
        cursor.execute(nullRefactor)
     
#------------------------------------------------------------------------------------------------
deleteQuery= "DELETE FROM `DMDDWorldEnergy`.`Domain_PrimaryEnergyConsumption`WHERE idPrimaryEnergyConsumption BETWEEN 1 AND 99;"
cursor.execute(deleteQuery)

primaryEnergyConsumption = excel_sheet.sheet_by_name("PrimaryEnergyConsumption")
insertPrimaryEnerggyConsumption= " INSERT INTO `DMDDWorldEnergy`.`Domain_PrimaryEnergyConsumption`(`idPrimaryEnergyConsumption`,`PECCountryID`,`Consumption`) VALUES(%s,%s,%s)"
for r in range(0, primaryEnergyConsumption.nrows):

        id   =  primaryEnergyConsumption.cell(r,0).value
        countryid = primaryEnergyConsumption.cell(r,1).value
        primaryEnergy = primaryEnergyConsumption.cell(r,2).value
        primaryEnergyvalue = (id,countryid,primaryEnergy)

        cursor.execute(insertPrimaryEnerggyConsumption,primaryEnergyvalue)
        nullRefactor =  "UPDATE `DMDDWorldEnergy`.`Domain_PrimaryEnergyConsumption` SET  Consumption = NULL WHERE Consumption = '0';"
        cursor.execute(nullRefactor)

#------------------------------------------------------------------------------------------------
deleteQuery= "DELETE FROM `DMDDWorldEnergy`.`Domain_PrimaryEnergyConsumptionPerCapita`WHERE idPrimaryEnergyConsumptionPerCapita BETWEEN 1 AND 99;"
cursor.execute(deleteQuery)

primaryEnergyConsumptionCapita = excel_sheet.sheet_by_name("PrimaryEnergyConsumptionCapita")
insertPrimaryEnerggyConsumptionCapita= " INSERT INTO `DMDDWorldEnergy`.`Domain_PrimaryEnergyConsumptionPerCapita`(`idPrimaryEnergyConsumptionPerCapita`,`PEPCCountryID`,`Consumption`) VALUES(%s,%s,%s)"
for r in range(0, primaryEnergyConsumptionCapita.nrows):

        id   =  primaryEnergyConsumptionCapita.cell(r,0).value
        countryid = primaryEnergyConsumptionCapita.cell(r,1).value
        primaryEnergy = primaryEnergyConsumptionCapita.cell(r,2).value
        primaryEnergyvalueCapita = (id,countryid,primaryEnergy)

        cursor.execute(insertPrimaryEnerggyConsumptionCapita,primaryEnergyvalueCapita)
        nullRefactor =  "UPDATE `DMDDWorldEnergy`.`Domain_PrimaryEnergyConsumptionPerCapita` SET  Consumption = NULL WHERE Consumption = '0';"
        cursor.execute(nullRefactor)
#------------------------------------------------------------------------------------------------
deleteQuery= "DELETE FROM `DMDDWorldEnergy`.`Domain_RenewableEnergyConsumption`WHERE idRenewableEnergyConsumption BETWEEN 1 AND 99;"
cursor.execute(deleteQuery)

renewableEnergyConsumption = excel_sheet.sheet_by_name("PrimaryEnergyConsumptionCapita")
insertRenewableEnergyConsumption= " INSERT INTO `DMDDWorldEnergy`.`Domain_RenewableEnergyConsumption`(`idRenewableEnergyConsumption`,`RECCountryID`,`EnergyConsumption`) VALUES(%s,%s,%s)"
for r in range(0, renewableEnergyConsumption.nrows):

        id   =  renewableEnergyConsumption.cell(r,0).value
        countryid = renewableEnergyConsumption.cell(r,1).value
        renewableEnergy = renewableEnergyConsumption.cell(r,2).value
        renewableEnergyvalue = (id,countryid,renewableEnergy)

        cursor.execute(insertRenewableEnergyConsumption,renewableEnergyvalue)
        nullRefactor =  "UPDATE `DMDDWorldEnergy`.`Domain_RenewableEnergyConsumption` SET  EnergyConsumption = NULL WHERE EnergyConsumption = '0';"
        cursor.execute(nullRefactor)

#------------------------------------------------------------------------------------------------

deleteQuery= "DELETE FROM `DMDDWorldEnergy`.`Domain_RenewableEnergyGeneration`WHERE idRenewableEnergyGeneration BETWEEN 1 AND 99;"
cursor.execute(deleteQuery)

renewableEnergyGeneration = excel_sheet.sheet_by_name("RenewableEnergyGeneration")
insertRenewableGeneration= " INSERT INTO `DMDDWorldEnergy`.`Domain_RenewableEnergyGeneration`(`idRenewableEnergyGeneration`,`REGCountryID`,`EnergyGeneration`) VALUES(%s,%s,%s)"
for r in range(0, renewableEnergyGeneration.nrows):

        id   =  renewableEnergyGeneration.cell(r,0).value
        countryid = renewableEnergyGeneration.cell(r,1).value
        renewableEnergyGen = renewableEnergyGeneration.cell(r,2).value
        renewableEnergyGenvalue = (id,countryid,renewableEnergyGen)

        cursor.execute(insertRenewableGeneration,renewableEnergyGenvalue)
        nullRefactor =  "UPDATE `DMDDWorldEnergy`.`Domain_RenewableEnergyGeneration` SET  EnergyGeneration = NULL WHERE EnergyGeneration = '0';"
        cursor.execute(nullRefactor)
#------------------------------------------------------------------------------------------------
deleteQuery= "DELETE FROM `DMDDWorldEnergy`.`Domain_PrimaryEnergyConsumptionByFuel`WHERE idPrimaryEnergyConsumptionByFuel BETWEEN 1 AND 99;"
cursor.execute(deleteQuery)

primaryEnergy = excel_sheet.sheet_by_name("EnergyConsumptionByFuel")
insertprimaryEnergy= " INSERT INTO `DMDDWorldEnergy`.`Domain_PrimaryEnergyConsumptionByFuel`(`idPrimaryEnergyConsumptionByFuel`,`PECBCountryID`,`CoalConsumption`,`OilConsumption`,`GasConsumption`) VALUES(%s,%s,%s,%s,%s)"
for r in range(0, primaryEnergy.nrows):

        id   =  primaryEnergy.cell(r,0).value
        countryid = primaryEnergy.cell(r,1).value
        coal = primaryEnergy.cell(r,2).value
        oil = primaryEnergy.cell(r,3).value
        gas = primaryEnergy.cell(r,4).value
        primaryEnergyValueSource = (id,countryid,coal, oil, gas)

        cursor.execute(insertprimaryEnergy,primaryEnergyValueSource)
        nullRefactor =  "UPDATE `DMDDWorldEnergy`.`Domain_PrimaryEnergyConsumptionByFuel` SET  CoalConsumption = NULL WHERE CoalConsumption = '0';"
        cursor.execute(nullRefactor)
        nullRefactor1 =  "UPDATE `DMDDWorldEnergy`.`Domain_PrimaryEnergyConsumptionByFuel` SET  OilConsumption = NULL WHERE OilConsumption = '0';"
        cursor.execute(nullRefactor1)
        nullRefactor2 =  "UPDATE `DMDDWorldEnergy`.`Domain_PrimaryEnergyConsumptionByFuel` SET  GasConsumption = NULL WHERE GasConsumption = '0';"
        cursor.execute(nullRefactor2)

#------------------------------------------------------------------------------------------------
deleteQuery= "DELETE FROM `DMDDWorldEnergy`.`Domain_RenewableEnergyConsumptionByFuel`WHERE idRenewableEnergyConsumptionByFuelType BETWEEN 1 AND 99;"
cursor.execute(deleteQuery)

renewableEnergy = excel_sheet.sheet_by_name("EnergyConsumptionRenewable")
insertRenewableEnergy= " INSERT INTO `DMDDWorldEnergy`.`Domain_RenewableEnergyConsumptionByFuel`(`idRenewableEnergyConsumptionByFuelType`,`RECBFCountryId`,`SolarConsumption`,`WindConsumption`,`GeoBioMassConsumption`) VALUES(%s,%s,%s,%s,%s)"
for r in range(0, renewableEnergy.nrows):

        id   =  renewableEnergy.cell(r,0).value
        countryid = renewableEnergy.cell(r,1).value
        solar = renewableEnergy.cell(r,2).value
        wind = renewableEnergy.cell(r,3).value
        geo = renewableEnergy.cell(r,4).value
        renewableEnergyValueSource = (id,countryid,solar, wind, geo)

        cursor.execute(insertRenewableEnergy,renewableEnergyValueSource)
        nullRefactor =  "UPDATE `DMDDWorldEnergy`.`Domain_RenewableEnergyConsumptionByFuel` SET  SolarConsumption = NULL WHERE solarConsumption = '0' ;"
        cursor.execute(nullRefactor)
        nullRefactor1 =  "UPDATE `DMDDWorldEnergy`.`Domain_RenewableEnergyConsumptionByFuel` SET  WindConsumption = NULL WHERE WindConsumption = '0' ;"
        cursor.execute(nullRefactor1)
        nullRefactor2 =  "UPDATE `DMDDWorldEnergy`.`Domain_RenewableEnergyConsumptionByFuel` SET  GeoBioMassConsumption = NULL WHERE GeoBioMassConsumption = '0' ;"
        cursor.execute(nullRefactor2)

database.commit()
 

