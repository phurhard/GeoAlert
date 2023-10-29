CREATE TABLE `locations` (
  `id` varchar(128) NOT NULL,
  `user_name` varchar(128) DEFAULT NULL,
  `name` varchar(128) DEFAULT NULL,
  `address` varchar(128) DEFAULT NULL,
  `latitude` varchar(28) NOT NULL,
  `longitude` varchar(28) NOT NULL,
  `created_at` datetime DEFAULT NULL,
  `updated_at` datetime DEFAULT NULL,
  PRIMARY KEY (`id`),
--   KEY `user_name` (`user_name`),
--   CONSTRAINT `locations_ibfk_1` FOREIGN KEY (`user_name`) REFERENCES `users` (`username`)
)

CREATE TABLE `locationReminder` (
  `id` varchar(128) NOT NULL,
  `user_name` varchar(128) DEFAULT NULL,
  `location_id` varchar(128) DEFAULT NULL,
  `todo_id` varchar(128) DEFAULT NULL,
  `accuracy` int DEFAULT NULL,
  `activated` tinyint(1) DEFAULT NULL,
  `created_at` datetime DEFAULT NULL,
  `updated_at` datetime DEFAULT NULL,
  PRIMARY KEY (`id`),
--   KEY `user_name` (`user_name`),
--   KEY `location_id` (`location_id`),
--   KEY `todo_id` (`todo_id`),
--   CONSTRAINT `locationReminder_ibfk_1` FOREIGN KEY (`user_name`) REFERENCES `users` (`username`),
--   CONSTRAINT `locationReminder_ibfk_2` FOREIGN KEY (`location_id`) REFERENCES `locations` (`id`) ON UPDATE CASCADE,
--   CONSTRAINT `locationReminder_ibfk_3` FOREIGN KEY (`todo_id`) REFERENCES `todos` (`id`) ON UPDATE CASCADE
)

CREATE TABLE `todos` (
  `id` varchar(255) NOT NULL,
  `user_name` varchar(128) DEFAULT NULL,
  `title` varchar(255) DEFAULT NULL,
  `description` varchar(255) DEFAULT NULL,
  `due_date` datetime DEFAULT NULL,
  `completed` tinyint(1) DEFAULT NULL,
  `created_at` datetime DEFAULT NULL,
  `updated_at` datetime DEFAULT NULL,
  PRIMARY KEY (`id`),
--   KEY `user_name` (`user_name`),
--   CONSTRAINT `todos_ibfk_1` FOREIGN KEY (`user_name`) REFERENCES `users` (`username`)
)

CREATE TABLE `users` (
  `username` varchar(128) NOT NULL,
  `firstname` varchar(128) NOT NULL,
  `lastname` varchar(128) DEFAULT NULL,
  `email` varchar(128) NOT NULL,
  `password` varchar(128) NOT NULL,
  `created_at` datetime DEFAULT NULL,
  `updated_at` datetime DEFAULT NULL,
  `id` varchar(255) NOT NULL,
  PRIMARY KEY (`username`,`id`)
)