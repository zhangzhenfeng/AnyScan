/*
 Navicat Premium Data Transfer

 Source Server         : localhost
 Source Server Type    : MySQL
 Source Server Version : 50717
 Source Host           : localhost
 Source Database       : anyscan

 Target Server Type    : MySQL
 Target Server Version : 50717
 File Encoding         : utf-8

 Date: 03/02/2017 17:15:56 PM
*/

SET NAMES utf8;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
--  Table structure for `AnyScanUI_portcrack`
-- ----------------------------
DROP TABLE IF EXISTS `AnyScanUI_portcrack`;
CREATE TABLE `AnyScanUI_portcrack` (
  `id` varchar(40) COLLATE utf8_bin NOT NULL,
  `start_time` varchar(50) COLLATE utf8_bin NOT NULL,
  `end_time` varchar(50) COLLATE utf8_bin NOT NULL,
  `result` varchar(5000) COLLATE utf8_bin NOT NULL,
  `status` varchar(10) COLLATE utf8_bin NOT NULL,
  `type` varchar(10) COLLATE utf8_bin NOT NULL,
  `log` varchar(5000) COLLATE utf8_bin NOT NULL,
  `progress` varchar(50) COLLATE utf8_bin NOT NULL,
  `success_num` varchar(10) COLLATE utf8_bin NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;

-- ----------------------------
--  Table structure for `AnyScanUI_portcrackchild`
-- ----------------------------
DROP TABLE IF EXISTS `AnyScanUI_portcrackchild`;
CREATE TABLE `AnyScanUI_portcrackchild` (
  `id` varchar(40) COLLATE utf8_bin NOT NULL,
  `start_time` varchar(50) COLLATE utf8_bin NOT NULL,
  `end_time` varchar(50) COLLATE utf8_bin NOT NULL,
  `username` varchar(50) COLLATE utf8_bin NOT NULL,
  `password` varchar(50) COLLATE utf8_bin NOT NULL,
  `status` varchar(10) COLLATE utf8_bin NOT NULL,
  `type` varchar(10) COLLATE utf8_bin NOT NULL,
  `log` varchar(5000) COLLATE utf8_bin NOT NULL,
  `progress` varchar(50) COLLATE utf8_bin NOT NULL,
  `pid_id` varchar(40) COLLATE utf8_bin NOT NULL,
  `ip` varchar(50) COLLATE utf8_bin NOT NULL,
  `port` varchar(50) COLLATE utf8_bin NOT NULL,
  `attack_queue_list` longtext COLLATE utf8_bin NOT NULL,
  `old_queue_size` varchar(20) COLLATE utf8_bin NOT NULL,
  `threads` varchar(10) COLLATE utf8_bin NOT NULL,
  PRIMARY KEY (`id`),
  KEY `AnyScanUI_portcrackchi_pid_id_c26b4db0_fk_AnyScanUI_portcrack_id` (`pid_id`),
  CONSTRAINT `AnyScanUI_portcrackchi_pid_id_c26b4db0_fk_AnyScanUI_portcrack_id` FOREIGN KEY (`pid_id`) REFERENCES `AnyScanUI_portcrack` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;

-- ----------------------------
--  Table structure for `AnyScanUI_user`
-- ----------------------------
DROP TABLE IF EXISTS `AnyScanUI_user`;
CREATE TABLE `AnyScanUI_user` (
  `id` varchar(32) COLLATE utf8_bin NOT NULL,
  `username` varchar(50) COLLATE utf8_bin NOT NULL,
  `password` varchar(50) COLLATE utf8_bin NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;

-- ----------------------------
--  Table structure for `auth_group`
-- ----------------------------
DROP TABLE IF EXISTS `auth_group`;
CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(80) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- ----------------------------
--  Table structure for `auth_group_permissions`
-- ----------------------------
DROP TABLE IF EXISTS `auth_group_permissions`;
CREATE TABLE `auth_group_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissi_permission_id_84c5c92e_fk_auth_permission_id` (`permission_id`),
  CONSTRAINT `auth_group_permissi_permission_id_84c5c92e_fk_auth_permission_id` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- ----------------------------
--  Table structure for `auth_permission`
-- ----------------------------
DROP TABLE IF EXISTS `auth_permission`;
CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permissi_content_type_id_2f476e4b_fk_django_content_type_id` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=37 DEFAULT CHARSET=latin1;

-- ----------------------------
--  Records of `auth_permission`
-- ----------------------------
BEGIN;
INSERT INTO `auth_permission` VALUES ('1', 'Can add log entry', '1', 'add_logentry'), ('2', 'Can change log entry', '1', 'change_logentry'), ('3', 'Can delete log entry', '1', 'delete_logentry'), ('4', 'Can add permission', '2', 'add_permission'), ('5', 'Can change permission', '2', 'change_permission'), ('6', 'Can delete permission', '2', 'delete_permission'), ('7', 'Can add user', '3', 'add_user'), ('8', 'Can change user', '3', 'change_user'), ('9', 'Can delete user', '3', 'delete_user'), ('10', 'Can add group', '4', 'add_group'), ('11', 'Can change group', '4', 'change_group'), ('12', 'Can delete group', '4', 'delete_group'), ('13', 'Can add content type', '5', 'add_contenttype'), ('14', 'Can change content type', '5', 'change_contenttype'), ('15', 'Can delete content type', '5', 'delete_contenttype'), ('16', 'Can add session', '6', 'add_session'), ('17', 'Can change session', '6', 'change_session'), ('18', 'Can delete session', '6', 'delete_session'), ('19', 'Can add site', '7', 'add_site'), ('20', 'Can change site', '7', 'change_site'), ('21', 'Can delete site', '7', 'delete_site'), ('22', 'Can add user', '8', 'add_user'), ('23', 'Can change user', '8', 'change_user'), ('24', 'Can delete user', '8', 'delete_user'), ('25', 'Can add port crack', '9', 'add_portcrack'), ('26', 'Can change port crack', '9', 'change_portcrack'), ('27', 'Can delete port crack', '9', 'delete_portcrack'), ('28', 'Can add user', '10', 'add_user'), ('29', 'Can change user', '10', 'change_user'), ('30', 'Can delete user', '10', 'delete_user'), ('31', 'Can add port crack', '11', 'add_portcrack'), ('32', 'Can change port crack', '11', 'change_portcrack'), ('33', 'Can delete port crack', '11', 'delete_portcrack'), ('34', 'Can add port crack child', '12', 'add_portcrackchild'), ('35', 'Can change port crack child', '12', 'change_portcrackchild'), ('36', 'Can delete port crack child', '12', 'delete_portcrackchild');
COMMIT;

-- ----------------------------
--  Table structure for `auth_user`
-- ----------------------------
DROP TABLE IF EXISTS `auth_user`;
CREATE TABLE `auth_user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(30) NOT NULL,
  `last_name` varchar(30) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- ----------------------------
--  Table structure for `auth_user_groups`
-- ----------------------------
DROP TABLE IF EXISTS `auth_user_groups`;
CREATE TABLE `auth_user_groups` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_groups_user_id_94350c0c_uniq` (`user_id`,`group_id`),
  KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`),
  CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- ----------------------------
--  Table structure for `auth_user_user_permissions`
-- ----------------------------
DROP TABLE IF EXISTS `auth_user_user_permissions`;
CREATE TABLE `auth_user_user_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_user_permissions_user_id_14a6b632_uniq` (`user_id`,`permission_id`),
  KEY `auth_user_user_perm_permission_id_1fbb5f2c_fk_auth_permission_id` (`permission_id`),
  CONSTRAINT `auth_user_user_perm_permission_id_1fbb5f2c_fk_auth_permission_id` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- ----------------------------
--  Table structure for `django_admin_log`
-- ----------------------------
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
  KEY `django_admin__content_type_id_c4bce8eb_fk_django_content_type_id` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`),
  CONSTRAINT `django_admin__content_type_id_c4bce8eb_fk_django_content_type_id` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- ----------------------------
--  Table structure for `django_content_type`
-- ----------------------------
DROP TABLE IF EXISTS `django_content_type`;
CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=latin1;

-- ----------------------------
--  Records of `django_content_type`
-- ----------------------------
BEGIN;
INSERT INTO `django_content_type` VALUES ('1', 'admin', 'logentry'), ('11', 'AnyScanUI', 'portcrack'), ('12', 'AnyScanUI', 'portcrackchild'), ('10', 'AnyScanUI', 'user'), ('4', 'auth', 'group'), ('2', 'auth', 'permission'), ('3', 'auth', 'user'), ('5', 'contenttypes', 'contenttype'), ('6', 'sessions', 'session'), ('7', 'sites', 'site'), ('9', 'SQLMapUI', 'portcrack'), ('8', 'SQLMapUI', 'user');
COMMIT;

-- ----------------------------
--  Table structure for `django_migrations`
-- ----------------------------
DROP TABLE IF EXISTS `django_migrations`;
CREATE TABLE `django_migrations` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=29 DEFAULT CHARSET=latin1;

-- ----------------------------
--  Records of `django_migrations`
-- ----------------------------
BEGIN;
INSERT INTO `django_migrations` VALUES ('1', 'contenttypes', '0001_initial', '2017-01-17 05:33:20.242313'), ('2', 'auth', '0001_initial', '2017-01-17 05:33:20.599384'), ('3', 'admin', '0001_initial', '2017-01-17 05:33:20.675907'), ('4', 'admin', '0002_logentry_remove_auto_add', '2017-01-17 05:33:20.711854'), ('5', 'contenttypes', '0002_remove_content_type_name', '2017-01-17 05:33:20.794714'), ('6', 'auth', '0002_alter_permission_name_max_length', '2017-01-17 05:33:20.820361'), ('7', 'auth', '0003_alter_user_email_max_length', '2017-01-17 05:33:20.841315'), ('8', 'auth', '0004_alter_user_username_opts', '2017-01-17 05:33:20.852464'), ('9', 'auth', '0005_alter_user_last_login_null', '2017-01-17 05:33:20.881113'), ('10', 'auth', '0006_require_contenttypes_0002', '2017-01-17 05:33:20.883565'), ('11', 'auth', '0007_alter_validators_add_error_messages', '2017-01-17 05:33:20.896275'), ('12', 'auth', '0008_alter_user_username_max_length', '2017-01-17 05:33:20.925892'), ('13', 'sessions', '0001_initial', '2017-01-17 05:33:20.959363'), ('14', 'sites', '0001_initial', '2017-01-17 05:33:20.980293'), ('15', 'sites', '0002_alter_domain_unique', '2017-01-17 05:33:20.998294'), ('16', 'SQLMapUI', '0001_initial', '2017-01-17 08:55:19.318032'), ('17', 'SQLMapUI', '0002_portcrack', '2017-02-20 06:02:17.720875'), ('18', 'SQLMapUI', '0003_auto_20170221_0555', '2017-02-21 05:55:42.712400'), ('19', 'SQLMapUI', '0004_auto_20170221_0648', '2017-02-21 06:49:01.586193'), ('20', 'AnyScanUI', '0001_initial', '2017-02-21 08:48:12.283305'), ('21', 'AnyScanUI', '0002_portcrack', '2017-02-21 08:48:12.307719'), ('22', 'AnyScanUI', '0003_auto_20170221_0555', '2017-02-21 08:48:12.347399'), ('23', 'AnyScanUI', '0004_auto_20170221_0648', '2017-02-21 08:48:12.394870'), ('24', 'AnyScanUI', '0005_auto_20170223_0656', '2017-02-23 06:56:34.341235'), ('25', 'AnyScanUI', '0006_portcrack_success_num', '2017-02-23 08:32:18.107182'), ('26', 'AnyScanUI', '0007_auto_20170224_0305', '2017-02-24 03:05:58.364124'), ('27', 'AnyScanUI', '0008_auto_20170224_0744', '2017-02-24 07:45:02.199626'), ('28', 'AnyScanUI', '0009_portcrackchild_threads', '2017-02-24 08:51:58.388500');
COMMIT;

-- ----------------------------
--  Table structure for `django_session`
-- ----------------------------
DROP TABLE IF EXISTS `django_session`;
CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_de54fa62` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- ----------------------------
--  Table structure for `django_site`
-- ----------------------------
DROP TABLE IF EXISTS `django_site`;
CREATE TABLE `django_site` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `domain` varchar(100) NOT NULL,
  `name` varchar(50) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_site_domain_a2e37b91_uniq` (`domain`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

-- ----------------------------
--  Records of `django_site`
-- ----------------------------
BEGIN;
INSERT INTO `django_site` VALUES ('1', 'example.com', 'example.com');
COMMIT;

SET FOREIGN_KEY_CHECKS = 1;
