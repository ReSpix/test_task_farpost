CREATE TABLE IF NOT EXISTS logs (
    id INTEGER PRIMARY KEY,
    datetime TEXT NOT NULL,
    user_id INTEGER NOT NULL,
    post_id INTEGER,
    space_type_id INTEGER NOT NULL,
    event_type_id INTEGER NOT NULL,
    FOREIGN KEY (space_type_id) REFERENCES space_type (id),
    FOREIGN KEY (event_type_id) REFERENCES event_type_id (id)
);

CREATE TABLE IF NOT EXISTS space_type (id INTEGER PRIMARY KEY, name TEXT NOT NULL);

DELETE FROM
    space_type;

INSERT INTO
    space_type (id, name)
VALUES
    (1, 'global'),
    (2, 'blog'),
    (3, 'post');

CREATE TABLE IF NOT EXISTS event_type (id INTEGER PRIMARY KEY, name TEXT NOT NULL);

DELETE FROM
    event_type;

INSERT INTO
    event_type (id, name)
VALUES
    (1, 'login'),
    (2, 'comment'),
    (3, 'create_post'),
    (4, 'delete_post'),
    (5, 'logout');