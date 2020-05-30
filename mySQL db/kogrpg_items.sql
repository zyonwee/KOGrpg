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
-- Table structure for table `items`
--

DROP TABLE IF EXISTS `items`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `items` (
  `id` int(11) NOT NULL,
  `name` varchar(45) NOT NULL,
  `emoji` varchar(45) DEFAULT NULL,
  `type` varchar(45) DEFAULT NULL,
  `desc` varchar(95) DEFAULT NULL,
  `price` int(11) DEFAULT NULL,
  `shop` varchar(45) DEFAULT NULL,
  `boosts` int(11) DEFAULT NULL,
  PRIMARY KEY (`name`,`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `items`
--

LOCK TABLES `items` WRITE;
/*!40000 ALTER TABLE `items` DISABLE KEYS */;
INSERT INTO `items` VALUES (12,'Baby Core','<:BabyCore:715931243270897736>','evo','Used to evolve a Baby pet',500,'pet',NULL),(8,'Blood','<:littleBlood:715476281227214892>','mat','Its either my blood, or yours. *From lv 3 Monster*',400,'misc',NULL),(20,'Champion Core','<:ChampionCore:716082031414739015>','evo','Used to evolve a Champion pet',32000,'pet',NULL),(2,'Egg Common','<:EggCommon:714959842846179428>','pet','Common Egg? Maybe a Chicken. Maybe A Dog.',1500,'egg',NULL),(3,'Egg Uncommon','<:EggUncommon:714970054877511711>','pet','Uncommon Egg. You dont eat them everyday',10000,'egg',NULL),(9,'Fangs','<:littlefangs:715474159538405406>','mat','Omg. Someone\'s not brushing Teeth! *From lv 0 Monster*',200,'misc',NULL),(17,'Halo Ole Champion','<:championhalo:716082031339110431>','mat','When a champion wins, he lo-hey ! *From level 25 Monster*',10000,'misc',NULL),(7,'Holey Shirt','<:holeyshirt:715580306324848761>','def','Obscene. Do not wear. + 2 Def',2000,'basic',2),(13,'In-Training Core','<:InTrainingCore:716003698618269798>','evo','Used to evolve a In-Training pet',2000,'pet',NULL),(14,'Jelly','<:jellydrop:716013929750331434>','mat','Oh my! Yumz.. *From lv 9 Monster*',2000,'misc',NULL),(1,'Life Potion','<:lifepotion:715245405918593207>','hp','Consume by `kog heal`',25,'basic',NULL),(21,'Lootbox','<:lootbox:716102332764389406>','lb','Loot Box for a Noob',10000,'lb',NULL),(15,'Magic Bean','<:magicbean:716082031615934504>','mat','Jack threw it away. *From lv 12 Monster*',3000,'misc',NULL),(6,'Nail','<:nail:715580306031247381>','att','Nail ( Not the ones Jesus use ). + 5 Att',1500,'basic',5),(10,'Ooze','<:littleOoze:715475989353857064>','mat','Is this... Mucus ? *From lv 5 Monster*',1000,'misc',NULL),(5,'Pancake','<:pancake:715580305796497519>','def','Days old Pancake. + 1 Def',1000,'basic',1),(11,'Pet Treats','<:pettrest:715823538694783067>','petxp','Main Pet XP + 1000',2000,'pet',1000),(22,'Rare Lootbox','<:rarelootbox:716102332772778104>','lb','Loot Box for Not a noob. Unique items : <:rarestaff:716219592325857340>',50000,'lb',NULL),(23,'Rare Staff','<:rarestaff:716219592325857340>','att','This is the staff of legends! Only obtainable through Rare lootbox and above!!',20000,'misc',8),(16,'Rockie Core','<:rockiecore:716082031658008687>','mat','The Life of a Stone *From level 19  Monster*',5000,'misc',NULL),(19,'Rookie Core','<:RookieCore:716082031624454165>','evo','Used to evolve a Rookie pet',8000,'pet',NULL),(4,'Stick','<:stick:715580305922195478>','att','Stick of the floor. + 3 Att',600,'basic',3),(18,'Water Lantern','<:waterlantern:716082031330721815>','mat','Lantern that works underwater? *From level 31 Monster*',15000,'misc',NULL);
/*!40000 ALTER TABLE `items` ENABLE KEYS */;
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
