/*
SQLyog Community v13.1.5  (64 bit)
MySQL - 5.6.12-log : Database - e_pharma
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;
CREATE DATABASE /*!32312 IF NOT EXISTS*/`e_pharma` /*!40100 DEFAULT CHARACTER SET latin1 */;

USE `e_pharma`;

/*Table structure for table `auth_group` */

DROP TABLE IF EXISTS `auth_group`;

CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(150) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `auth_group` */

/*Table structure for table `auth_group_permissions` */

DROP TABLE IF EXISTS `auth_group_permissions`;

CREATE TABLE `auth_group_permissions` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `auth_group_permissions` */

/*Table structure for table `auth_permission` */

DROP TABLE IF EXISTS `auth_permission`;

CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=73 DEFAULT CHARSET=latin1;

/*Data for the table `auth_permission` */

insert  into `auth_permission`(`id`,`name`,`content_type_id`,`codename`) values 
(1,'Can add log entry',1,'add_logentry'),
(2,'Can change log entry',1,'change_logentry'),
(3,'Can delete log entry',1,'delete_logentry'),
(4,'Can view log entry',1,'view_logentry'),
(5,'Can add permission',2,'add_permission'),
(6,'Can change permission',2,'change_permission'),
(7,'Can delete permission',2,'delete_permission'),
(8,'Can view permission',2,'view_permission'),
(9,'Can add group',3,'add_group'),
(10,'Can change group',3,'change_group'),
(11,'Can delete group',3,'delete_group'),
(12,'Can view group',3,'view_group'),
(13,'Can add user',4,'add_user'),
(14,'Can change user',4,'change_user'),
(15,'Can delete user',4,'delete_user'),
(16,'Can view user',4,'view_user'),
(17,'Can add content type',5,'add_contenttype'),
(18,'Can change content type',5,'change_contenttype'),
(19,'Can delete content type',5,'delete_contenttype'),
(20,'Can view content type',5,'view_contenttype'),
(21,'Can add session',6,'add_session'),
(22,'Can change session',6,'change_session'),
(23,'Can delete session',6,'delete_session'),
(24,'Can view session',6,'view_session'),
(25,'Can add customer',7,'add_customer'),
(26,'Can change customer',7,'change_customer'),
(27,'Can delete customer',7,'delete_customer'),
(28,'Can view customer',7,'view_customer'),
(29,'Can add login',8,'add_login'),
(30,'Can change login',8,'change_login'),
(31,'Can delete login',8,'delete_login'),
(32,'Can view login',8,'view_login'),
(33,'Can add order',9,'add_order'),
(34,'Can change order',9,'change_order'),
(35,'Can delete order',9,'delete_order'),
(36,'Can view order',9,'view_order'),
(37,'Can add stocks',10,'add_stocks'),
(38,'Can change stocks',10,'change_stocks'),
(39,'Can delete stocks',10,'delete_stocks'),
(40,'Can view stocks',10,'view_stocks'),
(41,'Can add prescription',11,'add_prescription'),
(42,'Can change prescription',11,'change_prescription'),
(43,'Can delete prescription',11,'delete_prescription'),
(44,'Can view prescription',11,'view_prescription'),
(45,'Can add payment',12,'add_payment'),
(46,'Can change payment',12,'change_payment'),
(47,'Can delete payment',12,'delete_payment'),
(48,'Can view payment',12,'view_payment'),
(49,'Can add order sub',13,'add_ordersub'),
(50,'Can change order sub',13,'change_ordersub'),
(51,'Can delete order sub',13,'delete_ordersub'),
(52,'Can view order sub',13,'view_ordersub'),
(53,'Can add inventory',14,'add_inventory'),
(54,'Can change inventory',14,'change_inventory'),
(55,'Can delete inventory',14,'delete_inventory'),
(56,'Can view inventory',14,'view_inventory'),
(57,'Can add feedback',15,'add_feedback'),
(58,'Can change feedback',15,'change_feedback'),
(59,'Can delete feedback',15,'delete_feedback'),
(60,'Can view feedback',15,'view_feedback'),
(61,'Can add complaint',16,'add_complaint'),
(62,'Can change complaint',16,'change_complaint'),
(63,'Can delete complaint',16,'delete_complaint'),
(64,'Can view complaint',16,'view_complaint'),
(65,'Can add available_ products',17,'add_available_products'),
(66,'Can change available_ products',17,'change_available_products'),
(67,'Can delete available_ products',17,'delete_available_products'),
(68,'Can view available_ products',17,'view_available_products'),
(69,'Can add bank',18,'add_bank'),
(70,'Can change bank',18,'change_bank'),
(71,'Can delete bank',18,'delete_bank'),
(72,'Can view bank',18,'view_bank');

/*Table structure for table `auth_user` */

DROP TABLE IF EXISTS `auth_user`;

CREATE TABLE `auth_user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(150) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `auth_user` */

/*Table structure for table `auth_user_groups` */

DROP TABLE IF EXISTS `auth_user_groups`;

CREATE TABLE `auth_user_groups` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`),
  CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `auth_user_groups` */

/*Table structure for table `auth_user_user_permissions` */

DROP TABLE IF EXISTS `auth_user_user_permissions`;

CREATE TABLE `auth_user_user_permissions` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`),
  CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `auth_user_user_permissions` */

/*Table structure for table `django_admin_log` */

DROP TABLE IF EXISTS `django_admin_log`;

CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`),
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `django_admin_log` */

/*Table structure for table `django_content_type` */

DROP TABLE IF EXISTS `django_content_type`;

CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=19 DEFAULT CHARSET=latin1;

/*Data for the table `django_content_type` */

insert  into `django_content_type`(`id`,`app_label`,`model`) values 
(1,'admin','logentry'),
(3,'auth','group'),
(2,'auth','permission'),
(4,'auth','user'),
(5,'contenttypes','contenttype'),
(17,'E_PHARMA','available_products'),
(18,'E_PHARMA','bank'),
(16,'E_PHARMA','complaint'),
(7,'E_PHARMA','customer'),
(15,'E_PHARMA','feedback'),
(14,'E_PHARMA','inventory'),
(8,'E_PHARMA','login'),
(9,'E_PHARMA','order'),
(13,'E_PHARMA','ordersub'),
(12,'E_PHARMA','payment'),
(11,'E_PHARMA','prescription'),
(10,'E_PHARMA','stocks'),
(6,'sessions','session');

/*Table structure for table `django_migrations` */

DROP TABLE IF EXISTS `django_migrations`;

CREATE TABLE `django_migrations` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=22 DEFAULT CHARSET=latin1;

/*Data for the table `django_migrations` */

insert  into `django_migrations`(`id`,`app`,`name`,`applied`) values 
(1,'E_PHARMA','0001_initial','2023-10-10 05:43:23.862389'),
(2,'contenttypes','0001_initial','2023-10-10 05:43:23.879238'),
(3,'auth','0001_initial','2023-10-10 05:43:24.145595'),
(4,'admin','0001_initial','2023-10-10 05:43:24.211975'),
(5,'admin','0002_logentry_remove_auto_add','2023-10-10 05:43:24.211975'),
(6,'admin','0003_logentry_add_action_flag_choices','2023-10-10 05:43:24.224987'),
(7,'contenttypes','0002_remove_content_type_name','2023-10-10 05:43:24.288453'),
(8,'auth','0002_alter_permission_name_max_length','2023-10-10 05:43:24.319525'),
(9,'auth','0003_alter_user_email_max_length','2023-10-10 05:43:24.360748'),
(10,'auth','0004_alter_user_username_opts','2023-10-10 05:43:24.366761'),
(11,'auth','0005_alter_user_last_login_null','2023-10-10 05:43:24.398020'),
(12,'auth','0006_require_contenttypes_0002','2023-10-10 05:43:24.398020'),
(13,'auth','0007_alter_validators_add_error_messages','2023-10-10 05:43:24.398020'),
(14,'auth','0008_alter_user_username_max_length','2023-10-10 05:43:24.445115'),
(15,'auth','0009_alter_user_last_name_max_length','2023-10-10 05:43:24.470219'),
(16,'auth','0010_alter_group_name_max_length','2023-10-10 05:43:24.507929'),
(17,'auth','0011_update_proxy_permissions','2023-10-10 05:43:24.507929'),
(18,'auth','0012_alter_user_first_name_max_length','2023-10-10 05:43:24.554975'),
(19,'sessions','0001_initial','2023-10-10 05:43:24.586868'),
(20,'E_PHARMA','0002_bank','2023-10-25 03:49:28.432034'),
(21,'E_PHARMA','0003_stocks_product_type','2023-11-24 07:53:17.457811');

/*Table structure for table `django_session` */

DROP TABLE IF EXISTS `django_session`;

CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `django_session` */

insert  into `django_session`(`session_key`,`session_data`,`expire_date`) values 
('7eevcn0mb069d6h9besssvh93rf27usx','eyJsaWQiOiIiLCJjbmYiOlsiMzUiXX0:1r6Uu1:PFnxfQgjo_U1i2Oi8u3QEJlzjgaHnIGWZo5MPP-vR0M','2023-12-08 12:03:21.801020');

/*Table structure for table `e_pharma_available_products` */

DROP TABLE IF EXISTS `e_pharma_available_products`;

CREATE TABLE `e_pharma_available_products` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `Status` varchar(50) NOT NULL,
  `Quantity` varchar(100) NOT NULL,
  `PRESCRIPTION_id` bigint(20) NOT NULL,
  `PRODUCT_id` bigint(20) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `E_PHARMA_available_p_PRESCRIPTION_id_16eeeca8_fk_E_PHARMA_` (`PRESCRIPTION_id`),
  KEY `E_PHARMA_available_p_PRODUCT_id_41ef3542_fk_E_PHARMA_` (`PRODUCT_id`),
  CONSTRAINT `E_PHARMA_available_p_PRESCRIPTION_id_16eeeca8_fk_E_PHARMA_` FOREIGN KEY (`PRESCRIPTION_id`) REFERENCES `e_pharma_prescription` (`id`),
  CONSTRAINT `E_PHARMA_available_p_PRODUCT_id_41ef3542_fk_E_PHARMA_` FOREIGN KEY (`PRODUCT_id`) REFERENCES `e_pharma_stocks` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=40 DEFAULT CHARSET=latin1;

/*Data for the table `e_pharma_available_products` */

insert  into `e_pharma_available_products`(`id`,`Status`,`Quantity`,`PRESCRIPTION_id`,`PRODUCT_id`) values 
(29,'Available','10',11,1),
(30,'Available','12',11,3),
(31,'Available','2',11,5),
(32,'Available','10',12,1),
(33,'Available','12',13,1),
(34,'Available','10',14,5),
(35,'Available','10',14,3),
(36,'Available','10',14,1),
(37,'Available','10',14,4),
(38,'Available','7',14,5),
(39,'Available','2',11,1);

/*Table structure for table `e_pharma_bank` */

DROP TABLE IF EXISTS `e_pharma_bank`;

CREATE TABLE `e_pharma_bank` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `Account_Holder` varchar(100) NOT NULL,
  `Account_Number` varchar(100) NOT NULL,
  `Card_Number` varchar(100) NOT NULL,
  `CVV` varchar(100) NOT NULL,
  `Expiry_Date` date NOT NULL,
  `Balance_Amount` varchar(100) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;

/*Data for the table `e_pharma_bank` */

insert  into `e_pharma_bank`(`id`,`Account_Holder`,`Account_Number`,`Card_Number`,`CVV`,`Expiry_Date`,`Balance_Amount`) values 
(1,'Archana T','323789738234578932','89748732','3451','2027-06-10','5390'),
(2,'','','','','0000-00-00','');

/*Table structure for table `e_pharma_complaint` */

DROP TABLE IF EXISTS `e_pharma_complaint`;

CREATE TABLE `e_pharma_complaint` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `Date` date NOT NULL,
  `Complaint` varchar(200) NOT NULL,
  `Status` varchar(100) NOT NULL,
  `Reply` varchar(200) NOT NULL,
  `CUSTOMER_id` bigint(20) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `E_PHARMA_complaint_CUSTOMER_id_d43993df_fk_E_PHARMA_customer_id` (`CUSTOMER_id`),
  CONSTRAINT `E_PHARMA_complaint_CUSTOMER_id_d43993df_fk_E_PHARMA_customer_id` FOREIGN KEY (`CUSTOMER_id`) REFERENCES `e_pharma_customer` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=latin1;

/*Data for the table `e_pharma_complaint` */

insert  into `e_pharma_complaint`(`id`,`Date`,`Complaint`,`Status`,`Reply`,`CUSTOMER_id`) values 
(2,'2023-10-15','nooo','replyed','okay',2),
(6,'2023-10-17','tehtfh','replyed','yess',1),
(7,'2023-10-25','not satisfied with the service','replyed','okay i will check',1),
(8,'2023-11-21','service is bad','replyed','sorry',7),
(9,'2023-11-21','too late for delivery ','replyed','okay',1),
(10,'2023-11-24','tuhiji','Pending','Pending',1);

/*Table structure for table `e_pharma_customer` */

DROP TABLE IF EXISTS `e_pharma_customer`;

CREATE TABLE `e_pharma_customer` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `Name` varchar(50) NOT NULL,
  `Phone` varchar(10) NOT NULL,
  `Email` varchar(50) NOT NULL,
  `House_Name` varchar(100) NOT NULL,
  `Place` varchar(100) NOT NULL,
  `Post` varchar(100) NOT NULL,
  `District` varchar(100) NOT NULL,
  `Pin` varchar(10) NOT NULL,
  `Status` varchar(100) NOT NULL,
  `LOGIN_id` bigint(20) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `E_PHARMA_customer_LOGIN_id_9f0ca37d_fk_E_PHARMA_login_id` (`LOGIN_id`),
  CONSTRAINT `E_PHARMA_customer_LOGIN_id_9f0ca37d_fk_E_PHARMA_login_id` FOREIGN KEY (`LOGIN_id`) REFERENCES `e_pharma_login` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=latin1;

/*Data for the table `e_pharma_customer` */

insert  into `e_pharma_customer`(`id`,`Name`,`Phone`,`Email`,`House_Name`,`Place`,`Post`,`District`,`Pin`,`Status`,`LOGIN_id`) values 
(1,'Archana Shiond','9647477880','archana123@gmail.com','Anjali','feroke','feroke','Kozhikode','679029','Approved',1),
(2,'Anu','98787655','anu123@gmail.com','Anu','Nadakav','Nadakav','Kozhikode','675432','Rejected',3),
(3,'Anusree','9810787655','anu123@gmail.com','house name','Beypore','Beypore','Kozhikode','677882','Approved',4),
(6,'yami','7484930092','yami78@gmail.com','nayomika','mankav','mankav','kozhikode','678888','Approved',7),
(7,'Ayisha M','8954321763','ayisham@gmail.com','Ayisha','madavoor','koduvally','Kozhikode','234455','Approved',8),
(8,'Archana v','9647477888','archana1233@gmail.com','Archana','vengeri','kakkodi','Kozhikode','677886','Approved',9),
(9,'Archana s','9647477888','archana97@gmail.com','Archana','Beypore','Beypore','Kozhikode','677886','pending',10),
(10,'Anjana','7865709373','anjana123@gmail.com','Anju','Kallai','Kallai','Kozhikode','677881','Rejected',11);

/*Table structure for table `e_pharma_feedback` */

DROP TABLE IF EXISTS `e_pharma_feedback`;

CREATE TABLE `e_pharma_feedback` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `Date` date NOT NULL,
  `Feedback` varchar(200) NOT NULL,
  `CUSTOMER_id` bigint(20) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `E_PHARMA_feedback_CUSTOMER_id_6c20c063_fk_E_PHARMA_customer_id` (`CUSTOMER_id`),
  CONSTRAINT `E_PHARMA_feedback_CUSTOMER_id_6c20c063_fk_E_PHARMA_customer_id` FOREIGN KEY (`CUSTOMER_id`) REFERENCES `e_pharma_customer` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=latin1;

/*Data for the table `e_pharma_feedback` */

insert  into `e_pharma_feedback`(`id`,`Date`,`Feedback`,`CUSTOMER_id`) values 
(1,'2023-10-10','sdsfde',1),
(2,'2023-10-17','good',1),
(3,'2023-10-17','better',1),
(4,'2023-11-21','good ',7),
(5,'2023-11-21','not meet my expectations',1),
(6,'2023-11-24','bbkjkk',1);

/*Table structure for table `e_pharma_inventory` */

DROP TABLE IF EXISTS `e_pharma_inventory`;

CREATE TABLE `e_pharma_inventory` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `Expiry_Date` varchar(100) NOT NULL,
  `Shelf_Code` varchar(20) NOT NULL,
  `Shelf_Rowno` varchar(20) NOT NULL,
  `Shelf_Colno` varchar(20) NOT NULL,
  `PRODUCT_id` bigint(20) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `E_PHARMA_inventory_PRODUCT_id_ff4da519_fk_E_PHARMA_stocks_id` (`PRODUCT_id`),
  CONSTRAINT `E_PHARMA_inventory_PRODUCT_id_ff4da519_fk_E_PHARMA_stocks_id` FOREIGN KEY (`PRODUCT_id`) REFERENCES `e_pharma_stocks` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=latin1;

/*Data for the table `e_pharma_inventory` */

insert  into `e_pharma_inventory`(`id`,`Expiry_Date`,`Shelf_Code`,`Shelf_Rowno`,`Shelf_Colno`,`PRODUCT_id`) values 
(1,'2023-10-12','A','1','5',1),
(2,'2023-10-15','C','1','1',2),
(3,'2025-06-11','A','3','6',3),
(4,'2027-01-04','D','2','2',4),
(5,'2023-11-30','A','4','2',5),
(6,'2023-11-20','s','2','3',12),
(7,'2023-12-07','A','3','4',15),
(9,'2023-12-07','A','1','2',1),
(10,'2023-11-29','A','12','4',1),
(11,'2024-01-11','A','2','3',1);

/*Table structure for table `e_pharma_login` */

DROP TABLE IF EXISTS `e_pharma_login`;

CREATE TABLE `e_pharma_login` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `Username` varchar(100) NOT NULL,
  `Password` varchar(50) NOT NULL,
  `Type` varchar(50) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=latin1;

/*Data for the table `e_pharma_login` */

insert  into `e_pharma_login`(`id`,`Username`,`Password`,`Type`) values 
(1,'archana1233@gmail.com','12345','Customer'),
(2,'Admin@gmail.com','admin','Admin'),
(3,'anu123@gmail.com','56789','Customer'),
(4,'anu123@gmail.com','Anusree@1234','Customer'),
(5,'anu123@gmail.com','Anusree@1234','Customer'),
(6,'anu123@gmail.com','Anusree@1234','Customer'),
(7,'yami78@gmail.com','Y123456a','Customer'),
(8,'ayisham@gmail.com','Ayisha@1','Customer'),
(9,'archana1233@gmail.com','Archana12345','Customer'),
(10,'archana97@gmail.com','Malu1234','Customer'),
(11,'anjana123@gmail.com','Anju@123','Customer');

/*Table structure for table `e_pharma_order` */

DROP TABLE IF EXISTS `e_pharma_order`;

CREATE TABLE `e_pharma_order` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `Date` date NOT NULL,
  `Total_Amount` varchar(20) NOT NULL,
  `Status` varchar(50) NOT NULL,
  `Place` varchar(100) NOT NULL,
  `Landmark` varchar(100) NOT NULL,
  `Post` varchar(100) NOT NULL,
  `District` varchar(100) NOT NULL,
  `Pin` varchar(10) NOT NULL,
  `CUSTOMER_id` bigint(20) NOT NULL,
  `PRESCRIPTION_id` bigint(20) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `E_PHARMA_order_PRESCRIPTION_id_7581b172_fk_E_PHARMA_` (`PRESCRIPTION_id`),
  KEY `E_PHARMA_order_CUSTOMER_id_5e68a410_fk_E_PHARMA_customer_id` (`CUSTOMER_id`),
  CONSTRAINT `E_PHARMA_order_CUSTOMER_id_5e68a410_fk_E_PHARMA_customer_id` FOREIGN KEY (`CUSTOMER_id`) REFERENCES `e_pharma_customer` (`id`),
  CONSTRAINT `E_PHARMA_order_PRESCRIPTION_id_7581b172_fk_E_PHARMA_` FOREIGN KEY (`PRESCRIPTION_id`) REFERENCES `e_pharma_prescription` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=83 DEFAULT CHARSET=latin1;

/*Data for the table `e_pharma_order` */

insert  into `e_pharma_order`(`id`,`Date`,`Total_Amount`,`Status`,`Place`,`Landmark`,`Post`,`District`,`Pin`,`CUSTOMER_id`,`PRESCRIPTION_id`) values 
(50,'2023-11-22','96.66','Delivered','beypore','Beypore highersecondary school','Beypore','Kozhikode','679025',1,11),
(51,'2023-11-22','150.0','Delivered','beypore','Beypore port','Beypore','Kozhikode','679025',1,11),
(52,'2023-11-23','51.3','Delivered','beypore','Beypore port','Beypore','Kozhikode','679025',1,12),
(53,'2023-11-24','111.56','Delivered','beypore','Beypore port','Beypore','Kozhikode','679025',1,13),
(54,'2023-11-24','276.8','Delivered','beypore','Beypore port','Beypore','Kozhikode','679025',1,14),
(55,'2023-11-24','111.56','Ordered','beypore','Beypore port','Beypore','Kozhikode','679025',1,13),
(56,'2023-11-24','276.8','Ordered','beypore','Beypore port','Beypore','Kozhikode','679025',1,14),
(57,'2023-11-24','61.56','Ordered','beypore','Beypore port','Beypore','Kozhikode','679025',1,13),
(58,'2023-11-24','288.36','Ordered','beypore','Beypore port','Beypore','Kozhikode','679025',1,13),
(59,'2023-11-24','288.36','Ordered','beypore','Beypore port','Beypore','Kozhikode','679025',1,14),
(60,'2023-11-24','61.56','Ordered','beypore','Beypore port','Beypore','Kozhikode','679025',1,13),
(61,'2023-11-24','61.56','Ordered','beypore','Beypore port','Beypore','Kozhikode','679025',1,13),
(62,'2023-11-24','288.36','Ordered','beypore','Beypore port','Beypore','Kozhikode','679025',1,13),
(63,'2023-11-24','288.36','Ordered','beypore','Beypore port','Beypore','Kozhikode','679025',1,14),
(64,'2023-11-24','61.56','Ordered','beypore','Beypore port','Beypore','Kozhikode','679025',1,13),
(65,'2023-11-24','288.36','Ordered','beypore','Beypore port','Beypore','Kozhikode','679025',1,13),
(66,'2023-11-24','288.36','Ordered','beypore','Beypore port','Beypore','Kozhikode','679025',1,14),
(67,'2023-11-24','61.56','Ordered','beypore','Beypore port','Beypore','Kozhikode','679025',1,13),
(68,'2023-11-24','288.36','Ordered','beypore','Beypore port','Beypore','Kozhikode','679025',1,13),
(69,'2023-11-24','288.36','Ordered','beypore','Beypore port','Beypore','Kozhikode','679025',1,14),
(70,'2023-11-24','2991.0','Ordered','beypore','Beypore port','Beypore','Kozhikode','679025',1,14),
(71,'2023-11-24','3042.3','Ordered','beypore','Beypore port','Beypore','Kozhikode','679025',1,14),
(72,'2023-11-24','61.56','Ordered','beypore','Beypore port','Beypore','Kozhikode','679025',1,13),
(73,'2023-11-24','3342.8','Ordered','beypore','Beypore port','Beypore','Kozhikode','679025',1,14),
(74,'2023-11-24','61.56','Ordered','beypore','Beypore port','Beypore','Kozhikode','679025',1,13),
(75,'2023-11-24','61.56','Ordered','beypore','Beypore port','Beypore','Kozhikode','679025',1,13),
(76,'2023-11-24','61.56','Ordered','beypore','Beypore port','Beypore','Kozhikode','679025',1,13),
(77,'2023-11-24','61.56','Ordered','beypore','Beypore port','Beypore','Kozhikode','679025',1,13),
(78,'2023-11-24','226.8','Ordered','beypore','Beypore port','Beypore','Kozhikode','679025',1,14),
(79,'2023-11-24','61.56','Ordered','beypore','Beypore port','Beypore','Kozhikode','679025',1,13),
(80,'2023-11-24','61.56','Ordered','beypore','Beypore port','Beypore','Kozhikode','679025',1,13),
(81,'2023-11-24','351.8','Ordered','beypore','Beypore port','Beypore','Kozhikode','679025',1,14),
(82,'2023-11-24','125.0','Ordered','beypore','Beypore port','Beypore','Kozhikode','679025',1,14);

/*Table structure for table `e_pharma_ordersub` */

DROP TABLE IF EXISTS `e_pharma_ordersub`;

CREATE TABLE `e_pharma_ordersub` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `Quantity` varchar(100) NOT NULL,
  `ORDER_id` bigint(20) NOT NULL,
  `PRODUCT_id` bigint(20) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `E_PHARMA_ordersub_ORDER_id_4b555d20_fk_E_PHARMA_order_id` (`ORDER_id`),
  KEY `E_PHARMA_ordersub_PRODUCT_id_eb77d4e2_fk_E_PHARMA_stocks_id` (`PRODUCT_id`),
  CONSTRAINT `E_PHARMA_ordersub_ORDER_id_4b555d20_fk_E_PHARMA_order_id` FOREIGN KEY (`ORDER_id`) REFERENCES `e_pharma_order` (`id`),
  CONSTRAINT `E_PHARMA_ordersub_PRODUCT_id_eb77d4e2_fk_E_PHARMA_stocks_id` FOREIGN KEY (`PRODUCT_id`) REFERENCES `e_pharma_stocks` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=73 DEFAULT CHARSET=latin1;

/*Data for the table `e_pharma_ordersub` */

insert  into `e_pharma_ordersub`(`id`,`Quantity`,`ORDER_id`,`PRODUCT_id`) values 
(27,'10',50,1),
(28,'2',50,5),
(29,'12',51,3),
(30,'10',52,1),
(31,'12',53,1),
(32,'10',54,5),
(33,'12',55,1),
(34,'10',56,5),
(35,'12',57,1),
(36,'12',58,1),
(37,'10',58,5),
(38,'12',59,1),
(39,'10',59,5),
(40,'12',60,1),
(41,'12',61,1),
(42,'12',62,1),
(43,'10',62,5),
(44,'12',63,1),
(45,'10',63,5),
(46,'12',64,1),
(47,'12',65,1),
(48,'10',65,5),
(49,'12',66,1),
(50,'10',66,5),
(51,'12',67,1),
(52,'12',68,1),
(53,'10',68,5),
(54,'12',69,1),
(55,'10',69,5),
(56,'10',70,4),
(57,'10',71,1),
(58,'10',71,4),
(59,'12',72,1),
(60,'10',73,5),
(61,'10',73,3),
(62,'10',73,4),
(63,'12',74,1),
(64,'12',75,1),
(65,'12',76,1),
(66,'12',77,1),
(67,'10',78,5),
(68,'12',79,1),
(69,'12',80,1),
(70,'10',81,5),
(71,'10',81,3),
(72,'10',82,3);

/*Table structure for table `e_pharma_payment` */

DROP TABLE IF EXISTS `e_pharma_payment`;

CREATE TABLE `e_pharma_payment` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `Total_Amount` varchar(20) NOT NULL,
  `Date` date NOT NULL,
  `Status` varchar(50) NOT NULL,
  `CUSTOMER_id` bigint(20) NOT NULL,
  `ORDER_id` bigint(20) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `E_PHARMA_payment_CUSTOMER_id_ae780e9b_fk_E_PHARMA_customer_id` (`CUSTOMER_id`),
  KEY `E_PHARMA_payment_ORDER_id_11661560_fk_E_PHARMA_order_id` (`ORDER_id`),
  CONSTRAINT `E_PHARMA_payment_CUSTOMER_id_ae780e9b_fk_E_PHARMA_customer_id` FOREIGN KEY (`CUSTOMER_id`) REFERENCES `e_pharma_customer` (`id`),
  CONSTRAINT `E_PHARMA_payment_ORDER_id_11661560_fk_E_PHARMA_order_id` FOREIGN KEY (`ORDER_id`) REFERENCES `e_pharma_order` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=41 DEFAULT CHARSET=latin1;

/*Data for the table `e_pharma_payment` */

insert  into `e_pharma_payment`(`id`,`Total_Amount`,`Date`,`Status`,`CUSTOMER_id`,`ORDER_id`) values 
(29,'3042.3','2023-11-24','Paid',1,71),
(30,'111.56','2023-11-24','Paid',1,72),
(31,'3342.8','2023-11-24','Paid',1,73),
(32,'111.56','2023-11-24','Paid',1,74),
(33,'111.56','2023-11-24','Paid',1,75),
(34,'111.56','2023-11-24','Paid',1,76),
(35,'111.56','2023-11-24','Paid',1,77),
(36,'226.8','2023-11-24','Paid',1,78),
(37,'111.56','2023-11-24','Paid',1,79),
(38,'61.56','2023-11-24','Paid',1,80),
(39,'351.8','2023-11-24','Paid',1,81),
(40,'125.0','2023-11-24','Paid',1,82);

/*Table structure for table `e_pharma_prescription` */

DROP TABLE IF EXISTS `e_pharma_prescription`;

CREATE TABLE `e_pharma_prescription` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `Date` date NOT NULL,
  `File` varchar(300) NOT NULL,
  `Status` varchar(50) NOT NULL,
  `USER_id` bigint(20) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `E_PHARMA_prescription_USER_id_3222ab1e_fk_E_PHARMA_customer_id` (`USER_id`),
  CONSTRAINT `E_PHARMA_prescription_USER_id_3222ab1e_fk_E_PHARMA_customer_id` FOREIGN KEY (`USER_id`) REFERENCES `e_pharma_customer` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=15 DEFAULT CHARSET=latin1;

/*Data for the table `e_pharma_prescription` */

insert  into `e_pharma_prescription`(`id`,`Date`,`File`,`Status`,`USER_id`) values 
(11,'2023-11-22','/media/prescription/20231122221702.jpeg','',1),
(12,'2023-11-23','/media/prescription/20231123112616.jpeg','',1),
(13,'2023-11-24','/media/prescription/20231124100729.jpeg','',1),
(14,'2023-11-24','/media/prescription/20231124102708.jpeg','',1);

/*Table structure for table `e_pharma_stocks` */

DROP TABLE IF EXISTS `e_pharma_stocks`;

CREATE TABLE `e_pharma_stocks` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `Product_Name` varchar(100) NOT NULL,
  `Product_image` varchar(200) NOT NULL,
  `Manufacturer_Name` varchar(100) NOT NULL,
  `Category` varchar(20) NOT NULL,
  `Quantity` varchar(100) NOT NULL,
  `Netvoldos` varchar(100) NOT NULL,
  `Price` varchar(100) NOT NULL,
  `Product_Type` varchar(100) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=23 DEFAULT CHARSET=latin1;

/*Data for the table `e_pharma_stocks` */

insert  into `e_pharma_stocks`(`id`,`Product_Name`,`Product_image`,`Manufacturer_Name`,`Category`,`Quantity`,`Netvoldos`,`Price`,`Product_Type`) values 
(1,'ACILOC RD TAB           ','/media/medicines/20231010111959.jpeg','CADIL','RX','204','32no','5.13','Tablet'),
(2,'VICKS VAPORUB         ','/media/medicines/20231015153521.jpeg','PROCTER&GAMBLE','RX','24','4gm','150','Balm'),
(3,'VELTAM .4 MG TAB ','/media/medicines/20231016203949.jpeg','INTAS','RX','26','10','12.50','1'),
(4,'LACTAGARD 1.5 INJ','/media/medicines/20231016204138.jpeg','IPCA','RX','-36','50ML','299.10','1'),
(5,'DUOLIN REPSULES ','/media/medicines/20231016204408.jpeg','CIPLA','RX','-125','3ML','22.68','1'),
(6,'VICKS VAPORUB','/media/medicines/20231016213733.jpeg','PROCTER&GAMBLE','OTC','56','10ML','120','1'),
(7,'VICKS BABYRUB','/media/medicines/20231016213842.jpeg','PROCTER&GAMBLE','OTC','78','50ML','114','1'),
(9,'VICKS VAPORUB','/media/medicines/20231016214037.jpeg','PROCTER&GAMBLE','OTC','12','5ML','65','1'),
(11,'BOROLINE','/media/medicines/20231016214424.jpeg','G.D PHARMACEUTICALS','OTC','100','20GM','40','1'),
(12,'MOVE PAINRELIEF  ','/media/medicines/20231016214705.jpeg','RECKITT BENCKISER','RX','39','15ML','75','Ointment'),
(13,'VICKS BABYRUB','/media/medicines/20231016215021.jpeg','PROCTER&GAMBLE','OTC','28','10ML','56','1'),
(15,'PARACETAMOL 500mg','/media/medicines/20231121150215.jpeg','FARMSON PHARMACEUTICAL PVT LTD','RX','450','10ML','40','1'),
(22,'ARD TAB','/media/medicines/20231124170021.jpeg','CADIL','RX','19','5.13','23','Tablet');

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
