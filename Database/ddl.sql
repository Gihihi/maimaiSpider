/*
Navicat MySQL Data Transfer

Source Server         : maimai
Source Server Version : 50718
Source Host           : 192.168.1.105:3306
Source Database       : maimai

Target Server Type    : MYSQL
Target Server Version : 50718
File Encoding         : 65001

Date: 2017-07-08 21:57:39
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for baseitem
-- ----------------------------
DROP TABLE IF EXISTS `baseitem`;
CREATE TABLE `baseitem` (
  `id` varchar(100) DEFAULT NULL,
  `name` varchar(100) DEFAULT NULL,
  `sex` varchar(100) DEFAULT NULL,
  `birthday` varchar(100) DEFAULT NULL,
  `img` varchar(2000) DEFAULT NULL,
  `company` varchar(100) DEFAULT NULL,
  `position` varchar(100) DEFAULT NULL,
  `work_city` varchar(100) DEFAULT NULL,
  `birth_city` varchar(100) DEFAULT NULL,
  `xingzuo` varchar(100) DEFAULT NULL,
  `tag` varchar(2000) DEFAULT NULL,
  `url` varchar(2000) DEFAULT NULL,
  `flag` varchar(10) DEFAULT NULL COMMENT '校验位'
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Table structure for commentitem
-- ----------------------------
DROP TABLE IF EXISTS `commentitem`;
CREATE TABLE `commentitem` (
  `id` varchar(100) DEFAULT NULL,
  `friend_id` varchar(100) DEFAULT NULL,
  `friend_name` varchar(100) DEFAULT NULL,
  `friend_company` varchar(100) DEFAULT NULL,
  `friend_position` varchar(100) DEFAULT NULL,
  `level` varchar(2000) DEFAULT NULL,
  `comment` varchar(2000) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Table structure for cookies
-- ----------------------------
DROP TABLE IF EXISTS `cookies`;
CREATE TABLE `cookies` (
  `text` varchar(500) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Table structure for eduitem
-- ----------------------------
DROP TABLE IF EXISTS `eduitem`;
CREATE TABLE `eduitem` (
  `id` varchar(100) DEFAULT NULL,
  `school` varchar(500) DEFAULT NULL,
  `degree` varchar(100) DEFAULT NULL,
  `department` varchar(2000) DEFAULT NULL,
  `start_date` varchar(100) DEFAULT NULL,
  `end_date` varchar(100) DEFAULT NULL,
  `flag` varchar(5) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Table structure for simpleitem
-- ----------------------------
DROP TABLE IF EXISTS `simpleitem`;
CREATE TABLE `simpleitem` (
  `id` varchar(500) DEFAULT NULL,
  `cid` varchar(500) DEFAULT NULL,
  `name` varchar(500) DEFAULT NULL,
  `loc` varchar(500) DEFAULT NULL,
  `company` varchar(500) DEFAULT NULL,
  `position` varchar(500) DEFAULT NULL,
  `encode_mmid` varchar(500) DEFAULT NULL,
  `url` varchar(1000) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Table structure for simpleitem_search
-- ----------------------------
DROP TABLE IF EXISTS `simpleitem_search`;
CREATE TABLE `simpleitem_search` (
  `id` varchar(500) DEFAULT NULL,
  `cid` varchar(500) DEFAULT NULL,
  `name` varchar(500) DEFAULT NULL,
  `loc` varchar(500) DEFAULT NULL,
  `company` varchar(500) DEFAULT NULL,
  `position` varchar(500) DEFAULT NULL,
  `encode_mmid` varchar(500) DEFAULT NULL,
  `url` varchar(1000) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Table structure for workitem
-- ----------------------------
DROP TABLE IF EXISTS `workitem`;
CREATE TABLE `workitem` (
  `id` varchar(100) DEFAULT NULL,
  `company` varchar(2000) DEFAULT NULL,
  `position` varchar(2000) DEFAULT NULL,
  `description` varchar(2000) DEFAULT NULL,
  `start_date` varchar(100) DEFAULT NULL,
  `end_date` varchar(100) DEFAULT NULL,
  `flag` varchar(5) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
