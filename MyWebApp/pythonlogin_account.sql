-- MySQL dump 10.13  Distrib 8.0.33, for Win64 (x86_64)
--
-- Host: localhost    Database: pythonlogin
-- ------------------------------------------------------
-- Server version	8.0.33

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `accounts`
--

DROP TABLE IF EXISTS `accounts`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `accounts` (
  `id` int NOT NULL AUTO_INCREMENT,
  `username` varchar(50) NOT NULL,
  `password` varchar(255) NOT NULL,
  `email` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username_UNIQUE` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `accounts`
--

LOCK TABLES `accounts` WRITE;
/*!40000 ALTER TABLE `accounts` DISABLE KEYS */;
INSERT INTO `accounts` VALUES (1,'testing','testing','testing@test.com'),(2,'test2','$2b$12$8Nz76F.7L534V9lUCs0sseHAp8DavAOUJ2rATwja4LxNWAIoTXheq','gAAAAABkWgpaZW76DF-E6b8Kjfrr1ozdbwOoUx1A6dpLOA16XdH539anib2duqKzciSfQYijBKladaaUHO-6F13mopJ9XvHITA=='),(3,'test3','$2b$12$Or.oqmV99Lo/JiZMCHLUcuzhAp4EWMVCcIpa0aL5mdMc.g9vcwZ5K','gAAAAABkWgsDKT97s8MR3Ihl-U4hptLfdjtBPkbCwXCOmENYop3p2-xkA5mon8g4e6fuAI4nlIAj9YXfB75byB_gN20ykxKh6g=='),(5,'test4','$2b$12$awox0yMmozzuDr.gJ6gE.OvKYown91ejnb7R5EzmfVAyAIniV5Pvi','gAAAAABkWgxFxeyMTP7KUeRKkhWMNsB5FPVOTcMXQY8bvyGXGIRa3QBIIlvYebSrRQ0ARpTlgdMTxfYyIQBotd4C6zWRxCcNeA=='),(7,'test5','$2b$12$NdhvYvQWJA6EIih9Z8baP.LLy/AxWHvTku4zMZGTXjONwvnh/QIYy','gAAAAABkWhJ6Hfji-YkX9MpA4SgT0gkFxzPmPiBPAvohRi58TRAJtvoYZ72JDmTEc3AKl_lVSIs5wIRchO-mWSfM5SJu7_D9dw==');
/*!40000 ALTER TABLE `accounts` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-05-10 22:23:41
