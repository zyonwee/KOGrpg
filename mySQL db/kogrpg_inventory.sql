-- MySQL dump 10.13  Distrib 8.0.16, for Win64 (x86_64)
--
-- Host: localhost    Database: kogrpg
-- ------------------------------------------------------
-- Server version	8.0.16

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
 SET NAMES utf8 ;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `inventory`
--

DROP TABLE IF EXISTS `inventory`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `inventory` (
  `category_id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `item` varchar(45) DEFAULT NULL,
  `number` int(11) DEFAULT '1',
  `equip` varchar(45) DEFAULT NULL,
  `type` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`category_id`),
  KEY `name_idx` (`name`),
  CONSTRAINT `name` FOREIGN KEY (`name`) REFERENCES `stats` (`name`) ON DELETE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=327 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `inventory`
--

LOCK TABLES `inventory` WRITE;
/*!40000 ALTER TABLE `inventory` DISABLE KEYS */;
INSERT INTO `inventory` VALUES (243,'tobs#8561','rare lootbox',0,NULL,'lb'),(269,'OneForFourKay#5753','lootbox',2,NULL,'lb'),(280,'tobs#8561','rockie core',3,NULL,'mat'),(281,'OneForFourKay#5753','water lantern',10,NULL,'mat'),(282,'tobs#8561','blood',5,NULL,'mat'),(283,'tobs#8561','egg common',0,NULL,'pet'),(284,'tobs#8561','pancake',0,'FALSE','def'),(285,'tobs#8561','life potion',9,NULL,'hp'),(286,'OneForFourKay#5753','magic bean',7,NULL,'mat'),(287,'tobs#8561','ooze',8,NULL,'mat'),(288,'tobs#8561','pet treats',0,NULL,'petxp'),(289,'tobs#8561','egg uncommon',0,NULL,'pet'),(290,'OneForFourKay#5753','nail',1,'FALSE','att'),(291,'tobs#8561','halo ole champion',2,NULL,'mat'),(292,'tobs#8561','fangs',3,NULL,'mat'),(293,'tobs#8561','rare lootbox',0,NULL,'lb'),(295,'tobs#8561','stick',0,'FALSE','att'),(296,'OneForFourKay#5753','jelly',1,NULL,'mat'),(297,'OneForFourKay#5753','rookie core',1,NULL,'evo'),(298,'tobs#8561','baby core',2,NULL,'evo'),(299,'tobs#8561','life potion',9,NULL,'hp'),(301,'tobs#8561','baby core',2,NULL,'evo'),(302,'tobs#8561','blood',5,NULL,'mat'),(303,'tobs#8561','stick',0,'FALSE','att'),(304,'tobs#8561','fangs',3,NULL,'mat'),(305,'tobs#8561','rare lootbox',0,NULL,'lb'),(306,'tobs#8561','holey shirt',1,'TRUE','def'),(307,'tobs#8561','in-training core',1,NULL,'evo'),(308,'tobs#8561','magic bean',1,NULL,'mat'),(309,'tobs#8561','pancake',0,'FALSE','def'),(310,'tobs#8561','rockie core',3,NULL,'mat'),(311,'OneForFourKay#5753','water lantern',10,NULL,'mat'),(312,'tobs#8561','ooze',8,NULL,'mat'),(313,'tobs#8561','halo ole champion',2,NULL,'mat'),(314,'tobs#8561','nail',1,'FALSE','att'),(315,'OneForFourKay#5753','in-training core',1,NULL,'evo'),(316,'tobs#8561','blood',5,NULL,'mat'),(317,'OneForFourKay#5753','holey shirt',1,'TRUE','def'),(318,'tobs#8561','life potion',9,NULL,'hp'),(320,'tobs#8561','ooze',8,NULL,'mat'),(321,'OneForFourKay#5753','rare staff',1,'TRUE','att'),(322,'tobs#8561','ooze',8,NULL,'mat'),(323,'tobs#8561','egg uncommon',0,NULL,'pet'),(324,'tobs#8561','pet treats',0,NULL,'petxp'),(325,'tobs#8561','rookie core',1,NULL,'evo'),(326,'tobs#8561','egg common',0,NULL,'pet');
/*!40000 ALTER TABLE `inventory` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2020-05-30 19:02:47
