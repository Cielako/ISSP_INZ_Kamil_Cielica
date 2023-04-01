-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Czas generowania: 29 Mar 2023, 21:33
-- Wersja serwera: 10.4.24-MariaDB
-- Wersja PHP: 8.0.19

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Baza danych: `sitedb`
--

-- --------------------------------------------------------

--
-- Struktura tabeli dla tabeli `accounts_account`
--

CREATE TABLE `accounts_account` (
  `id` bigint(20) NOT NULL,
  `password` varchar(128) NOT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `first_name` varchar(150) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  `username` varchar(35) NOT NULL,
  `email` varchar(65) NOT NULL,
  `last_login` date NOT NULL,
  `phone` varchar(128) NOT NULL,
  `region` varchar(19) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Zrzut danych tabeli `accounts_account`
--

INSERT INTO `accounts_account` (`id`, `password`, `is_superuser`, `first_name`, `last_name`, `is_staff`, `is_active`, `date_joined`, `username`, `email`, `last_login`, `phone`, `region`) VALUES
(1, 'pbkdf2_sha256$390000$DKNBMk5ABSzgVfGj897YQp$r0CJvObsJqfE1CH8P1a7Mt1WJLgarBkWnuohBSF41KY=', 1, '', '', 1, 1, '2022-12-03 16:04:24.000000', 'admin', 'cielak.dev@gmail.com', '2023-03-27', '', 'Inna lokalizacja'),
(2, 'pbkdf2_sha256$390000$dfkHa4C1xWmJDJRZa3LHHL$BN9Qtwzt8poyedS20esEH0IERERciZ6EjNhdaukilSs=', 0, 'Hzjsj', 'Ngsjsj', 0, 0, '2022-12-04 10:38:36.000000', 'pietrek', 'boben@gmail.com', '2023-03-26', '+48453203123', 'Dolnośląskie'),
(3, 'pbkdf2_sha256$390000$M7H2Ppf9ufFLTsT6mDN37F$0Je1t2avITI/03xnVbu/exmxWdyZn6iLf8m7zkL5lfI=', 0, '', '', 0, 1, '2022-12-04 15:15:24.000000', '123', 'cielakfake@gmail.com', '2022-12-10', '', 'Dolnośląskie'),
(5, 'pbkdf2_sha256$390000$EZtZOZPueMEAJRljowcPTM$oclZL0e1E+kUjoPVXm4vxuCQeqVGEevwQe5QV6iXWDY=', 0, 'dad', 'adsd', 0, 1, '2022-12-28 21:31:37.000000', 'sads', 'adsdaa@gmail.com', '2023-03-26', '+48123132123', 'Zachodnio-pomorskie'),
(6, 'pbkdf2_sha256$390000$YsHMiDx6cDE2vCDJ1NsnDG$dgCUAlqgHdOBzpDBTSbqFB+RlIKjLM+h83sDzq1LfFE=', 0, '', '', 0, 1, '2023-01-07 19:18:29.000000', '12345', 'asdadsasd@gmail.com', '2023-03-26', '', 'Inna lokalizacja'),
(7, 'pbkdf2_sha256$390000$ZTqsWOvkbMDvSvpYWZOeYx$puYG/kc4i34A9DaLFbgtZzYO6Sbg/EBi+hk7A9ip+Fs=', 0, '', '', 0, 1, '2023-01-07 20:20:14.352883', 'pietrek2', 'dupol@gmail.com', '2023-01-07', '', 'Inna lokalizacja'),
(8, 'pbkdf2_sha256$390000$0hblFhV65Z8LnrAst9QQFx$HDsFBLEtkeVMVXvnS0RvVSVzZl8/51xPBDWTaSWTBWU=', 0, 'Jan', 'Kowalski', 0, 1, '2023-01-07 20:36:18.468122', 'pietrek3', 'donnos@gmail.com', '2023-01-07', '', 'Inna lokalizacja'),
(9, 'pbkdf2_sha256$390000$edROtfX06CtOuHGyXMSo20$1hKYzY7R07K/Q2ehWmhhVnOQSAAslspaJ3PCDxYt0CU=', 0, 'Andrzej', 'Stasiek', 0, 1, '2023-01-16 19:20:16.776251', 'testowy_user', 'testow2y@gmail.com', '2023-01-16', '+48123456789', 'Dolnośląskie'),
(10, 'pbkdf2_sha256$390000$c6jcYTduoEuCCdLqoUKMcn$EBogjw1jiJQ3CKyl0aeL1iUcgdgxEibNuYgwIQzDIWw=', 0, '', '', 0, 0, '2023-01-16 19:23:59.000000', 'testowy_telefon', 'testowy_telefon@gmail.com', '2023-03-27', '', 'Inna lokalizacja'),
(13, 'pbkdf2_sha256$390000$Ca6zUziZfUrAtd7EHHRoS7$mAg/ZNcZLJFgngESmdrp5n4HX+a+t7K/KnP87fqAd10=', 0, 'jan', 'testowy', 0, 1, '2023-03-27 19:06:46.924346', 'test', 'testowysd@gmail.com', '2023-03-27', '+48790790443', 'Dolnośląskie');

-- --------------------------------------------------------

--
-- Struktura tabeli dla tabeli `accounts_account_groups`
--

CREATE TABLE `accounts_account_groups` (
  `id` bigint(20) NOT NULL,
  `account_id` bigint(20) NOT NULL,
  `group_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Struktura tabeli dla tabeli `accounts_account_user_permissions`
--

CREATE TABLE `accounts_account_user_permissions` (
  `id` bigint(20) NOT NULL,
  `account_id` bigint(20) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Zrzut danych tabeli `accounts_account_user_permissions`
--

INSERT INTO `accounts_account_user_permissions` (`id`, `account_id`, `permission_id`) VALUES
(1, 2, 22),
(2, 3, 22),
(4, 5, 22),
(5, 6, 22),
(6, 7, 22),
(7, 8, 22),
(8, 9, 22),
(9, 10, 22),
(12, 13, 22);

-- --------------------------------------------------------

--
-- Struktura tabeli dla tabeli `auth_group`
--

CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL,
  `name` varchar(150) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Struktura tabeli dla tabeli `auth_group_permissions`
--

CREATE TABLE `auth_group_permissions` (
  `id` bigint(20) NOT NULL,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Struktura tabeli dla tabeli `auth_permission`
--

CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Zrzut danych tabeli `auth_permission`
--

INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES
(1, 'Can add log entry', 1, 'add_logentry'),
(2, 'Can change log entry', 1, 'change_logentry'),
(3, 'Can delete log entry', 1, 'delete_logentry'),
(4, 'Can view log entry', 1, 'view_logentry'),
(5, 'Can add permission', 2, 'add_permission'),
(6, 'Can change permission', 2, 'change_permission'),
(7, 'Can delete permission', 2, 'delete_permission'),
(8, 'Can view permission', 2, 'view_permission'),
(9, 'Can add group', 3, 'add_group'),
(10, 'Can change group', 3, 'change_group'),
(11, 'Can delete group', 3, 'delete_group'),
(12, 'Can view group', 3, 'view_group'),
(13, 'Can add content type', 4, 'add_contenttype'),
(14, 'Can change content type', 4, 'change_contenttype'),
(15, 'Can delete content type', 4, 'delete_contenttype'),
(16, 'Can view content type', 4, 'view_contenttype'),
(17, 'Can add session', 5, 'add_session'),
(18, 'Can change session', 5, 'change_session'),
(19, 'Can delete session', 5, 'delete_session'),
(20, 'Can view session', 5, 'view_session'),
(21, 'Can add user', 6, 'add_account'),
(22, 'Can change user', 6, 'change_account'),
(23, 'Can delete user', 6, 'delete_account'),
(24, 'Can view user', 6, 'view_account'),
(25, 'Can add pet profile', 7, 'add_petprofile'),
(26, 'Can change pet profile', 7, 'change_petprofile'),
(27, 'Can delete pet profile', 7, 'delete_petprofile'),
(28, 'Can view pet profile', 7, 'view_petprofile');

-- --------------------------------------------------------

--
-- Struktura tabeli dla tabeli `django_admin_log`
--

CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext DEFAULT NULL,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) UNSIGNED NOT NULL CHECK (`action_flag` >= 0),
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` bigint(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Zrzut danych tabeli `django_admin_log`
--

INSERT INTO `django_admin_log` (`id`, `action_time`, `object_id`, `object_repr`, `action_flag`, `change_message`, `content_type_id`, `user_id`) VALUES
(1, '2022-12-10 15:53:03.986992', '1', 'admin', 2, '[{\"changed\": {\"fields\": [\"Wojew\\u00f3dztwo\"]}}]', 6, 1),
(2, '2022-12-10 15:53:08.908668', '1', 'admin', 2, '[{\"changed\": {\"fields\": [\"Wojew\\u00f3dztwo\"]}}]', 6, 1),
(3, '2022-12-10 16:05:04.552475', '1', 'admin', 2, '[]', 6, 1),
(4, '2022-12-10 16:05:10.084099', '3', '123', 2, '[{\"changed\": {\"fields\": [\"Wojew\\u00f3dztwo\"]}}]', 6, 1),
(5, '2022-12-10 16:15:23.238577', '1', 'admin', 2, '[{\"changed\": {\"fields\": [\"Wojew\\u00f3dztwo\"]}}]', 6, 1),
(6, '2022-12-10 16:18:10.608615', '3', '123', 2, '[{\"changed\": {\"fields\": [\"Wojew\\u00f3dztwo\"]}}]', 6, 1),
(7, '2022-12-10 16:18:16.580253', '2', 'pietrek', 2, '[{\"changed\": {\"fields\": [\"Wojew\\u00f3dztwo\"]}}]', 6, 1),
(8, '2022-12-10 18:29:45.505395', '16', '2133214', 2, '[{\"changed\": {\"fields\": [\"P\\u0142e\\u0107\", \"Zdj\\u0119cie\"]}}]', 7, 1),
(9, '2022-12-11 12:33:03.882399', '17', '129089102982130', 2, '[{\"changed\": {\"fields\": [\"Gatunek\", \"P\\u0142e\\u0107\", \"Zdj\\u0119cie\", \"Status zagini\\u0119cia\"]}}]', 7, 1),
(10, '2022-12-11 12:40:50.389794', '17', '129089102982130', 2, '[{\"changed\": {\"fields\": [\"P\\u0142e\\u0107\", \"Zdj\\u0119cie\"]}}]', 7, 1),
(11, '2022-12-11 15:12:30.758341', '17', '129089102982130', 3, '', 7, 1),
(12, '2022-12-21 20:17:49.549004', '30', '123213', 1, '[{\"added\": {}}]', 7, 1),
(13, '2022-12-21 20:18:13.264764', '31', '12323', 1, '[{\"added\": {}}]', 7, 1),
(14, '2023-01-01 11:04:11.269099', '4', '11111111111111111111111111111111111', 3, '', 6, 1),
(15, '2023-01-01 11:04:42.628720', '2', 'pietrek', 2, '[{\"changed\": {\"fields\": [\"password\"]}}]', 6, 1),
(16, '2023-01-06 15:27:38.935684', '37', '12312442124', 1, '[{\"added\": {}}]', 7, 1),
(17, '2023-01-06 15:29:56.597672', '37', '12312442124', 2, '[{\"changed\": {\"fields\": [\"Zdj\\u0119cie\"]}}]', 7, 1),
(18, '2023-01-06 15:30:13.055383', '38', '13123231', 1, '[{\"added\": {}}]', 7, 1),
(19, '2023-03-26 16:32:01.367210', '2', 'pietrek', 2, '[{\"changed\": {\"fields\": [\"Konto aktywne\"]}}]', 6, 1),
(20, '2023-03-26 16:33:01.643222', '2', 'pietrek', 2, '[{\"changed\": {\"fields\": [\"password\"]}}]', 6, 1),
(21, '2023-03-26 16:36:18.338799', '2', 'pietrek', 2, '[{\"changed\": {\"fields\": [\"password\"]}}]', 6, 1),
(22, '2023-03-26 16:37:46.808980', '2', 'pietrek', 2, '[{\"changed\": {\"fields\": [\"password\"]}}]', 6, 1),
(23, '2023-03-26 16:38:27.476862', '2', 'pietrek', 2, '[{\"changed\": {\"fields\": [\"Konto aktywne\"]}}]', 6, 1),
(24, '2023-03-26 16:45:54.862471', '6', '12345', 2, '[{\"changed\": {\"fields\": [\"password\"]}}]', 6, 1),
(25, '2023-03-26 16:46:27.641988', '6', '12345', 2, '[{\"changed\": {\"fields\": [\"Konto aktywne\"]}}]', 6, 1),
(26, '2023-03-26 17:04:04.062581', '6', '12345', 2, '[{\"changed\": {\"fields\": [\"Konto aktywne\"]}}]', 6, 1),
(27, '2023-03-26 17:05:48.105507', '2', 'pietrek', 2, '[{\"changed\": {\"fields\": [\"Konto aktywne\"]}}]', 6, 1),
(28, '2023-03-26 17:07:27.544007', '5', 'sads', 2, '[{\"changed\": {\"fields\": [\"password\"]}}]', 6, 1),
(29, '2023-03-26 17:07:31.702771', '5', 'sads', 2, '[{\"changed\": {\"fields\": [\"Konto aktywne\"]}}]', 6, 1),
(30, '2023-03-26 17:08:08.950310', '5', 'sads', 2, '[{\"changed\": {\"fields\": [\"Konto aktywne\"]}}]', 6, 1),
(31, '2023-03-27 19:06:10.942438', '11', 'test', 3, '', 6, 1),
(32, '2023-03-27 19:06:10.995486', '12', 'testowy23', 3, '', 6, 1),
(33, '2023-03-27 19:10:42.094864', '10', 'testowy_telefon', 2, '[{\"changed\": {\"fields\": [\"Konto aktywne\"]}}]', 6, 1),
(34, '2023-03-27 19:10:55.759091', '10', 'testowy_telefon', 2, '[{\"changed\": {\"fields\": [\"password\"]}}]', 6, 1);

-- --------------------------------------------------------

--
-- Struktura tabeli dla tabeli `django_content_type`
--

CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Zrzut danych tabeli `django_content_type`
--

INSERT INTO `django_content_type` (`id`, `app_label`, `model`) VALUES
(6, 'accounts', 'account'),
(1, 'admin', 'logentry'),
(3, 'auth', 'group'),
(2, 'auth', 'permission'),
(4, 'contenttypes', 'contenttype'),
(7, 'pets', 'petprofile'),
(5, 'sessions', 'session');

-- --------------------------------------------------------

--
-- Struktura tabeli dla tabeli `django_migrations`
--

CREATE TABLE `django_migrations` (
  `id` bigint(20) NOT NULL,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Zrzut danych tabeli `django_migrations`
--

INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES
(1, 'contenttypes', '0001_initial', '2022-12-03 16:01:26.262090'),
(2, 'contenttypes', '0002_remove_content_type_name', '2022-12-03 16:01:26.694987'),
(3, 'auth', '0001_initial', '2022-12-03 16:01:29.291890'),
(4, 'auth', '0002_alter_permission_name_max_length', '2022-12-03 16:01:29.901948'),
(5, 'auth', '0003_alter_user_email_max_length', '2022-12-03 16:01:29.929973'),
(6, 'auth', '0004_alter_user_username_opts', '2022-12-03 16:01:29.954996'),
(7, 'auth', '0005_alter_user_last_login_null', '2022-12-03 16:01:29.980019'),
(8, 'auth', '0006_require_contenttypes_0002', '2022-12-03 16:01:30.077107'),
(9, 'auth', '0007_alter_validators_add_error_messages', '2022-12-03 16:01:30.105133'),
(10, 'auth', '0008_alter_user_username_max_length', '2022-12-03 16:01:30.130155'),
(11, 'auth', '0009_alter_user_last_name_max_length', '2022-12-03 16:01:30.155178'),
(12, 'auth', '0010_alter_group_name_max_length', '2022-12-03 16:01:30.220237'),
(13, 'auth', '0011_update_proxy_permissions', '2022-12-03 16:01:30.247262'),
(14, 'auth', '0012_alter_user_first_name_max_length', '2022-12-03 16:01:30.271284'),
(15, 'accounts', '0001_initial', '2022-12-03 16:01:57.674555'),
(16, 'accounts', '0002_alter_account_is_active_alter_account_is_staff_and_more', '2022-12-03 16:01:58.561381'),
(17, 'accounts', '0003_alter_account_is_superuser', '2022-12-03 16:01:58.586404'),
(18, 'admin', '0001_initial', '2022-12-03 16:01:59.874582'),
(19, 'admin', '0002_logentry_remove_auto_add', '2022-12-03 16:01:59.962662'),
(20, 'admin', '0003_logentry_add_action_flag_choices', '2022-12-03 16:01:59.987685'),
(21, 'pets', '0001_initial', '2022-12-03 16:02:01.183779'),
(22, 'sessions', '0001_initial', '2022-12-03 16:02:01.517082'),
(23, 'accounts', '0004_account_region', '2022-12-10 15:18:46.991291'),
(24, 'accounts', '0005_alter_account_region', '2022-12-10 16:11:41.973751'),
(25, 'accounts', '0006_alter_account_region', '2022-12-10 18:21:03.471455'),
(26, 'pets', '0002_petprofile_pet_sex_petprofile_pet_type', '2022-12-10 18:21:03.745704'),
(27, 'pets', '0003_alter_petprofile_pet_sex', '2022-12-10 18:27:40.962887'),
(28, 'pets', '0004_alter_petprofile_pet_sex', '2022-12-10 18:28:24.916247'),
(29, 'pets', '0005_alter_petprofile_pet_sex_alter_petprofile_pet_type', '2022-12-11 13:42:44.836688'),
(30, 'accounts', '0007_alter_account_region', '2022-12-11 15:03:35.597138'),
(31, 'pets', '0006_petprofile_region', '2022-12-11 15:03:35.871387'),
(32, 'pets', '0007_rename_pet_num_petprofile_chip_number_and_more', '2022-12-15 17:32:29.486170');

-- --------------------------------------------------------

--
-- Struktura tabeli dla tabeli `django_session`
--

CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Zrzut danych tabeli `django_session`
--

INSERT INTO `django_session` (`session_key`, `session_data`, `expire_date`) VALUES
('0gasxuj49h0hr4d5sd3lnyb1h5lyxptu', '.eJxVi0sKwjAQQO-StZSMaT7jUug5wmRmQopawbQr8e4qdKHb93maTNva8tb1kWcxJwPm8MsK8UWXryDm-7asfdhRH6YbzdfzHvxdjXr7LKiiYjklrsWjF_RQoNoxHoUsUgJwGsFFoRCiT1AqMToOYVR0Vsm83lUfM_I:1pAx7k:i49G1WaaaqbfTi8c0o-pJ0WsDMyocnqqvCnPLxOby0U', '2023-01-12 17:55:24.506020'),
('1dgph128kblhitvbxffbhf51aj7fyni2', '.eJxVi0kKwjAUhu-StZQMZnIp9BzhT94LKWoF06zEu6vQhW6_4SkSxtbS6PxIC4mT0OLwyzLKhdevQCn3sW592lGf5huW63kP_q6G3j6LyjbqyJUyKa2CAtsqja3HICPBQ0eNgGwcO0ZWHoZAkoFKwXmrxesNV2A0mQ:1pDlU3:8ViDv0kUCEoNeN87zHaTm-mVopDcTi-p8f_O2RDWJVI', '2023-01-20 12:06:03.226860'),
('1lau18hu4wo7yoq9l7ak327ctpdfvc7p', '.eJxVi0kKwjAUhu-StZQMZnIp9BzhT94LKWoF06zEu6vQhW6_4SkSxtbS6PxIC4mT0OLwyzLKhdevQCn3sW592lGf5huW63kP_q6G3j6LyjbqyJUyKa2CAtsqja3HICPBQ0eNgGwcO0ZWHoZAkoFKwXmrxesNV2A0mQ:1pGfP9:pQqP6OMjHUZsNnemYtYJB4xDf9Mc0fkfW-HTmgE2Ii8', '2023-01-28 12:12:59.846553'),
('1mfokw6cfpn7vurah878gm4t9p3z2pl5', '.eJxVi0sKwjAQQO-StZSMaT7jUug5wmRmQopawbQr8e4qdKHb93maTNva8tb1kWcxJwPm8MsK8UWXryDm-7asfdhRH6YbzdfzHvxdjXr7LKiiYjklrsWjF_RQoNoxHoUsUgJwGsFFoRCiT1AqMToOYVR0Vsm83lUfM_I:1p6Smt:JukXpif9_IbtbZHBBt8PnFlf9IfF4dRcroJTRD8sAFU', '2022-12-31 08:43:19.003959'),
('4chyz8e7isajsvi4qbf6ulvlmnbxfcgi', '.eJxVi0sKwjAQQO-StZSMaT7jUug5wmRmQopawbQr8e4qdKHb93maTNva8tb1kWcxJwPm8MsK8UWXryDm-7asfdhRH6YbzdfzHvxdjXr7LKiiYjklrsWjF_RQoNoxHoUsUgJwGsFFoRCiT1AqMToOYVR0Vsm83lUfM_I:1pBw8w:q7RdK3hUQG791wlaNmoOAzkpwMBGLX_4-_wy7bdzxjw', '2023-01-15 11:04:42.703788'),
('5kl8ckmjhzclqacc5685anb7sqd0z7lq', '.eJxVi80OwiAMgN-Fs1mwRQYeTXwOUloaFnUmMk7Gd3dLdtDr9_M2ifpSU2_llSYxZwPm8Msy8a3MmyDmZ5-XNuyoDdcHTffLHvxdlVpdl-hCAUIYUY7AJw0I5BkpROtthCIKQGIhZw0KHtWJ8xqYRmuRJJrPFzRgM7A:1p855T:wIm2B_yK7D6w_KILlaOVXun1krDC1-UfTHaJWBv5GR4', '2023-01-04 19:49:11.093818'),
('9ir8eqpv8nkfsbfulm6yhuu5xxz804qh', '.eJxVi80OwiAMgN-Fs1mAUSgeTXwOUto1LOpMZDsZ311NdtDr9_M0hba1la1PjzKLORo0h19WiS_T8hXEfN-WtQ876sP5RvP1tAd_V6PePotXjhKtU6CkgJZdGj0rZAKhwIwBtVbnRxRJOYj1gpCUIqhwzNW83lV5NF0:1pEFvP:MmiRfJz_42YS7dnLHZfyr7eMQ5mFt-BdtYVv8fTzzdc', '2023-01-21 20:36:19.135270'),
('cj7nqg78jbsykkhf5tpmydp59ivnwt4s', '.eJxVi80OwiAMgN-Fs1lYGYV6NPE5SBltWNSZyDgZ311NdtDr9_M0iftWU2_ySEsxR-PN4Zdlni-yfgXP872vWxt21IbzjZfraQ_-rsqtfhYbGMRqVpRYGKIL4pmBCK0nlYyADifIJNEiBTcqIjNpmSKMota83kjIM6A:1pgTqs:8smjlHr96XmQf2fiX57izZcEkGdhyo5Dr_cOpSg-crM', '2023-04-09 17:08:18.025365'),
('dxoq9c7q6v8ip8ixcui4xvhehqnx2k9a', '.eJxVi0sKwjAQQO-StZSMaT7jUug5wmRmQopawbQr8e4qdKHb93maTNva8tb1kWcxJwPm8MsK8UWXryDm-7asfdhRH6YbzdfzHvxdjXr7LKiiYjklrsWjF_RQoNoxHoUsUgJwGsFFoRCiT1AqMToOYVR0Vsm83lUfM_I:1pOHUY:OlU1gB5TxHqUdF_yBbHvSnKOdRp0vBFI5lDqCDuRMk0', '2023-02-18 12:18:02.332031'),
('dykn6l18cyqq97l09wvblyunuo40cw4t', '.eJxVizEOwjAMRe-SGVWJW6cJI1LPEdmuo1RAkUgzIe5OkTrA8Jf333uZRG0rqVV9pmU2Z-OsOf1CJrnq-n1I5NHWrXYHqt10p-V2OYS_qlAtexLJCwjkHmFEHCznkUIGF23w2A_Kqi4EjBxBJRMyB5Z-zmD3AXvz_gBeUDRM:1pHV6b:hxku3DYPQ6ZnGPFx7nIBfLJFkXQREkszUWY14GjLwsI', '2023-01-30 19:25:17.486483'),
('eefciwz5aq1boyjdnk4twiu07a0euclz', '.eJxVi0sKwjAQQO-StZSMaT7jUug5wmRmQopawbQr8e4qdKHb93maTNva8tb1kWcxJwPm8MsK8UWXryDm-7asfdhRH6YbzdfzHvxdjXr7LKiiYjklrsWjF_RQoNoxHoUsUgJwGsFFoRCiT1AqMToOYVR0Vsm83lUfM_I:1pGe8q:-oQPgLML-Sd3GGB-n1S3_rq7jQ5jj2mRMVHRx10jTxM', '2023-01-28 10:52:04.159601'),
('eowouu4kb52fg3qna87j7kte2rsk84u7', '.eJxVi80OwiAMgN-Fs1mwRQYeTXwOUloaFnUmMk7Gd3dLdtDr9_M2ifpSU2_llSYxZwPm8Msy8a3MmyDmZ5-XNuyoDdcHTffLHvxdlVpdl-hCAUIYUY7AJw0I5BkpROtthCIKQGIhZw0KHtWJ8xqYRmuRJJrPFzRgM7A:1p85rE:2Ckxm_7L-KBTUwCXgllYHDVjL1TJvAGjCox7UZIySVs', '2023-01-04 20:38:32.275325'),
('gyqtk73v8n58vgl6rbypyrb2npvyjotz', '.eJxVi0kKwjAUhu-StZQMZnIp9BzhT94LKWoF06zEu6vQhW6_4SkSxtbS6PxIC4mT0OLwyzLKhdevQCn3sW592lGf5huW63kP_q6G3j6LyjbqyJUyKa2CAtsqja3HICPBQ0eNgGwcO0ZWHoZAkoFKwXmrxesNV2A0mQ:1pCQCC:RWLVRhNT04RIg5zZzCqvlExcQaJ3XjzLOL6PEMpup_Y', '2023-01-16 19:10:04.804344'),
('i7rfqe9z4tpzoh3mh4j0d9x8pml16sjl', '.eJxVi80OwiAMgN-Fs1mwRQYeTXwOUloaFnUmMk7Gd3dLdtDr9_M2ifpSU2_llSYxZwPm8Msy8a3MmyDmZ5-XNuyoDdcHTffLHvxdlVpdl-hCAUIYUY7AJw0I5BkpROtthCIKQGIhZw0KHtWJ8xqYRmuRJJrPFzRgM7A:1pAcBO:qeufU0zFiIN9_2uPmHTc4f_5BT_GmPqpJmOi6c0XdLA', '2023-01-11 19:33:46.819185'),
('iep618yjoin72voue0aa0olqe42fox7b', '.eJxVi0kKwjAUhu-StZQMZnIp9BzhT94LKWoF06zEu6vQhW6_4SkSxtbS6PxIC4mT0OLwyzLKhdevQCn3sW592lGf5huW63kP_q6G3j6LyjbqyJUyKa2CAtsqja3HICPBQ0eNgGwcO0ZWHoZAkoFKwXmrxesNV2A0mQ:1pC28p:p94Vo1kADadX-gX0rkaw-ztjxOUcaJrsLd6J7Xe_9WA', '2023-01-15 17:28:59.391137'),
('m1ow6q4p3zx8ni1dss32iy70hxjz25ob', '.eJxVi0kKwjAUhu-StZQMZnIp9BzhT94LKWoF06zEu6vQhW6_4SkSxtbS6PxIC4mT0OLwyzLKhdevQCn3sW592lGf5huW63kP_q6G3j6LyjbqyJUyKa2CAtsqja3HICPBQ0eNgGwcO0ZWHoZAkoFKwXmrxesNV2A0mQ:1pBw9T:1tLkxK9P7lCW-053sznW1uKU9EKHRSltwaSRQ6htWDE', '2023-01-15 11:05:15.176714'),
('mma7h4mujw5mmpbngieqrnj20fv7wah8', '.eJxVi80OwiAMgN-Fs1mwRQYeTXwOUloaFnUmMk7Gd3dLdtDr9_M2ifpSU2_llSYxZwPm8Msy8a3MmyDmZ5-XNuyoDdcHTffLHvxdlVpdl-hCAUIYUY7AJw0I5BkpROtthCIKQGIhZw0KHtWJ8xqYRmuRJJrPFzRgM7A:1p1rY6:z6zVfFjq2YxMmGyprzkukNhEW6VW4dz0uTJQgyzyQCY', '2022-12-18 16:09:02.699884'),
('om4kq3qd42on20o6m5fburf28i4vz7ml', '.eJxVi0kKwjAUhu-StZQMZnIp9BzhT94LKWoF06zEu6vQhW6_4SkSxtbS6PxIC4mT0OLwyzLKhdevQCn3sW592lGf5huW63kP_q6G3j6LyjbqyJUyKa2CAtsqja3HICPBQ0eNgGwcO0ZWHoZAkoFKwXmrxesNV2A0mQ:1pC2FK:V1VHu5V5I-RQiyhgotFk3V6ePfSjBZvRYMColb1yuto', '2023-01-15 17:35:42.519366'),
('sq2em5b6z9n95wxrmr9eyhcdjcl4rtu3', '.eJxVi0kKwjAUhu-StZQMZnIp9BzhT94LKWoF06zEu6vQhW6_4SkSxtbS6PxIC4mT0OLwyzLKhdevQCn3sW592lGf5huW63kP_q6G3j6LyjbqyJUyKa2CAtsqja3HICPBQ0eNgGwcO0ZWHoZAkoFKwXmrxesNV2A0mQ:1pDt7a:W5hNZVHqdWB81BQ4B2tfhMz-IOZ6Fmxz-Fg1jCbkEDw', '2023-01-20 20:15:22.466147'),
('yggqeg67rzpbjsysauqvivfuvofmtgzb', '.eJxVi0sKwjAQQO-StZSMaT7jUug5wmRmQopawbQr8e4qdKHb93maTNva8tb1kWcxJwPm8MsK8UWXryDm-7asfdhRH6YbzdfzHvxdjXr7LKiiYjklrsWjF_RQoNoxHoUsUgJwGsFFoRCiT1AqMToOYVR0Vsm83lUfM_I:1pVFCe:WV0FavAidXzeA2GKdwRvNQro0wZ9Nlo21iWmDx6-mCU', '2023-03-09 17:16:20.597744'),
('zkbuz4t0ct8rmh4xphni6wpwtrkuay4w', '.eJxVi0kKwjAUhu-StZQMZnIp9BzhT94LKWoF06zEu6vQhW6_4SkSxtbS6PxIC4mT0OLwyzLKhdevQCn3sW592lGf5huW63kP_q6G3j6LyjbqyJUyKa2CAtsqja3HICPBQ0eNgGwcO0ZWHoZAkoFKwXmrxesNV2A0mQ:1pCSNx:1uQQsq79ge-yRjXPpC4wNnTqjV5-R5TtmocOgTwxAwU', '2023-01-16 21:30:21.624760');

-- --------------------------------------------------------

--
-- Struktura tabeli dla tabeli `pets_petprofile`
--

CREATE TABLE `pets_petprofile` (
  `id` bigint(20) NOT NULL,
  `chip_number` varchar(15) NOT NULL,
  `pet_name` varchar(30) NOT NULL,
  `desc` longtext NOT NULL,
  `image` varchar(255) DEFAULT NULL,
  `is_lost` tinyint(1) NOT NULL,
  `add_date` date NOT NULL,
  `owner_id` bigint(20) NOT NULL,
  `gender` varchar(13) NOT NULL,
  `pet_type` varchar(6) NOT NULL,
  `region` varchar(19) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Zrzut danych tabeli `pets_petprofile`
--

INSERT INTO `pets_petprofile` (`id`, `chip_number`, `pet_name`, `desc`, `image`, `is_lost`, `add_date`, `owner_id`, `gender`, `pet_type`, `region`) VALUES
(20, '123123', 'Sunny', 'asdasdasdadsasd', 'profile_images/admin/123123/profile_pic.png', 1, '2022-12-11', 1, 'Samiec', 'Pies', 'Warmińsko-mazurskie'),
(24, '38338833', 'Hugguug', 'Gygugg', 'profile_images/pietrek/38338833/profile_pic.png', 1, '2022-12-17', 2, 'Samiec', 'Gryzoń', 'Dolnośląskie'),
(25, '0000012341', 'Pepsi', 'Spaniały piesu <b>TEST</b>', 'profile_images/admin/21322131231/profile_pic_48UoQER.png', 0, '2022-12-18', 1, 'Samica', 'Pies', 'Dolnośląskie'),
(27, '6231919', 'Hsjsejakksieieiskskwkwkkwwllwk', 'Hsjsjs', 'profile_images/pietrek/6231919/profile_pic.png', 1, '2022-12-21', 2, 'Samiec', 'Gryzoń', 'Dolnośląskie'),
(28, '2131233', 'Sunny as', 'asdasdadse', 'profile_images/admin/2131233/profile_pic_3yH3SJY.png', 1, '2022-12-21', 1, 'Samiec', 'Gryzoń', 'Dolnośląskie'),
(30, '123213', '123231', 'asdasd', 'profile_images/pietrek/123213/profile_pic.png', 1, '2022-12-21', 2, 'Samiec', 'Pies', 'Zachodnio-pomorskie'),
(31, '12323', 'asddas', 'asdasdasdadsdsads', 'profile_images/pietrek/12323/profile_pic.png', 1, '2022-12-21', 2, 'Samiec', 'Gryzoń', 'Świętokrzyskie'),
(32, '92626', 'Zbhshe', 'Hddid', 'profile_images/pietrek/92626/profile_pic.png', 1, '2022-12-21', 2, 'Samiec', 'Gryzoń', 'Dolnośląskie'),
(36, '21323142414', 'daadsa', 'dasdsasds', 'profile_images/sads/21323142414/profile_pic.png', 0, '2022-12-28', 5, 'Samiec', 'Gryzoń', 'Inna lokalizacja'),
(38, '13123231', 'Sunny', 'aadsdsads', 'profile_images/admin/13123231/profile_pic_eTyBSGi.png', 0, '2023-01-06', 1, 'Samiec', 'Pies', 'Opolskie'),
(39, '3213123', '213123', '2132123', 'profile_images/def_profile_pic.png', 0, '2023-01-06', 1, 'Samiec', 'Gryzoń', 'Inna lokalizacja'),
(40, '213214', '42124412', '12442124', 'profile_images/def_profile_pic.png', 0, '2023-01-06', 1, 'Samiec', 'Gryzoń', 'Dolnośląskie'),
(41, '1324', '421214', 'aasdasdasdadsasdasdasdasdasdasdasdasd', 'profile_images/def_profile_pic.png', 1, '2023-01-06', 1, 'Samiec', 'Gryzoń', 'Dolnośląskie'),
(42, '12421422145', 'asddasas', 'adsadsadsads', 'profile_images/def_profile_pic.png', 1, '2023-01-07', 8, 'Samiec', 'Gad', 'Inna lokalizacja'),
(43, '213214421', 'Sunny as', 'test', 'profile_images/admin/213214421/profile_pic.png', 0, '2023-01-14', 1, 'Samiec', 'Gryzoń', 'Dolnośląskie'),
(44, '123214', '2123', 'asasdasasd', 'profile_images/def_profile_pic.png', 1, '2023-01-14', 1, 'Samiec', 'Gryzoń', 'Dolnośląskie'),
(46, '12345678901', 'Lula', 'Super Piesek', 'profile_images/testowy_user/12345678901/profile_pic.png', 0, '2023-01-16', 9, 'Samica', 'Pies', 'Wielkopolskie'),
(48, '123421312', 'qwewee', 'asdadadsasdad', 'profile_images/testowy_telefon/123421312/profile_pic.png', 1, '2023-01-16', 10, 'Samiec', 'Gryzoń', 'Inna lokalizacja');

--
-- Indeksy dla zrzutów tabel
--

--
-- Indeksy dla tabeli `accounts_account`
--
ALTER TABLE `accounts_account`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `username` (`username`),
  ADD UNIQUE KEY `email` (`email`);

--
-- Indeksy dla tabeli `accounts_account_groups`
--
ALTER TABLE `accounts_account_groups`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `accounts_account_groups_account_id_group_id_f64165b0_uniq` (`account_id`,`group_id`),
  ADD KEY `accounts_account_groups_group_id_7c6a6bd1_fk_auth_group_id` (`group_id`);

--
-- Indeksy dla tabeli `accounts_account_user_permissions`
--
ALTER TABLE `accounts_account_user_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `accounts_account_user_pe_account_id_permission_id_9af93c14_uniq` (`account_id`,`permission_id`),
  ADD KEY `accounts_account_use_permission_id_24620205_fk_auth_perm` (`permission_id`);

--
-- Indeksy dla tabeli `auth_group`
--
ALTER TABLE `auth_group`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `name` (`name`);

--
-- Indeksy dla tabeli `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  ADD KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`);

--
-- Indeksy dla tabeli `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`);

--
-- Indeksy dla tabeli `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD PRIMARY KEY (`id`),
  ADD KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  ADD KEY `django_admin_log_user_id_c564eba6_fk_accounts_account_id` (`user_id`);

--
-- Indeksy dla tabeli `django_content_type`
--
ALTER TABLE `django_content_type`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`);

--
-- Indeksy dla tabeli `django_migrations`
--
ALTER TABLE `django_migrations`
  ADD PRIMARY KEY (`id`);

--
-- Indeksy dla tabeli `django_session`
--
ALTER TABLE `django_session`
  ADD PRIMARY KEY (`session_key`),
  ADD KEY `django_session_expire_date_a5c62663` (`expire_date`);

--
-- Indeksy dla tabeli `pets_petprofile`
--
ALTER TABLE `pets_petprofile`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `pet_num` (`chip_number`),
  ADD KEY `pets_petprofile_owner_id_5390dc81_fk_accounts_account_id` (`owner_id`);

--
-- AUTO_INCREMENT dla zrzuconych tabel
--

--
-- AUTO_INCREMENT dla tabeli `accounts_account`
--
ALTER TABLE `accounts_account`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=14;

--
-- AUTO_INCREMENT dla tabeli `accounts_account_groups`
--
ALTER TABLE `accounts_account_groups`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT dla tabeli `accounts_account_user_permissions`
--
ALTER TABLE `accounts_account_user_permissions`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=13;

--
-- AUTO_INCREMENT dla tabeli `auth_group`
--
ALTER TABLE `auth_group`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT dla tabeli `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT dla tabeli `auth_permission`
--
ALTER TABLE `auth_permission`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=29;

--
-- AUTO_INCREMENT dla tabeli `django_admin_log`
--
ALTER TABLE `django_admin_log`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=35;

--
-- AUTO_INCREMENT dla tabeli `django_content_type`
--
ALTER TABLE `django_content_type`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;

--
-- AUTO_INCREMENT dla tabeli `django_migrations`
--
ALTER TABLE `django_migrations`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=33;

--
-- AUTO_INCREMENT dla tabeli `pets_petprofile`
--
ALTER TABLE `pets_petprofile`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=52;

--
-- Ograniczenia dla zrzutów tabel
--

--
-- Ograniczenia dla tabeli `accounts_account_groups`
--
ALTER TABLE `accounts_account_groups`
  ADD CONSTRAINT `accounts_account_gro_account_id_52f14852_fk_accounts_` FOREIGN KEY (`account_id`) REFERENCES `accounts_account` (`id`),
  ADD CONSTRAINT `accounts_account_groups_group_id_7c6a6bd1_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`);

--
-- Ograniczenia dla tabeli `accounts_account_user_permissions`
--
ALTER TABLE `accounts_account_user_permissions`
  ADD CONSTRAINT `accounts_account_use_account_id_816f9bde_fk_accounts_` FOREIGN KEY (`account_id`) REFERENCES `accounts_account` (`id`),
  ADD CONSTRAINT `accounts_account_use_permission_id_24620205_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`);

--
-- Ograniczenia dla tabeli `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`);

--
-- Ograniczenia dla tabeli `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`);

--
-- Ograniczenia dla tabeli `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  ADD CONSTRAINT `django_admin_log_user_id_c564eba6_fk_accounts_account_id` FOREIGN KEY (`user_id`) REFERENCES `accounts_account` (`id`);

--
-- Ograniczenia dla tabeli `pets_petprofile`
--
ALTER TABLE `pets_petprofile`
  ADD CONSTRAINT `pets_petprofile_owner_id_5390dc81_fk_accounts_account_id` FOREIGN KEY (`owner_id`) REFERENCES `accounts_account` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
