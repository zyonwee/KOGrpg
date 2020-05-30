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
-- Table structure for table `monsters`
--

DROP TABLE IF EXISTS `monsters`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `monsters` (
  `name` varchar(45) NOT NULL,
  `emoji` varchar(45) DEFAULT NULL,
  `level` int(11) DEFAULT NULL,
  `itermdrop` varchar(45) DEFAULT NULL,
  `desc` varchar(45) DEFAULT NULL,
  `chance` decimal(10,0) DEFAULT NULL,
  `coins` int(11) DEFAULT NULL,
  `att` int(11) DEFAULT NULL,
  `hp` int(11) DEFAULT NULL,
  `xp` int(11) DEFAULT NULL,
  `num_drop` int(11) DEFAULT NULL,
  PRIMARY KEY (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `monsters`
--

LOCK TABLES `monsters` WRITE;
/*!40000 ALTER TABLE `monsters` DISABLE KEYS */;
INSERT INTO `monsters` VALUES ('BirbGel','<:birbgel:716082031653552238>',25,'Halo Ole Champion','Bird has a hoop. It gotta oop.',5,500,25,70,3000,2),('Eyeling','<:Eyeling:715242854158565446>',3,'Blood','Period.',6,20,4,70,200,2),('JellyBoi','<:tentaclemonster:716012597606088785>',9,'Jelly','Dont put him on your bread',7,100,13,100,800,2),('Planterra','<:plantera:716082031699689473>',12,'Magic Bean','For vegans only!',4,200,16,60,1000,2),('Rookie Core','<:Miniolem:716082031796420669>',19,'Rockie Core','I thought it was a ball !',5,300,19,80,1500,5),('Slimeling','<:slimeling:715475989387411486>',5,'Ooze','Slimey',4,60,9,80,450,4),('Snakeling','<:Snakeling:715010903828987975>',0,'Fangs','Medusa\'s lice and bugs',5,15,1,60,100,2),('Whalermere','<:whalemere:716082031561277521> ',31,'Water Lantern','Underwater Menance',3,1000,21,130,4500,5);
/*!40000 ALTER TABLE `monsters` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2020-05-30 19:02:49
