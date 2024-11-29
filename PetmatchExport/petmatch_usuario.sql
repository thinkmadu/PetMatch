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
-- Table structure for table `usuario`
--

DROP TABLE IF EXISTS `usuario`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `usuario` (
  `id` int NOT NULL AUTO_INCREMENT,
  `primeiro_nome` varchar(100) NOT NULL,
  `sobrenome` varchar(100) NOT NULL,
  `email` varchar(150) NOT NULL,
  `senha` varchar(200) NOT NULL,
  `telefone` varchar(20) NOT NULL,
  `rua` varchar(150) NOT NULL,
  `complemento` varchar(150) NOT NULL,
  `cep` varchar(9) NOT NULL,
  `numero` varchar(10) NOT NULL,
  `ddd` varchar(2) NOT NULL,
  `celular` varchar(9) NOT NULL,
  `foto_perfil` varchar(300) NOT NULL,
  `descricao_foto_perfil` varchar(300) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `email` (`email`)
) ENGINE=InnoDB AUTO_INCREMENT=58 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `usuario`
--

LOCK TABLES `usuario` WRITE;
/*!40000 ALTER TABLE `usuario` DISABLE KEYS */;
INSERT INTO `usuario` VALUES (55,'Jessica','Mora','doxino2895@aqqor.com','scrypt:32768:8:1$hfzwCxRwXJbNRi6N$618f2adfd33e4dca57446c126f74f5c79e9690dd7da1cbd2243a9bf041947a3037140644fe012f6ad0280647ecea7e6e05dd47784be976d32af29a0527fdbba1','111111111','rua 2','pp','77777777','7','77','777777777','static/uploads\\jessica_moraes.jpg','mulher platinada com batom vermelho'),(56,'Manuela','Gomes','melobos118@chainds.com','scrypt:32768:8:1$OtNvkERXlasK09iL$7cdaeddd87c25549b59636327b77c1ac454ac29d74d96fb7970d59fe0b479ae91fbe26c388200f894171943a3e3d39d69aff2ad673de2f98b8fb52a16b0541fb','222222222','rua teste 2','aa','22222222','22','22','222222222','static/uploads\\manuela_gomes.jpg','Mulher de cabelos escuros e vestido prata'),(57,'Jorge','Silva','sohew17721@confmin.com','scrypt:32768:8:1$FHAbLusn1chjN7GJ$e07a3abc7a21d9eb09f3945c23011d6f330905f4ebe34aea2884812d2e4a3f43e0fdc55f2a5e1298394ec9f8d80cf98dacdd50815c10324b90460cc547330e1d','444444444','rua 12','qq','11111111','444444','44','444444444','static/uploads\\seujorge.jpg','Seu jorge de terno');
/*!40000 ALTER TABLE `usuario` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-11-29  4:26:44
