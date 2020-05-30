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
-- Table structure for table `mypets`
--

DROP TABLE IF EXISTS `mypets`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `mypets` (
  `Name` text,
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `Stage` text,
  `Type` text,
  `Attribute` text,
  `pets` text,
  `Equip Slots` varchar(44) DEFAULT 'NONE',
  `HP` int(50) DEFAULT '0',
  `XP` int(11) DEFAULT '0',
  `Atk` int(11) DEFAULT '0',
  `Def` int(11) DEFAULT '0',
  `level` int(11) DEFAULT '1',
  `moves` int(11) DEFAULT NULL,
  `Image link` text,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=46 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `mypets`
--

LOCK TABLES `mypets` WRITE;
/*!40000 ALTER TABLE `mypets` DISABLE KEYS */;
INSERT INTO `mypets` VALUES ('suqarcookies#7445',33,'In-Training',NULL,'Fire','Koro','NONE',209,250,0,0,11,NULL,'http://digidb.io/images/dot/dot322.png'),('suqarcookies#7445',34,'In-Training',NULL,'Dark','Tsume','NONE',132,250,0,0,11,NULL,'http://digidb.io/images/dot/dot631.png'),('OneForFourKay#5753',35,'Ultimate',NULL,'Plant','Lilly','NONE',738,12610,0,0,41,NULL,'http://digidb.io/images/dot/dot359.png'),('OneForFourKay#5753',36,'Champion',NULL,'Water','Soceri','NONE',665,10800,0,0,35,NULL,'http://digidb.io/images/dot/dot755.png'),('OneForFourKay#5753',37,'Ultimate',NULL,'Water','Wha','NONE',1066,12470,0,0,41,NULL,'http://digidb.io/images/dot/dot021.png'),('suqarcookies#7445',38,'In-Training',NULL,'Plant','Yoko','Main Pet',154,250,0,0,11,NULL,'http://digidb.io/images/dot/dot510.png'),('suqarcookies#7445',39,'In-Training',NULL,'Water','Buka','Main Pet',170,510,0,0,10,NULL,'http://digidb.io/images/dot/dot514.png'),('OneForFourKay#5753',40,'Ultimate',NULL,'Light','Angewo','Main Pet',1000,6510,0,0,40,NULL,'http://digidb.io/images/dot/dot148.png'),('suqarcookies#7445',41,'In-Training',NULL,'Earth','Tsuno','NONE',19,0,0,0,1,NULL,'http://digidb.io/images/dot/dot438.png'),('OneForFourKay#5753',42,'In-Training',NULL,'Plant','Tane','NONE',462,1970,0,0,22,NULL,'http://digidb.io/images/dot/dot512.png'),('tobs#8561',43,'In-Training',NULL,'Neutral','Toko','NONE',91,240,0,0,7,NULL,'http://digidb.io/images/dot/dot325.png'),('tobs#8561',44,'In-Training',NULL,'Light','Nyaro','NONE',11,0,0,0,1,NULL,'http://digidb.io/images/dot/dot515.png'),('tobs#8561',45,'In-Training',NULL,'Water','Buka','Main Pet',170,510,0,0,10,NULL,'http://digidb.io/images/dot/dot514.png');
/*!40000 ALTER TABLE `mypets` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2020-05-30 19:02:48
