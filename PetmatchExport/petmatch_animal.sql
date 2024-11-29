-- MySQL dump 10.13  Distrib 8.0.38, for Win64 (x86_64)
--
-- Host: localhost    Database: petmatch
-- ------------------------------------------------------
-- Server version	8.0.39

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
-- Table structure for table `animal`
--

DROP TABLE IF EXISTS `animal`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `animal` (
  `id` int NOT NULL AUTO_INCREMENT,
  `nome` varchar(100) NOT NULL,
  `especie` varchar(50) NOT NULL,
  `tamanho` varchar(20) NOT NULL,
  `idade` int NOT NULL,
  `descricao` varchar(300) NOT NULL,
  `status` varchar(50) NOT NULL,
  `foto1` varchar(200) NOT NULL,
  `foto2` varchar(200) DEFAULT NULL,
  `foto3` varchar(200) DEFAULT NULL,
  `foto4` varchar(200) DEFAULT NULL,
  `descricao_foto1` varchar(300) NOT NULL,
  `descricao_foto2` varchar(300) DEFAULT NULL,
  `descricao_foto3` varchar(300) DEFAULT NULL,
  `descricao_foto4` varchar(300) DEFAULT NULL,
  `ong_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `ong_id` (`ong_id`),
  CONSTRAINT `animal_ibfk_1` FOREIGN KEY (`ong_id`) REFERENCES `ong` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `animal`
--

LOCK TABLES `animal` WRITE;
/*!40000 ALTER TABLE `animal` DISABLE KEYS */;
INSERT INTO `animal` VALUES (1,'Estelita ','gato','pequeno',2,'Animada e castrada','disponível','static/uploads\\estelita.jpg','static/uploads\\estelita_2.jpeg',NULL,NULL,'gatinho de gorro','gato branco pequeno com pata levantada','','',2),(2,'josefa','gato','medio',12,'gata idosa e ranzinza e com artrite','adotado','static/uploads\\josefa.jpeg',NULL,NULL,NULL,'gata cinza com olhar de tédio','','','',2),(3,'Tangerina','outro','pequeno',5,'Carente e se da bem com crianças','disponível','static/uploads\\tangerina.jpg',NULL,NULL,NULL,'periquito azul','','','',1),(4,'Pimba','cachorro','medio',3,'Brincalhão, castrado, vacinado e não se da bem com gatos','reservado','static/uploads\\pimba.jpg',NULL,NULL,NULL,'vira-lata marrom claro em uma cama','','','',1),(5,'robervaldo','gato','grande',5,'preguiçoso, gordo e surdo','disponível','static/uploads\\robervaldo.jpg','static/uploads\\robervaldo2.jpg','static/uploads\\robervaldo3.jpg',NULL,'gato frajola deitado','gato frajola  olhando pra frente','gato frajola numa calçada','',2),(6,'princesa','cachorro','grande',2,'Pitbull cinza dócil, castrada, com muita energia','reservado','static/uploads\\princesa.jpg','static/uploads\\princesa2.jpg','static/uploads\\princesa3.jpg',NULL,'Pitbull cinza  num gramado','Pitbull cinza sentada','Pitbull cinza sentada','',2),(7,'zico','cachorro','pequeno',6,'pinscher preto, não gosta de crianças, é raivoso ','disponível','static/uploads\\zico.jpg','static/uploads\\zico2.jpg',NULL,NULL,'pinscher preto em pé','rosto de um pinscher preto','','',1);
/*!40000 ALTER TABLE `animal` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-11-29  4:26:30
