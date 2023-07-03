-- MySQL dump 10.13  Distrib 8.0.32, for Linux (x86_64)
--
-- Host: localhost    Database: GeoAlert
-- ------------------------------------------------------
-- Server version	8.0.32-0ubuntu0.22.04.2

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `locationReminder`
--

DROP TABLE IF EXISTS `locationReminder`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `locationReminder` (
  `id` varchar(128) NOT NULL,
  `user_name` varchar(128) DEFAULT NULL,
  `location_id` varchar(128) DEFAULT NULL,
  `todo_id` varchar(128) DEFAULT NULL,
  `accuracy` int DEFAULT NULL,
  `activated` tinyint(1) DEFAULT NULL,
  `created_at` datetime DEFAULT NULL,
  `updated_at` datetime DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `user_name` (`user_name`),
  KEY `location_id` (`location_id`),
  KEY `todo_id` (`todo_id`),
  CONSTRAINT `locationReminder_ibfk_1` FOREIGN KEY (`user_name`) REFERENCES `users` (`username`),
  CONSTRAINT `locationReminder_ibfk_2` FOREIGN KEY (`location_id`) REFERENCES `locations` (`id`) ON UPDATE CASCADE,
  CONSTRAINT `locationReminder_ibfk_3` FOREIGN KEY (`todo_id`) REFERENCES `todos` (`id`) ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `locationReminder`
--

LOCK TABLES `locationReminder` WRITE;
/*!40000 ALTER TABLE `locationReminder` DISABLE KEYS */;
INSERT INTO `locationReminder` VALUES ('0f389b9d-f6e8-49a7-964c-544c8e82862c',NULL,'d9c9045c-2417-44d9-b6c4-8e6dd4dc9850',NULL,0,0,'2023-06-20 20:44:38','2023-06-20 20:44:38');
/*!40000 ALTER TABLE `locationReminder` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `locations`
--

DROP TABLE IF EXISTS `locations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `locations` (
  `id` varchar(128) NOT NULL,
  `user_name` varchar(128) DEFAULT NULL,
  `name` varchar(128) DEFAULT NULL,
  `address` varchar(128) DEFAULT NULL,
  `latitude` varchar(28) NOT NULL,
  `longitude` varchar(28) NOT NULL,
  `created_at` datetime DEFAULT NULL,
  `updated_at` datetime DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `user_name` (`user_name`),
  CONSTRAINT `locations_ibfk_1` FOREIGN KEY (`user_name`) REFERENCES `users` (`username`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `locations`
--

LOCK TABLES `locations` WRITE;
/*!40000 ALTER TABLE `locations` DISABLE KEYS */;
INSERT INTO `locations` VALUES ('d9c9045c-2417-44d9-b6c4-8e6dd4dc9850',NULL,'Sample','\"No','19.32','20.03','2023-06-20 20:40:08','2023-06-20 20:40:08');
/*!40000 ALTER TABLE `locations` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `todos`
--

DROP TABLE IF EXISTS `todos`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `todos` (
  `id` varchar(255) NOT NULL,
  `user_name` varchar(128) DEFAULT NULL,
  `title` varchar(255) DEFAULT NULL,
  `description` varchar(255) DEFAULT NULL,
  `due_date` datetime DEFAULT NULL,
  `completed` tinyint(1) DEFAULT NULL,
  `created_at` datetime DEFAULT NULL,
  `updated_at` datetime DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `user_name` (`user_name`),
  CONSTRAINT `todos_ibfk_1` FOREIGN KEY (`user_name`) REFERENCES `users` (`username`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `todos`
--

LOCK TABLES `todos` WRITE;
/*!40000 ALTER TABLE `todos` DISABLE KEYS */;
INSERT INTO `todos` VALUES ('06ba0caa-f166-4b52-bc41-4e6b2b6d2559','deyer','First Todo','an_example_used','2023-06-19 00:00:00',0,'2023-06-21 21:48:49','2023-06-22 06:20:16'),('761dbcae-4b3f-425e-96fd-fe3aa8f22fca','deyer','Testing fromVSCode updating','This is another example of things i can achieve with python','2023-07-02 19:45:58',1,'2023-07-02 19:45:58','2023-07-02 19:45:58'),('cb980d54-5773-4c9d-b0e4-cbb394469cd2',NULL,'Testing fromVSCode','This is another example of things i can achieve with python','2023-07-02 17:37:11',1,'2023-07-02 17:37:11','2023-07-02 17:37:11');
/*!40000 ALTER TABLE `todos` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `users`
--

DROP TABLE IF EXISTS `users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `users` (
  `username` varchar(128) NOT NULL,
  `firstname` varchar(128) NOT NULL,
  `lastname` varchar(128) DEFAULT NULL,
  `email` varchar(128) NOT NULL,
  `password` varchar(128) NOT NULL,
  `created_at` datetime DEFAULT NULL,
  `updated_at` datetime DEFAULT NULL,
  `id` varchar(255) NOT NULL,
  PRIMARY KEY (`username`,`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users`
--

LOCK TABLES `users` WRITE;
/*!40000 ALTER TABLE `users` DISABLE KEYS */;
INSERT INTO `users` VALUES ('anonymous','Anonymous',NULL,'anoymous@mail','password','2023-06-21 21:28:32','2023-06-21 21:28:32','8203c3d2-c736-477f-b29b-542a88b446b3'),('anonymous','Anonymous',NULL,'anoymous@mail','password','2023-06-21 21:28:24','2023-06-21 21:28:24','a8441f18-9128-43c0-a996-4bc3222b6b3f'),('deyer','Anonymous',NULL,'anoymous@mail','password','2023-06-21 12:34:38','2023-07-02 20:41:50','9b6cd797-a662-4012-a1e6-ff7ac2e40eed');
/*!40000 ALTER TABLE `users` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-07-03 19:07:40
