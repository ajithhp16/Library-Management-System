-- phpMyAdmin SQL Dump
-- version 4.7.9
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1:3306
-- Generation Time: Mar 26, 2023 at 02:29 PM
-- Server version: 5.7.21
-- PHP Version: 5.6.35

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `library_management_system`
--
CREATE DATABASE IF NOT EXISTS `library_management_system` DEFAULT CHARACTER SET latin1 COLLATE latin1_swedish_ci;
USE `library_management_system`;

-- --------------------------------------------------------

--
-- Table structure for table `authors`
--

DROP TABLE IF EXISTS `authors`;
CREATE TABLE IF NOT EXISTS `authors` (
  `id` int(20) NOT NULL AUTO_INCREMENT,
  `NAME` varchar(200) NOT NULL,
  `ADDRESS` varchar(200) DEFAULT NULL,
  `PHONE_NUMBER` varchar(200) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=11003 DEFAULT CHARSET=latin1;

--
-- Truncate table before insert `authors`
--

TRUNCATE TABLE `authors`;
--
-- Dumping data for table `authors`
--

INSERT INTO `authors` (`id`, `NAME`, `ADDRESS`, `PHONE_NUMBER`) VALUES
(11001, 'Chethan Bhaskar', 'Mysore', '9876543210'),
(11002, 'Monish Iyengar', 'Hubli', '9753124680');

-- --------------------------------------------------------

--
-- Table structure for table `books`
--

DROP TABLE IF EXISTS `books`;
CREATE TABLE IF NOT EXISTS `books` (
  `id` int(20) NOT NULL AUTO_INCREMENT,
  `NAME` varchar(200) NOT NULL,
  `AUTHOR_ID` int(20) NOT NULL,
  `PUBLISHER_ID` int(20) NOT NULL,
  `PRICE` float NOT NULL,
  `PUBLICATION_DATE` date NOT NULL,
  `LANGUAGE_ID` int(20) NOT NULL,
  `EDITION` varchar(200) DEFAULT NULL,
  `SECTION` varchar(200) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `AUTHOR_ID` (`AUTHOR_ID`),
  KEY `PUBLISHER_ID` (`PUBLISHER_ID`),
  KEY `LANGUAGE_ID` (`LANGUAGE_ID`)
) ENGINE=MyISAM AUTO_INCREMENT=40006 DEFAULT CHARSET=latin1;

--
-- Truncate table before insert `books`
--

TRUNCATE TABLE `books`;
--
-- Dumping data for table `books`
--

INSERT INTO `books` (`id`, `NAME`, `AUTHOR_ID`, `PUBLISHER_ID`, `PRICE`, `PUBLICATION_DATE`, `LANGUAGE_ID`, `EDITION`, `SECTION`) VALUES
(40001, 'Once Apon A Time', 11001, 10002, 280, '2019-02-26', 13001, 'First', 'Fiction'),
(40002, 'Never Before', 11002, 10001, 320, '2012-12-12', 13005, 'First', 'Science'),
(40003, 'To Begin With', 11002, 10002, 199, '2022-01-01', 13001, 'First', 'Maths'),
(40004, 'World Of Happiness', 11001, 10001, 249, '2020-10-08', 13001, 'First', 'Fiction'),
(40005, 'Believe And Become', 11001, 10001, 449, '2023-02-01', 13002, 'Second', 'Motivation');

-- --------------------------------------------------------

--
-- Table structure for table `books_available`
--

DROP TABLE IF EXISTS `books_available`;
CREATE TABLE IF NOT EXISTS `books_available` (
  `id` int(20) NOT NULL AUTO_INCREMENT,
  `BOOK_ID` int(20) NOT NULL,
  `LIBRARY_ID` int(20) NOT NULL,
  `COUNT_AVAILABLE` int(20) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `BOOK_ID` (`BOOK_ID`),
  KEY `LIBRARY_ID` (`LIBRARY_ID`)
) ENGINE=MyISAM AUTO_INCREMENT=70008 DEFAULT CHARSET=latin1;

--
-- Truncate table before insert `books_available`
--

TRUNCATE TABLE `books_available`;
--
-- Dumping data for table `books_available`
--

INSERT INTO `books_available` (`id`, `BOOK_ID`, `LIBRARY_ID`, `COUNT_AVAILABLE`) VALUES
(70001, 40001, 12002, 6),
(70002, 40005, 12001, 3),
(70003, 40001, 12001, 4),
(70004, 40002, 12001, 9),
(70005, 40003, 12002, 8),
(70006, 40005, 12002, 6),
(70007, 40004, 12001, 10);

-- --------------------------------------------------------

--
-- Table structure for table `books_borrowed`
--

DROP TABLE IF EXISTS `books_borrowed`;
CREATE TABLE IF NOT EXISTS `books_borrowed` (
  `id` int(20) NOT NULL AUTO_INCREMENT,
  `BOOK_ID` int(20) NOT NULL,
  `USER_ID` int(20) NOT NULL,
  `LIBRARY_ID` int(20) NOT NULL,
  `ISSUED_DATE` datetime NOT NULL,
  `ISSUED_LIBRARIAN_ID` int(20) NOT NULL,
  `DUE_DATE` datetime NOT NULL,
  `COLLECTED_DATE` datetime DEFAULT NULL,
  `COLLECTED_LIBRARIAN_ID` int(20) DEFAULT NULL,
  `FINE_COLLECTED` float NOT NULL,
  `STATUS` varchar(200) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `BOOK_ID` (`BOOK_ID`),
  KEY `USER_ID` (`USER_ID`),
  KEY `LIBRARY_ID` (`LIBRARY_ID`),
  KEY `ISSUED_LIBRARIAN_ID` (`ISSUED_LIBRARIAN_ID`),
  KEY `COLLECTED_LIBRARIAN_ID` (`COLLECTED_LIBRARIAN_ID`)
) ENGINE=MyISAM AUTO_INCREMENT=50007 DEFAULT CHARSET=latin1;

--
-- Truncate table before insert `books_borrowed`
--

TRUNCATE TABLE `books_borrowed`;
--
-- Dumping data for table `books_borrowed`
--

INSERT INTO `books_borrowed` (`id`, `BOOK_ID`, `USER_ID`, `LIBRARY_ID`, `ISSUED_DATE`, `ISSUED_LIBRARIAN_ID`, `DUE_DATE`, `COLLECTED_DATE`, `COLLECTED_LIBRARIAN_ID`, `FINE_COLLECTED`, `STATUS`) VALUES
(50001, 40005, 20003, 12001, '2016-06-26 13:30:00', 30002, '2015-07-11 13:29:59', '2015-07-10 10:25:00', 30005, 0, 'Collected'),
(50002, 40004, 20001, 12002, '2019-12-02 15:45:20', 30003, '2019-12-17 15:44:19', '2019-12-18 12:44:19', 30003, 10, 'Collected'),
(50003, 40001, 20001, 12001, '2023-03-10 16:02:30', 30001, '2023-03-25 16:02:29', '2023-03-26 11:31:09', 30001, 5, 'Collected'),
(50004, 40001, 20004, 12002, '2023-03-15 10:22:45', 30004, '2023-03-30 10:22:44', '2023-03-26 13:12:18', 30004, 0, 'Collected'),
(50005, 40003, 20001, 12001, '2023-03-18 17:56:10', 30002, '2023-04-02 17:56:09', '2023-03-26 11:40:11', 30001, 0, 'Collected'),
(50006, 40002, 20001, 12001, '2023-03-26 12:52:15', 30001, '2023-04-10 12:52:15', NULL, NULL, 0, 'Pending');

-- --------------------------------------------------------

--
-- Table structure for table `ebooks`
--

DROP TABLE IF EXISTS `ebooks`;
CREATE TABLE IF NOT EXISTS `ebooks` (
  `id` int(20) NOT NULL AUTO_INCREMENT,
  `BOOK_ID` int(20) NOT NULL,
  `EXTENSION` varchar(200) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `BOOK_ID` (`BOOK_ID`)
) ENGINE=MyISAM AUTO_INCREMENT=60006 DEFAULT CHARSET=latin1;

--
-- Truncate table before insert `ebooks`
--

TRUNCATE TABLE `ebooks`;
--
-- Dumping data for table `ebooks`
--

INSERT INTO `ebooks` (`id`, `BOOK_ID`, `EXTENSION`) VALUES
(60001, 40001, 'http://onceaponatime.aws.in'),
(60002, 40002, 'https://neverbefore.youtube.com'),
(60003, 40004, 'http://worldofhappiness.cloud.eu'),
(60004, 40005, 'http://believeandbecome.aws.in'),
(60005, 40003, 'https://tobeginwith.aws.in');

-- --------------------------------------------------------

--
-- Table structure for table `languages`
--

DROP TABLE IF EXISTS `languages`;
CREATE TABLE IF NOT EXISTS `languages` (
  `id` int(20) NOT NULL AUTO_INCREMENT,
  `NAME` varchar(200) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=13007 DEFAULT CHARSET=latin1;

--
-- Truncate table before insert `languages`
--

TRUNCATE TABLE `languages`;
--
-- Dumping data for table `languages`
--

INSERT INTO `languages` (`id`, `NAME`) VALUES
(13001, 'English'),
(13002, 'Kannada'),
(13003, 'Hindi'),
(13004, 'Telugu'),
(13005, 'German');

-- --------------------------------------------------------

--
-- Table structure for table `librarians`
--

DROP TABLE IF EXISTS `librarians`;
CREATE TABLE IF NOT EXISTS `librarians` (
  `id` int(20) NOT NULL AUTO_INCREMENT,
  `LIBRARY_ID` int(20) NOT NULL,
  `NAME` varchar(200) NOT NULL,
  `GENDER` varchar(20) NOT NULL,
  `PHONE_NUMBER` varchar(200) NOT NULL,
  `MAIL_ID` varchar(200) NOT NULL,
  `LIBRARIAN_PASSWORD` varchar(200) NOT NULL,
  `ORIGINAL_ADDRESS` varchar(200) NOT NULL,
  `PRESENT_ADDRESS` varchar(200) NOT NULL,
  `IS_ROOT` varchar(200) NOT NULL,
  `IS_ACTIVE` varchar(200) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `LIBRARY_ID` (`LIBRARY_ID`)
) ENGINE=MyISAM AUTO_INCREMENT=30009 DEFAULT CHARSET=latin1;

--
-- Truncate table before insert `librarians`
--

TRUNCATE TABLE `librarians`;
--
-- Dumping data for table `librarians`
--

INSERT INTO `librarians` (`id`, `LIBRARY_ID`, `NAME`, `GENDER`, `PHONE_NUMBER`, `MAIL_ID`, `LIBRARIAN_PASSWORD`, `ORIGINAL_ADDRESS`, `PRESENT_ADDRESS`, `IS_ROOT`, `IS_ACTIVE`) VALUES
(30001, 12001, 'Savitha K T', 'FEMALE', '9699981729', 'savithakt@gmail.com', 'Savitha@1403', 'Choodasandra, Bangalore', 'Choodasandra, Bangalore', 'Yes', 'Yes'),
(30002, 12001, 'Amrutha Setty', 'FEMALE', '7022230222', 'amruthasetty@gmail.com', 'Amrutha@2209', 'JP Nagar, Bangalore', 'JP Nagar, Bangalore', 'No', 'Yes'),
(30003, 12002, 'Nagendra Setty', 'MALE', '7445454725', 'nagendrasetty@gmail.com', 'Nagendra@1212', 'JP Nagar, Bangalore', 'JP Nagar, Bangalore', 'Yes', 'No'),
(30004, 12002, 'Samarth Reddy', 'MALE', '9612345666', 'samarthreddy@gmail.com', 'Samarth@0408', 'Doddakannelli, Bangalore', 'Doddakannelli, Bangalore', 'No', 'Yes'),
(30005, 12001, 'Charvik Gowda', 'MALE', '9900705114', 'charvikgowda@gmail.com', 'Charvik@1001', 'Doddakannelli, Bangalore', 'Doddakannelli, Bangalore', 'No', 'No'),
(30006, 12001, 'Gopal G', 'MALE', '9074321010', 'gopalg@gmail.com', 'GopalG@1212', 'Honnavar, Dakshina Kannada', 'Srirangapatna, Mysore', 'No', 'No'),
(30007, 12002, 'Saraswati', 'FEMALE', '8800660044', 'saraswati@gmail.com', 'Saraswati@1001', 'Kushal Nagar, Kodagu', 'Kalyan Nagar, Bengaluru', 'Yes', 'No'),
(30008, 12001, 'Vishnu Dev', 'MALE', '8765432109', 'vishnudev12@gmail.com', 'Vishnu@12', 'Rona, Hubli', 'Siddhartha Layout, Mysore', 'No', 'No');

-- --------------------------------------------------------

--
-- Table structure for table `libraries`
--

DROP TABLE IF EXISTS `libraries`;
CREATE TABLE IF NOT EXISTS `libraries` (
  `id` int(20) NOT NULL AUTO_INCREMENT,
  `ADDRESS` varchar(200) NOT NULL,
  `CITY` varchar(200) NOT NULL,
  `STATE` varchar(200) NOT NULL,
  `PINCODE` varchar(200) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=12004 DEFAULT CHARSET=latin1;

--
-- Truncate table before insert `libraries`
--

TRUNCATE TABLE `libraries`;
--
-- Dumping data for table `libraries`
--

INSERT INTO `libraries` (`id`, `ADDRESS`, `CITY`, `STATE`, `PINCODE`) VALUES
(12001, 'Agara', 'Bangalore', 'Karnataka', '560035'),
(12002, 'JP Nagar', 'Hassan', 'Karnataka', '561032'),
(12003, 'Palace Road', 'Mysore', 'Karnataka', '571011');

-- --------------------------------------------------------

--
-- Table structure for table `publishers`
--

DROP TABLE IF EXISTS `publishers`;
CREATE TABLE IF NOT EXISTS `publishers` (
  `id` int(20) NOT NULL AUTO_INCREMENT,
  `NAME` varchar(200) NOT NULL,
  `ADDRESS` varchar(200) DEFAULT NULL,
  `PHONE_NUMBER` varchar(200) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=10003 DEFAULT CHARSET=latin1;

--
-- Truncate table before insert `publishers`
--

TRUNCATE TABLE `publishers`;
--
-- Dumping data for table `publishers`
--

INSERT INTO `publishers` (`id`, `NAME`, `ADDRESS`, `PHONE_NUMBER`) VALUES
(10001, 'SLV Publishers', 'Chikpet, Bangalore', '9080706050'),
(10002, 'GK Publishers', 'Koramangala, Bangalore', '9988776655');

-- --------------------------------------------------------

--
-- Table structure for table `users`
--

DROP TABLE IF EXISTS `users`;
CREATE TABLE IF NOT EXISTS `users` (
  `id` int(20) NOT NULL AUTO_INCREMENT,
  `NAME` varchar(200) NOT NULL,
  `FATHER_NAME` varchar(200) DEFAULT NULL,
  `GENDER` varchar(20) NOT NULL,
  `PHONE_NUMBER` varchar(200) NOT NULL,
  `MAIL_ID` varchar(200) NOT NULL,
  `USER_PASSWORD` varchar(200) NOT NULL,
  `ORIGINAL_ADDRESS` varchar(200) NOT NULL,
  `PRESENT_ADDRESS` varchar(200) NOT NULL,
  `IS_ACTIVE` varchar(20) NOT NULL,
  `BOOKS_COUNT_ALLOWED` int(20) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=20006 DEFAULT CHARSET=latin1;

--
-- Truncate table before insert `users`
--

TRUNCATE TABLE `users`;
--
-- Dumping data for table `users`
--

INSERT INTO `users` (`id`, `NAME`, `FATHER_NAME`, `GENDER`, `PHONE_NUMBER`, `MAIL_ID`, `USER_PASSWORD`, `ORIGINAL_ADDRESS`, `PRESENT_ADDRESS`, `IS_ACTIVE`, `BOOKS_COUNT_ALLOWED`) VALUES
(20001, 'Ajith K P', 'Pradeep M J', 'MALE', '8971090984', 'ajithkp@gmail.com', 'Ajith@1234', 'Choodasandra, Bangalore', 'Choodasandra, Bangalore', 'Yes', 1),
(20002, 'Drupad C J', 'Satish Setty', 'MALE', '7232328027', 'drupadcj1998@gmail.com', 'Drupad@1007', 'Navrang Circle, Bangalore', 'Navrang Circle, Bangalore', 'No', 0),
(20003, 'Smruthi D P', 'Dattatreya', 'FEMALE', '8073009996', 'smruthidp@gmail.com', 'Smruthi@0712', 'Hoodi, Bangalore', 'Hoodi, Bangalore', 'No', 0),
(20004, 'Deepthi L T', 'Chandrappa', 'FEMALE', '9144040261', 'deepthilt@gmail.com', 'Deepthi@2103', 'Channasandra, Bangalore', 'Channasandra, Bangalore', 'Yes', 2),
(20005, 'Shreyas K V', 'Suresh', 'MALE', '8023212122', 'shreyaskv@gmail.com', 'Shreyas@1212', 'Vijay Nagar, Mysore', 'Doddakannelli, Bengaluru', 'No', 0);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
