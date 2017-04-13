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

 Date: 04/13/2017 22:25:09 PM
*/

SET NAMES utf8;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
--  Table structure for `AnyScanUI_cms_poc_chil`
-- ----------------------------
DROP TABLE IF EXISTS `AnyScanUI_cms_poc_chil`;
CREATE TABLE `AnyScanUI_cms_poc_chil` (
  `id` varchar(40) COLLATE utf8_bin NOT NULL,
  `poc_type` varchar(40) COLLATE utf8_bin NOT NULL,
  `poc_num` varchar(200) COLLATE utf8_bin NOT NULL,
  `log` varchar(5000) COLLATE utf8_bin NOT NULL,
  `pid_id` varchar(40) COLLATE utf8_bin NOT NULL,
  `target` varchar(5000) COLLATE utf8_bin NOT NULL,
  `poc_name` varchar(200) COLLATE utf8_bin NOT NULL,
  PRIMARY KEY (`id`),
  KEY `AnyScanUI_cms_poc_c_pid_id_6f1cecbe_fk_AnyScanUI_cms_poc_main_id` (`pid_id`),
  CONSTRAINT `AnyScanUI_cms_poc_c_pid_id_6f1cecbe_fk_AnyScanUI_cms_poc_main_id` FOREIGN KEY (`pid_id`) REFERENCES `AnyScanUI_cms_poc_main` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;

-- ----------------------------
--  Table structure for `AnyScanUI_cms_poc_main`
-- ----------------------------
DROP TABLE IF EXISTS `AnyScanUI_cms_poc_main`;
CREATE TABLE `AnyScanUI_cms_poc_main` (
  `id` varchar(40) COLLATE utf8_bin NOT NULL,
  `start_time` varchar(50) COLLATE utf8_bin NOT NULL,
  `end_time` varchar(50) COLLATE utf8_bin NOT NULL,
  `log` varchar(5000) COLLATE utf8_bin NOT NULL,
  `threads` varchar(10) COLLATE utf8_bin NOT NULL,
  `status` varchar(10) COLLATE utf8_bin NOT NULL,
  `locker` varchar(5) COLLATE utf8_bin NOT NULL,
  `poc_size` varchar(200) COLLATE utf8_bin NOT NULL,
  `progress` varchar(50) COLLATE utf8_bin NOT NULL,
  `target` varchar(5000) COLLATE utf8_bin NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;

-- ----------------------------
--  Table structure for `AnyScanUI_cmsinfo`
-- ----------------------------
DROP TABLE IF EXISTS `AnyScanUI_cmsinfo`;
CREATE TABLE `AnyScanUI_cmsinfo` (
  `id` varchar(40) COLLATE utf8_bin NOT NULL,
  `host` varchar(500) COLLATE utf8_bin NOT NULL,
  `url_list` longtext COLLATE utf8_bin NOT NULL,
  `start_time` varchar(50) COLLATE utf8_bin NOT NULL,
  `end_time` varchar(50) COLLATE utf8_bin NOT NULL,
  `log` varchar(5000) COLLATE utf8_bin NOT NULL,
  `progress` varchar(50) COLLATE utf8_bin NOT NULL,
  `threads` varchar(10) COLLATE utf8_bin NOT NULL,
  `status` varchar(10) COLLATE utf8_bin NOT NULL,
  `locker` varchar(5) COLLATE utf8_bin NOT NULL,
  `cms` varchar(50) COLLATE utf8_bin NOT NULL,
  `payload` varchar(300) COLLATE utf8_bin NOT NULL,
  `version` varchar(50) COLLATE utf8_bin NOT NULL,
  `keyword` varchar(50) COLLATE utf8_bin NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;

-- ----------------------------
--  Table structure for `AnyScanUI_poc_chil`
-- ----------------------------
DROP TABLE IF EXISTS `AnyScanUI_poc_chil`;
CREATE TABLE `AnyScanUI_poc_chil` (
  `id` varchar(40) COLLATE utf8_bin NOT NULL,
  `commond` varchar(200) COLLATE utf8_bin NOT NULL,
  `vulnerable` varchar(10) COLLATE utf8_bin NOT NULL,
  `host` varchar(500) COLLATE utf8_bin NOT NULL,
  `keyword` longtext COLLATE utf8_bin NOT NULL,
  `pid_id` varchar(40) COLLATE utf8_bin NOT NULL,
  `name` varchar(500) COLLATE utf8_bin NOT NULL,
  PRIMARY KEY (`id`),
  KEY `AnyScanUI_poc_chil_pid_id_7a95cb3c_fk_AnyScanUI_poc_main_id` (`pid_id`),
  CONSTRAINT `AnyScanUI_poc_chil_pid_id_7a95cb3c_fk_AnyScanUI_poc_main_id` FOREIGN KEY (`pid_id`) REFERENCES `AnyScanUI_poc_main` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;

-- ----------------------------
--  Table structure for `AnyScanUI_poc_main`
-- ----------------------------
DROP TABLE IF EXISTS `AnyScanUI_poc_main`;
CREATE TABLE `AnyScanUI_poc_main` (
  `id` varchar(40) COLLATE utf8_bin NOT NULL,
  `commond` varchar(200) COLLATE utf8_bin NOT NULL,
  `start_time` varchar(50) COLLATE utf8_bin NOT NULL,
  `end_time` varchar(50) COLLATE utf8_bin NOT NULL,
  `log` varchar(5000) COLLATE utf8_bin NOT NULL,
  `progress` varchar(50) COLLATE utf8_bin NOT NULL,
  `threads` varchar(10) COLLATE utf8_bin NOT NULL,
  `status` varchar(10) COLLATE utf8_bin NOT NULL,
  `locker` varchar(5) COLLATE utf8_bin NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;

-- ----------------------------
--  Table structure for `AnyScanUI_poc_urls`
-- ----------------------------
DROP TABLE IF EXISTS `AnyScanUI_poc_urls`;
CREATE TABLE `AnyScanUI_poc_urls` (
  `id` varchar(40) COLLATE utf8_bin NOT NULL,
  `commond` varchar(200) COLLATE utf8_bin NOT NULL,
  `start_time` varchar(50) COLLATE utf8_bin NOT NULL,
  `end_time` varchar(50) COLLATE utf8_bin NOT NULL,
  `log` varchar(5000) COLLATE utf8_bin NOT NULL,
  `urls` longtext COLLATE utf8_bin NOT NULL,
  `counts` varchar(50) COLLATE utf8_bin NOT NULL,
  `threads` varchar(10) COLLATE utf8_bin NOT NULL,
  `status` varchar(10) COLLATE utf8_bin NOT NULL,
  `locker` varchar(5) COLLATE utf8_bin NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;

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
  `locker` varchar(5) COLLATE utf8_bin NOT NULL,
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
  `name` varchar(80) COLLATE utf8_bin NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;

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
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;

-- ----------------------------
--  Table structure for `auth_permission`
-- ----------------------------
DROP TABLE IF EXISTS `auth_permission`;
CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) COLLATE utf8_bin NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) COLLATE utf8_bin NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permissi_content_type_id_2f476e4b_fk_django_content_type_id` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=49 DEFAULT CHARSET=utf8 COLLATE=utf8_bin;

-- ----------------------------
--  Records of `auth_permission`
-- ----------------------------
BEGIN;
INSERT INTO `auth_permission` VALUES ('1', 'Can add log entry', '1', 'add_logentry'), ('2', 'Can change log entry', '1', 'change_logentry'), ('3', 'Can delete log entry', '1', 'delete_logentry'), ('4', 'Can add permission', '2', 'add_permission'), ('5', 'Can change permission', '2', 'change_permission'), ('6', 'Can delete permission', '2', 'delete_permission'), ('7', 'Can add user', '3', 'add_user'), ('8', 'Can change user', '3', 'change_user'), ('9', 'Can delete user', '3', 'delete_user'), ('10', 'Can add group', '4', 'add_group'), ('11', 'Can change group', '4', 'change_group'), ('12', 'Can delete group', '4', 'delete_group'), ('13', 'Can add content type', '5', 'add_contenttype'), ('14', 'Can change content type', '5', 'change_contenttype'), ('15', 'Can delete content type', '5', 'delete_contenttype'), ('16', 'Can add session', '6', 'add_session'), ('17', 'Can change session', '6', 'change_session'), ('18', 'Can delete session', '6', 'delete_session'), ('19', 'Can add site', '7', 'add_site'), ('20', 'Can change site', '7', 'change_site'), ('21', 'Can delete site', '7', 'delete_site'), ('22', 'Can add user', '8', 'add_user'), ('23', 'Can change user', '8', 'change_user'), ('24', 'Can delete user', '8', 'delete_user'), ('25', 'Can add port crack child', '9', 'add_portcrackchild'), ('26', 'Can change port crack child', '9', 'change_portcrackchild'), ('27', 'Can delete port crack child', '9', 'delete_portcrackchild'), ('28', 'Can add port crack', '10', 'add_portcrack'), ('29', 'Can change port crack', '10', 'change_portcrack'), ('30', 'Can delete port crack', '10', 'delete_portcrack'), ('31', 'Can add cms info', '11', 'add_cmsinfo'), ('32', 'Can change cms info', '11', 'change_cmsinfo'), ('33', 'Can delete cms info', '11', 'delete_cmsinfo'), ('34', 'Can add poc_chil', '12', 'add_poc_chil'), ('35', 'Can change poc_chil', '12', 'change_poc_chil'), ('36', 'Can delete poc_chil', '12', 'delete_poc_chil'), ('37', 'Can add poc_main', '13', 'add_poc_main'), ('38', 'Can change poc_main', '13', 'change_poc_main'), ('39', 'Can delete poc_main', '13', 'delete_poc_main'), ('40', 'Can add poc_urls', '14', 'add_poc_urls'), ('41', 'Can change poc_urls', '14', 'change_poc_urls'), ('42', 'Can delete poc_urls', '14', 'delete_poc_urls'), ('43', 'Can add cms_poc_chil', '15', 'add_cms_poc_chil'), ('44', 'Can change cms_poc_chil', '15', 'change_cms_poc_chil'), ('45', 'Can delete cms_poc_chil', '15', 'delete_cms_poc_chil'), ('46', 'Can add cms_poc_main', '16', 'add_cms_poc_main'), ('47', 'Can change cms_poc_main', '16', 'change_cms_poc_main'), ('48', 'Can delete cms_poc_main', '16', 'delete_cms_poc_main');
COMMIT;

-- ----------------------------
--  Table structure for `auth_user`
-- ----------------------------
DROP TABLE IF EXISTS `auth_user`;
CREATE TABLE `auth_user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `password` varchar(128) COLLATE utf8_bin NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) COLLATE utf8_bin NOT NULL,
  `first_name` varchar(30) COLLATE utf8_bin NOT NULL,
  `last_name` varchar(30) COLLATE utf8_bin NOT NULL,
  `email` varchar(254) COLLATE utf8_bin NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;

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
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;

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
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;

-- ----------------------------
--  Table structure for `class`
-- ----------------------------
DROP TABLE IF EXISTS `class`;
CREATE TABLE `class` (
  `id` int(11) DEFAULT NULL,
  `classname` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
--  Records of `class`
-- ----------------------------
BEGIN;
INSERT INTO `class` VALUES ('1', 'class_1');
COMMIT;

-- ----------------------------
--  Table structure for `django_admin_log`
-- ----------------------------
DROP TABLE IF EXISTS `django_admin_log`;
CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext COLLATE utf8_bin,
  `object_repr` varchar(200) COLLATE utf8_bin NOT NULL,
  `action_flag` smallint(5) unsigned NOT NULL,
  `change_message` longtext COLLATE utf8_bin NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin__content_type_id_c4bce8eb_fk_django_content_type_id` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`),
  CONSTRAINT `django_admin__content_type_id_c4bce8eb_fk_django_content_type_id` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;

-- ----------------------------
--  Table structure for `django_content_type`
-- ----------------------------
DROP TABLE IF EXISTS `django_content_type`;
CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) COLLATE utf8_bin NOT NULL,
  `model` varchar(100) COLLATE utf8_bin NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=17 DEFAULT CHARSET=utf8 COLLATE=utf8_bin;

-- ----------------------------
--  Records of `django_content_type`
-- ----------------------------
BEGIN;
INSERT INTO `django_content_type` VALUES ('15', 'AnyScanUI', 'cms_poc_chil'), ('16', 'AnyScanUI', 'cms_poc_main'), ('11', 'AnyScanUI', 'cmsinfo'), ('12', 'AnyScanUI', 'poc_chil'), ('13', 'AnyScanUI', 'poc_main'), ('14', 'AnyScanUI', 'poc_urls'), ('10', 'AnyScanUI', 'portcrack'), ('9', 'AnyScanUI', 'portcrackchild'), ('8', 'AnyScanUI', 'user'), ('1', 'admin', 'logentry'), ('4', 'auth', 'group'), ('2', 'auth', 'permission'), ('3', 'auth', 'user'), ('5', 'contenttypes', 'contenttype'), ('6', 'sessions', 'session'), ('7', 'sites', 'site');
COMMIT;

-- ----------------------------
--  Table structure for `django_migrations`
-- ----------------------------
DROP TABLE IF EXISTS `django_migrations`;
CREATE TABLE `django_migrations` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app` varchar(255) COLLATE utf8_bin NOT NULL,
  `name` varchar(255) COLLATE utf8_bin NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=38 DEFAULT CHARSET=utf8 COLLATE=utf8_bin;

-- ----------------------------
--  Records of `django_migrations`
-- ----------------------------
BEGIN;
INSERT INTO `django_migrations` VALUES ('1', 'AnyScanUI', '0001_initial', '2017-03-13 00:51:52.442675'), ('2', 'AnyScanUI', '0002_portcrack', '2017-03-13 00:51:52.469150'), ('3', 'AnyScanUI', '0003_auto_20170221_0555', '2017-03-13 00:51:52.510395'), ('4', 'AnyScanUI', '0004_auto_20170221_0648', '2017-03-13 00:51:52.554288'), ('5', 'AnyScanUI', '0005_auto_20170223_0656', '2017-03-13 00:51:52.695426'), ('6', 'AnyScanUI', '0006_portcrack_success_num', '2017-03-13 00:51:52.732820'), ('7', 'AnyScanUI', '0007_auto_20170224_0305', '2017-03-13 00:51:52.800062'), ('8', 'AnyScanUI', '0008_auto_20170224_0744', '2017-03-13 00:51:52.864156'), ('9', 'AnyScanUI', '0009_portcrackchild_threads', '2017-03-13 00:51:52.895825'), ('10', 'AnyScanUI', '0010_portcrackchild_locker', '2017-03-13 00:51:52.928553'), ('11', 'AnyScanUI', '0011_cmsinfo', '2017-03-13 00:51:52.947084'), ('12', 'AnyScanUI', '0012_auto_20170308_1242', '2017-03-13 00:51:53.031510'), ('13', 'AnyScanUI', '0013_cmsinfo_keyword', '2017-03-13 00:51:53.063683'), ('14', 'AnyScanUI', '0014_auto_20170312_1342', '2017-03-13 00:51:53.159665'), ('15', 'contenttypes', '0001_initial', '2017-03-13 00:51:53.194108'), ('16', 'auth', '0001_initial', '2017-03-13 00:51:53.518592'), ('17', 'admin', '0001_initial', '2017-03-13 00:51:53.585784'), ('18', 'admin', '0002_logentry_remove_auto_add', '2017-03-13 00:51:53.618850'), ('19', 'contenttypes', '0002_remove_content_type_name', '2017-03-13 00:51:53.687263'), ('20', 'auth', '0002_alter_permission_name_max_length', '2017-03-13 00:51:53.718848'), ('21', 'auth', '0003_alter_user_email_max_length', '2017-03-13 00:51:53.752158'), ('22', 'auth', '0004_alter_user_username_opts', '2017-03-13 00:51:53.765687'), ('23', 'auth', '0005_alter_user_last_login_null', '2017-03-13 00:51:53.798160'), ('24', 'auth', '0006_require_contenttypes_0002', '2017-03-13 00:51:53.800505'), ('25', 'auth', '0007_alter_validators_add_error_messages', '2017-03-13 00:51:53.814554'), ('26', 'auth', '0008_alter_user_username_max_length', '2017-03-13 00:51:53.844191'), ('27', 'sessions', '0001_initial', '2017-03-13 00:51:53.879258'), ('28', 'sites', '0001_initial', '2017-03-13 00:51:53.899146'), ('29', 'sites', '0002_alter_domain_unique', '2017-03-13 00:51:53.921632'), ('30', 'AnyScanUI', '0015_poc_urls', '2017-03-14 10:21:14.132087'), ('31', 'AnyScanUI', '0016_auto_20170315_1215', '2017-03-15 12:15:13.664012'), ('32', 'AnyScanUI', '0017_poc_chil_name', '2017-03-22 02:47:03.020246'), ('33', 'AnyScanUI', '0018_auto_20170323_0541', '2017-03-23 05:41:58.847285'), ('34', 'AnyScanUI', '0019_auto_20170408_0406', '2017-04-08 04:06:44.821699'), ('35', 'AnyScanUI', '0020_auto_20170408_0421', '2017-04-08 04:21:46.259030'), ('36', 'AnyScanUI', '0021_cms_poc_chil_poc_name', '2017-04-08 04:30:40.696862'), ('37', 'AnyScanUI', '0022_auto_20170408_0459', '2017-04-08 04:59:32.398587');
COMMIT;

-- ----------------------------
--  Table structure for `django_session`
-- ----------------------------
DROP TABLE IF EXISTS `django_session`;
CREATE TABLE `django_session` (
  `session_key` varchar(40) COLLATE utf8_bin NOT NULL,
  `session_data` longtext COLLATE utf8_bin NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_de54fa62` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;

-- ----------------------------
--  Table structure for `django_site`
-- ----------------------------
DROP TABLE IF EXISTS `django_site`;
CREATE TABLE `django_site` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `domain` varchar(100) COLLATE utf8_bin NOT NULL,
  `name` varchar(50) COLLATE utf8_bin NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_site_domain_a2e37b91_uniq` (`domain`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8 COLLATE=utf8_bin;

-- ----------------------------
--  Records of `django_site`
-- ----------------------------
BEGIN;
INSERT INTO `django_site` VALUES ('1', 'example.com', 'example.com');
COMMIT;

-- ----------------------------
--  Table structure for `student`
-- ----------------------------
DROP TABLE IF EXISTS `student`;
CREATE TABLE `student` (
  `id` int(11) DEFAULT NULL,
  `name` varchar(255) DEFAULT NULL,
  `country` varchar(255) DEFAULT NULL,
  `class_id` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
--  Records of `student`
-- ----------------------------
BEGIN;
INSERT INTO `student` VALUES ('1', 'stu1', '1', '1'), ('2', 'stu2', '2', '2');
COMMIT;

SET FOREIGN_KEY_CHECKS = 1;
