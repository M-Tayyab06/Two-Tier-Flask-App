CREATE DATABASE customdb;

USE customdb;

CREATE TABLE prompts (
    id INT AUTO_INCREMENT PRIMARY KEY,
    prompt TEXT NOT NULL
);

INSERT INTO prompts (prompt) VALUES ('Welcome to the custom database!');
