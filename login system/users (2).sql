-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Apr 30, 2022 at 12:24 AM
-- Server version: 10.4.22-MariaDB
-- PHP Version: 8.0.15

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `users`
--

-- --------------------------------------------------------

--
-- Table structure for table `users`
--

CREATE TABLE `users` (
  `sno` int(255) NOT NULL,
  `username` varchar(255) NOT NULL,
  `password` varchar(255) NOT NULL,
  `email` varchar(255) NOT NULL,
  `dt` datetime NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `users`
--

INSERT INTO `users` (`sno`, `username`, `password`, `email`, `dt`) VALUES
(1, 'paras', 'paras', 'paras@gmail.com', '2022-02-22 18:14:51'),
(3, 'Paras1', '$2y$10$g9HyrdakobCExBZVfpeiUeJvZ/gVVcIUwZDiX3xzCrYM0twzJe7Ey', 'paras1@gmail.com', '2022-02-23 21:47:00'),
(4, 'test', '$2y$10$ak.H1Esaiu5kVhHWtguwF.LMa5psqDPpx.KqjPS.jbPuSlOTL.Z2i', 'test@gmail.com', '2022-02-24 04:18:27'),
(5, 'aaaaa', '$2y$10$H4B82/qNDeGDBByzBJJDa.hje2GmV9PcpJHnXrk6UItXdz7REsgQu', 'aaaaa@gmail.com', '2022-02-24 04:20:17'),
(6, 'abc', 'abc', 'abc@gmail.com', '2022-02-24 04:21:44'),
(8, 'testing', 'testing', 'testing@gmail.com', '2022-02-25 10:58:20'),
(9, 'Papu', 'papu', 'papu@gmail.com', '2022-02-27 16:00:43'),
(10, 'aaa', '47bce5c74f589f4867dbd57e9ca9f808', 'aaa@gmail.com', '2022-03-01 08:09:37'),
(11, 'update', 'update', 'zzz@gmail.com', '2022-03-02 10:37:11'),
(12, 'alex', '534b44a19bf18d20b71ecc4eb77c572f', 'alex@gmail.com', '2022-03-03 10:38:43'),
(13, 'tom', '34b7da764b21d298ef307d04d8152dc5', 'tom@gmail.com', '2022-03-03 10:39:03'),
(14, 'sachin', '15285722f9def45c091725aee9c387cb', 'sachin@gmail.com', '2022-03-03 10:39:30'),
(17, 'crop', 'a634e7960e04b1633c103382004fe526', 'crop@gmail.com', '2022-04-06 11:31:06'),
(18, 'govind', '2654f4a1c04731cd0b9a50382d5031cd', 'govind@gmail.com', '2022-04-06 12:56:21');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `users`
--
ALTER TABLE `users`
  ADD PRIMARY KEY (`sno`),
  ADD UNIQUE KEY `username` (`username`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `users`
--
ALTER TABLE `users`
  MODIFY `sno` int(255) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=19;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
