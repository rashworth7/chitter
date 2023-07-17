DROP TABLE IF EXISTS tags cascade;
DROP SEQUENCE IF EXISTS tags_seq;
DROP TABLE IF EXISTS peeps cascade;
DROP SEQUENCE IF EXISTS peeps_seq;
DROP TABLE IF EXISTS users cascade;
DROP SEQUENCE IF EXISTS users_seq;

CREATE SEQUENCE users_seq;
CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    name text,
    username text,
    password text,
    email text
);

INSERT INTO users (name, username, password, email)
VALUES
('Rich', 'rich9', 'richpass', 'rich@email'),
('Mollie', 'mollie00', 'molliepass', 'mollie@email'),
('Harry', 'harry77', 'harrypass', 'harry@email'),
('Chelsea', 'chelsea14', 'chelseapass', 'chelsea@email')
;

CREATE SEQUENCE peeps_seq;
CREATE TABLE peeps (
    id SERIAL PRIMARY KEY,
    message text,
    timestamp text,
    user_id int,
    tags text,
    FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE cascade
);

INSERT INTO peeps (message, timestamp, user_id, tags)
VALUES
('Message 1', '2023-07-14 12:12:12', 1, 'mollie00, harry77'),
('Message 2', '2023-06-14 12:12:12', 2, 'rich9, chelsea14'),
('Message 3', '2023-05-14 12:12:12', 3, 'mollie00, rich9')
;


CREATE SEQUENCE tags_seq;
CREATE TABLE tags (
    user_id int,
    peep_id int,
    PRIMARY KEY (user_id, peep_id),
    FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE cascade,
    FOREIGN KEY (peep_id) REFERENCES peeps(id) ON DELETE cascade
);

INSERT INTO tags(user_id, peep_id) VALUES
(1, 2),
(1, 3),
(2, 1),
(2, 3),
(3, 1),
(4, 2);
