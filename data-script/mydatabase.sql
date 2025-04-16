CREATE DATABASE IF NOT EXISTS mydatabase;
USE mydatabase;

CREATE TABLE IF NOT EXISTS quotes (
    id INT AUTO_INCREMENT PRIMARY KEY,
    quote TEXT NOT NULL
);

INSERT INTO quotes (quote) VALUES
("Life is what happens when you're busy making other plans. -- John Lennon"),
("The purpose of our lives is to be happy. -- Dalai Lama"),
("Get busy living or get busy dying. -- Stephen King");

