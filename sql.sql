-- MySQL dump 10.13  Distrib 8.0.42, for Win64 (x86_64)
--
-- Host: localhost    Database: hotel
-- ------------------------------------------------------
-- Server version	8.0.42

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
-- Table structure for table `backend_guests`
--

DROP TABLE IF EXISTS `backend_guests`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `backend_guests` (
  `guestID` int NOT NULL AUTO_INCREMENT,
  `guestName` varchar(255) NOT NULL,
  `guestEmail` varchar(255) NOT NULL,
  `password` varchar(255) NOT NULL,
  `guestNRC` varchar(100) NOT NULL,
  `guestPh` varchar(11) DEFAULT NULL,
  `Address` varchar(255) DEFAULT NULL,
  `created_at` datetime(6) NOT NULL,
  PRIMARY KEY (`guestID`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `backend_guests`
--

LOCK TABLES `backend_guests` WRITE;
/*!40000 ALTER TABLE `backend_guests` DISABLE KEYS */;
INSERT INTO `backend_guests` VALUES (1,'Kaung Khant Lin','kaungkhantlin@gmail.com','00000000','12/yakana(N)088513','09963101015','Yankin Yangon','2025-10-13 20:13:55.000000');
/*!40000 ALTER TABLE `backend_guests` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `backend_menus`
--

DROP TABLE IF EXISTS `backend_menus`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `backend_menus` (
  `menuID` int NOT NULL AUTO_INCREMENT,
  `menuName` varchar(255) NOT NULL,
  `description` longtext NOT NULL,
  `price` int NOT NULL,
  `menuType` varchar(255) DEFAULT NULL,
  `cookingTime` int NOT NULL,
  `created_at` datetime(6) NOT NULL,
  PRIMARY KEY (`menuID`)
) ENGINE=InnoDB AUTO_INCREMENT=37 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `backend_menus`
--

LOCK TABLES `backend_menus` WRITE;
/*!40000 ALTER TABLE `backend_menus` DISABLE KEYS */;
INSERT INTO `backend_menus` VALUES (1,'Grilled Fish Platter','Fresh local fish, seasoned and grilled with herbs',20,'Local Special',25,'2025-10-08 22:49:11.000000'),(2,'Lamb Curry with Rice','Tender lamb slow cooked in spiced curry sauce with basmati rice',22,'Local Special',30,'2025-10-08 22:49:11.000000'),(3,'Coconut Prawn Curry','Juicy prawns simmered in coconut gravy',19,'Local Special',20,'2025-10-08 22:49:11.000000'),(4,'BBQ Mixed Platter','Chicken, lamb, sausage, vegetables - served with sauce',25,'Local Special',25,'2025-10-08 22:49:11.000000'),(5,'Fried Noodles Special','Stir-fried noodles with shrimp, egg, veggies, and soy sauce',12,'Local Special',12,'2025-10-08 22:49:11.000000'),(6,'Local Rice Set','Steamed rice with chicken curry, salad, and soup',10,'Local Special',15,'2025-10-08 22:49:11.000000'),(7,'Mini Burger & Fries','Small beef burger, fries, and juice box',8,'Kids Menu',10,'2025-10-08 22:49:11.000000'),(8,'Chicken Nuggets Meal','6 chicken nuggets, fries, ketchup, small drink',7,'Kids Menu',8,'2025-10-08 22:49:11.000000'),(9,'Kids Spaghetti','Plain spaghetti with tomato sauce & cheese',7,'Kids Menu',10,'2025-10-08 22:49:11.000000'),(10,'Mini Pancake Stack','Fluffy pancakes with honey or chocolate syrup',6,'Kids Menu',8,'2025-10-08 22:49:11.000000'),(11,'Cheese Quesadilla','Grilled tortilla filled with melted cheese',6,'Kids Menu',7,'2025-10-08 22:49:11.000000'),(12,'Fruit Cup','Mixed seasonal fruits, chopped for kids',4,'Kids Menu',5,'2025-10-08 22:49:11.000000'),(13,'Iced Latte','Espresso with chilled milk and ice',5,'Beverage',3,'2025-10-08 22:49:11.000000'),(14,'Hot Chocolate','Creamy chocolate drink topped with whipped cream',4,'Beverage',4,'2025-10-08 22:49:11.000000'),(15,'Smoothie Bowl','Blended fruits topped with granola, coconut, and berries',8,'Beverage',5,'2025-10-08 22:49:11.000000'),(16,'Mocktail Paradise','Colorful fruit mocktail with mint and ice',6,'Beverage',3,'2025-10-08 22:49:11.000000'),(17,'Tiramisu','Classic Italian coffee-flavored layered dessert',7,'Dessert',8,'2025-10-08 22:49:11.000000'),(18,'Cheesecake Slice','Creamy cheesecake with strawberry topping',6,'Dessert',6,'2025-10-08 22:49:11.000000'),(19,'Banana Split','Ice cream with banana, nuts, whipped cream, chocolate syrup',7,'Dessert',5,'2025-10-08 22:49:11.000000'),(20,'Continental Breakfast','Includes toast, butter, jam, eggs, juice, and coffee',10,'Breakfast',10,'2025-10-08 22:50:46.000000'),(21,'Traditional Breakfast','Local breakfast set with eggs, sausage, beans, etc.',12,'Breakfast',12,'2025-10-08 22:50:46.000000'),(22,'Chicken Fried Rice','Stir-fried rice with chicken, eggs, and vegetables',15,'Main Course',15,'2025-10-08 22:50:46.000000'),(23,'Club Sandwich','Triple layered sandwich with fries and salad',12,'Main Course',10,'2025-10-08 22:50:46.000000'),(24,'Caesar Salad','Fresh romaine, chicken, croutons, parmesan, Caesar sauce',11,'Main Course',8,'2025-10-08 22:50:46.000000'),(25,'Grilled Chicken Steak','Marinated chicken breast with mashed potatoes & veggies',18,'Main Course',20,'2025-10-08 22:50:46.000000'),(26,'Spaghetti Bolognese','Classic Italian pasta with meat sauce',14,'Main Course',15,'2025-10-08 22:50:46.000000'),(27,'Margarita Pizza','Classic cheese pizza with tomato and basil',13,'Main Course',18,'2025-10-08 22:50:46.000000'),(28,'Beef Burger','Juicy beef patty with cheese, lettuce, tomato, fries',15,'Main Course',15,'2025-10-08 22:50:46.000000'),(29,'Veggie Wrap','Grilled vegetables in a tortilla wrap',10,'Main Course',10,'2025-10-08 22:50:46.000000'),(30,'Fresh Juice','Seasonal fruit juice, cold-pressed',5,'Beverage',3,'2025-10-08 22:50:46.000000'),(31,'Cappuccino','Freshly brewed espresso with steamed milk',4,'Beverage',5,'2025-10-08 22:50:46.000000'),(32,'Mineral Water','Bottled drinking water',2,'Beverage',1,'2025-10-08 22:50:46.000000'),(33,'Soft Drinks','Coke, Pepsi, Sprite, Fanta',3,'Beverage',1,'2025-10-08 22:50:46.000000'),(34,'Chocolate Cake','Rich chocolate layered cake slice',6,'Dessert',7,'2025-10-08 22:50:46.000000'),(35,'Fruit Salad','Mixed seasonal fruits with honey & mint',7,'Dessert',5,'2025-10-08 22:50:46.000000'),(36,'Ice Cream Sundae','Vanilla ice cream with chocolate sauce and toppings',6,'Dessert',4,'2025-10-08 22:50:46.000000');
/*!40000 ALTER TABLE `backend_menus` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `backend_rooms`
--

DROP TABLE IF EXISTS `backend_rooms`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `backend_rooms` (
  `roomID` int NOT NULL AUTO_INCREMENT,
  `roomCode` varchar(5) NOT NULL,
  `building` varchar(2) NOT NULL,
  `accomodation` int NOT NULL,
  `type` varchar(100) NOT NULL,
  `price` int NOT NULL,
  `status` varchar(100) NOT NULL,
  PRIMARY KEY (`roomID`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `backend_rooms`
--

LOCK TABLES `backend_rooms` WRITE;
/*!40000 ALTER TABLE `backend_rooms` DISABLE KEYS */;
INSERT INTO `backend_rooms` VALUES (1,'001','A',4,'Deluxe',100,'free'),(2,'002','A',2,'Deluxe',100,'free'),(3,'001','B',3,'Standard',80,'free');
/*!40000 ALTER TABLE `backend_rooms` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `backend_staffs`
--

DROP TABLE IF EXISTS `backend_staffs`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `backend_staffs` (
  `staffID` int NOT NULL AUTO_INCREMENT,
  `staffName` varchar(255) NOT NULL,
  `staffEmail` varchar(255) NOT NULL,
  `staffPassword` varchar(255) NOT NULL,
  `role` varchar(255) NOT NULL,
  `payRoll` int NOT NULL,
  `created_at` datetime(6) NOT NULL,
  PRIMARY KEY (`staffID`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `backend_staffs`
--

LOCK TABLES `backend_staffs` WRITE;
/*!40000 ALTER TABLE `backend_staffs` DISABLE KEYS */;
INSERT INTO `backend_staffs` VALUES (1,'Manager','manager@gmail.com','Manager@123','Manager',800000,'2025-10-13 20:06:56.000000');
/*!40000 ALTER TABLE `backend_staffs` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2025-10-17 12:11:43
