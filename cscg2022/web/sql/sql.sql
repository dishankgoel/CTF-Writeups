CREATE TABLE fileupload_users(
  id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
  username VARCHAR(30) NOT NULL,
  password VARCHAR(256) NOT NULL,
  staff BIT(1)
);
INSERT INTO fileupload_users (username, password, staff) VALUES ('administrator', 'thisisadummyvalue', 1);
