-- phpMyAdmin SQL Dump
-- version 5.0.2
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1:3306
-- Tempo de geração: 27-Nov-2021 às 22:23
-- Versão do servidor: 5.7.31
-- versão do PHP: 7.3.21

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Banco de dados: `cadastro_doacao`
--

-- --------------------------------------------------------

--
-- Estrutura da tabela `tabela`
--

DROP TABLE IF EXISTS `tabela`;
CREATE TABLE IF NOT EXISTS `tabela` (
  `doacao` int(20) NOT NULL,
  `parceiro` varchar(50) NOT NULL,
  `cpf_cnpj` int(12) NOT NULL,
  `descricao` text NOT NULL,
  `data_doacao` date NOT NULL,
  `quantidade_kg` double NOT NULL,
  `categoria` varchar(50) NOT NULL,
  PRIMARY KEY (`doacao`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
