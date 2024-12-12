-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Dec 12, 2024 at 08:14 AM
-- Server version: 10.4.32-MariaDB
-- PHP Version: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `kakanin_hub`
--

-- --------------------------------------------------------

--
-- Table structure for table `orders`
--

CREATE TABLE `orders` (
  `id` int(11) NOT NULL,
  `customer_name` varchar(255) NOT NULL,
  `address` varchar(255) NOT NULL,
  `product_id` int(11) NOT NULL,
  `quantity` int(11) NOT NULL,
  `total_price` decimal(10,2) NOT NULL,
  `delivery_date` date DEFAULT NULL,
  `delivery_time` time DEFAULT NULL,
  `contact_number` varchar(15) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `orders`
--

INSERT INTO `orders` (`id`, `customer_name`, `address`, `product_id`, `quantity`, `total_price`, `delivery_date`, `delivery_time`, `contact_number`) VALUES
(2, 'cj', 'as-is', 3, 3, 8100.00, '2024-12-25', '10:00:00', '09091570012'),
(3, 'criezel', 'as-is', 3, 3, 4050.00, '2024-12-26', '10:00:00', '09461981974'),
(4, 'JEZIE', 'GAHOL', 2, 2, 1400.00, '2024-12-30', '13:00:00', '096541234789'),
(5, 'patrick ', 'bauan, batangas', 10, 2, 700.00, '2024-12-23', '12:00:00', '09821332344'),
(6, 'xyna', 'sta.teresita', 8, 2, 900.00, '2024-12-14', '11:00:00', '09876523215'),
(7, 'lucky', 'sta.teresita', 6, 2, 1200.00, '2025-01-01', '18:00:00', '09345678754'),
(8, 'james', 'san pascual', 7, 3, 1050.00, '2025-01-01', '10:00:00', '09312932564');

-- --------------------------------------------------------

--
-- Table structure for table `products`
--

CREATE TABLE `products` (
  `id` int(11) NOT NULL,
  `name` varchar(255) NOT NULL,
  `price` decimal(10,2) NOT NULL,
  `size` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `products`
--

INSERT INTO `products` (`id`, `name`, `price`, `size`) VALUES
(1, 'maja', 350.00, '12'),
(2, 'maja', 350.00, '12'),
(3, 'biko', 450.00, '14'),
(4, 'biko', 600.00, '16'),
(6, 'maja', 600.00, '16'),
(7, 'maja corn', 350.00, '12'),
(8, 'mahja corn', 450.00, '14'),
(9, 'maja corn', 600.00, '16'),
(10, 'biko', 350.00, '12');

-- --------------------------------------------------------

--
-- Table structure for table `users`
--

CREATE TABLE `users` (
  `id` int(11) NOT NULL,
  `email` varchar(255) NOT NULL,
  `password` varchar(255) NOT NULL,
  `role` enum('admin','customer') NOT NULL DEFAULT 'customer'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `users`
--

INSERT INTO `users` (`id`, `email`, `password`, `role`) VALUES
(1, 'admin@gmail.com', 'admin123', 'admin'),
(5, 'cj@gmail.com', '$2b$12$zyosYmlOqbKqZV0jebRak..VphdT553MPBxKBiLcpBZf.8eCfKtVG', 'customer'),
(6, 'jezie@gmail.com', '$2b$12$TEY34h2FSZNfnFcGbQMUxuZvpxoGnsH0th5prIUIKFwE73YlZw/wO', 'customer'),
(7, 'micheal@gmail.com', '$2b$12$xKIxYyxum2g/coi0bXW93uYj5h59A6S8BnzkWvkyblQLOj4z.pzTu', 'customer'),
(8, 'eloisa@gmail.com', '$2b$12$E8dWM1l9.I2kXbUSCrooQelE2O59YP.xmdynITJkn9epH4dgwNmoG', 'customer'),
(9, 'lucky09@gmail.com', '$2b$12$cZSyQegsSASkhbKyGmbJ.OcC/Nx73JcI4WQk/l410jYp2Dnt2vpG2', 'customer'),
(10, 'xyna@gmail.com', '$2b$12$cOWTcMFagKTUw1LiqjzMR.3TkmOFiAHH/OQcc4/jEIAAmmgW3Awxy', 'customer'),
(11, 'patrick@gmail.com', '$2b$12$..SQhInY8Kai8V8tDpoWtO6vwY3kFrFdSmbS2WbuEgW/wJE3xWhou', 'customer'),
(12, 'xyrel@gmail.com', '$2b$12$nyWSvlcM0grk1ZKOI/pKTeRM1rvCb0xBGG0SeDRqcPLYAvDM2WHhu', 'customer'),
(13, 'james@gmail.com', '$2b$12$0kgyYYA7YvFvda.y/yRu9.TBAJYYTJj31Rwy0PyaEGQny9kNE7d6i', 'customer'),
(14, 'nadine@gmail.com', '$2b$12$.iNaSCzYawOhvz4QC4Nb2.LMMpf2bstjJZxvadfFv1shQM7mxavKW', 'customer');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `orders`
--
ALTER TABLE `orders`
  ADD PRIMARY KEY (`id`),
  ADD KEY `product_id` (`product_id`);

--
-- Indexes for table `products`
--
ALTER TABLE `products`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `users`
--
ALTER TABLE `users`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `email` (`email`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `orders`
--
ALTER TABLE `orders`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=10;

--
-- AUTO_INCREMENT for table `products`
--
ALTER TABLE `products`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=12;

--
-- AUTO_INCREMENT for table `users`
--
ALTER TABLE `users`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=15;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `orders`
--
ALTER TABLE `orders`
  ADD CONSTRAINT `orders_ibfk_1` FOREIGN KEY (`product_id`) REFERENCES `products` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
