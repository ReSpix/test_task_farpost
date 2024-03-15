CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY,
    email TEXT NOT NULL,
    login TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS blog (
    id INTEGER PRIMARY KEY,
    owner_id INTEGER NOT NULL,
    name TEXT NOT NULL,
    description TEXT,
    FOREIGN KEY (owner_id) REFERENCES users (id)
);

CREATE TABLE IF NOT EXISTS post (
    id INTEGER PRIMARY KEY,
    header TEXT NOT NULL,
    text TEXT,
    author_id INTEGER NOT NULL,
    blog_id INTEGER NOT NULL,
    FOREIGN KEY (author_id) REFERENCES users (id),
    FOREIGN KEY (blog_id) REFERENCES blog (id)
);