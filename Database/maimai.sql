/*
Navicat MySQL Data Transfer

Source Server         : maimai
Source Server Version : 50718
Source Host           : 192.168.1.105:3306
Source Database       : maimai

Target Server Type    : MYSQL
Target Server Version : 50718
File Encoding         : 65001

Date: 2017-06-29 01:11:52
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for baseitem
-- ----------------------------
DROP TABLE IF EXISTS `baseitem`;
CREATE TABLE `baseitem` (
  `id` varchar(30) DEFAULT NULL,
  `name` varchar(100) DEFAULT NULL,
  `sex` varchar(10) DEFAULT NULL,
  `birthday` varchar(10) DEFAULT NULL,
  `img` varchar(500) DEFAULT NULL,
  `description` varchar(500) DEFAULT NULL,
  `work_city` varchar(30) DEFAULT NULL,
  `birth_city` varchar(30) DEFAULT NULL,
  `xingzuo` varchar(30) DEFAULT NULL,
  `tag` varchar(500) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Table structure for eduitem
-- ----------------------------
DROP TABLE IF EXISTS `eduitem`;
CREATE TABLE `eduitem` (
  `id` varchar(30) DEFAULT NULL,
  `school` varchar(500) DEFAULT NULL,
  `degree` varchar(10) DEFAULT NULL,
  `department` varchar(500) DEFAULT NULL,
  `start_date` varchar(20) DEFAULT NULL,
  `end_date` varchar(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Table structure for workitem
-- ----------------------------
DROP TABLE IF EXISTS `workitem`;
CREATE TABLE `workitem` (
  `id` varchar(30) DEFAULT NULL,
  `company` varchar(500) DEFAULT NULL,
  `position` varchar(500) DEFAULT NULL,
  `description` varchar(500) DEFAULT NULL,
  `start_date` varchar(20) DEFAULT NULL,
  `end_date` varchar(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
