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
-- Table structure for table `ong`
--

DROP TABLE IF EXISTS `ong`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `ong` (
  `id` int NOT NULL AUTO_INCREMENT,
  `nome_Ong` varchar(100) NOT NULL,
  `email` varchar(150) NOT NULL,
  `senha` varchar(200) NOT NULL,
  `telefone` varchar(20) NOT NULL,
  `rua` varchar(150) NOT NULL,
  `complemento` varchar(150) NOT NULL,
  `cep` varchar(9) NOT NULL,
  `instagram` varchar(50) NOT NULL,
  `cnpj` varchar(14) NOT NULL,
  `numero` varchar(10) NOT NULL,
  `ddd` varchar(2) NOT NULL,
  `celular` varchar(9) NOT NULL,
  `dados_bancarios` varchar(100) NOT NULL,
  `foto_perfil_Logo` varchar(200) DEFAULT NULL,
  `foto_qrCode` varchar(200) DEFAULT NULL,
  `descricao_foto_perfil_Logo` varchar(300) NOT NULL,
  `descricao_foto_qrCode` varchar(300) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `email` (`email`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ong`
--

LOCK TABLES `ong` WRITE;
/*!40000 ALTER TABLE `ong` DISABLE KEYS */;
INSERT INTO `ong` VALUES (1,'Animal de Rua Campina Grande','animalderuacg@gmail.com','scrypt:32768:8:1$ypzyz4udgjytN8GL$b8d6ebc20468abcf90856cfdd4d94b1d3dea4aac78c204c3041c8288d63d57357b67de023dfc0e60728eb358655b7b3f8a4ad67df4b123d41ad3f5257db020be','000000000','Logradouro NAPOLEAO LAUREANO','','58401372','https://www.instagram.com/animalderuacg/','46540371000167','527','00','000000000','animalderuacg@gmail.com','static/uploads\\Animal_de_rua.jpg','static/uploads\\qr_code_ong_animal_de_rua.png','Logo amarela com o nome da ong Animal de Rua ','Essa imagem é o QR code do PIX da ONG Animal de Rua Campina Grande'),(2,'Associação dos Amigos dos Animais Abandonados','a4ong@gmail.com','scrypt:32768:8:1$SjJLYzS7JgByKmmi$0749492610000756a75fd98885c16b7607f6432bac2a19f77c90deedb3f4030138f0e60c95b990142836d73f04cc26060c95d32bbd4f1d666a1dcd9a5735b501','111111111','ACASSIO FIGUEIREDO','','58400002','https://www.instagram.com/a4.ong/','06262522000148','1011','11','111111111','PIX:06.262.522.0001-48','static/uploads/Ass dos amgs dos animais.jpg','static/uploads/qr code a4 associacao.png','Logo da Associação dos Amigos dos Animais Abandonados com um gato e cachorro','Essa imagem é o QR code do PIX da ONG Associação dos Amigos dos Animais Abandonados');
/*!40000 ALTER TABLE `ong` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-11-29  4:26:32
