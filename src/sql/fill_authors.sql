DELETE FROM
    users;

INSERT INTO
    users (id, email, login)
VALUES
    (1, "user1@email.com", "user1"),
    (2, "user2@outlook.com", "user2");

DELETE FROM
    blog;

INSERT INTO
    blog (id, owner_id, name, description)
VALUES
    (1, 1, 'blog1', 'description1'),
    (2, 1, 'blog2', 'description2'),
    (3, 2, 'blog3', 'description3');

DELETE FROM
    post;

INSERT INTO
    post (id, header, text, author_id, blog_id)
VALUES
    (1, 'header1', 'text1', 1, 1),
    (2, 'header2', 'text2', 1, 1),
    (3, 'header3', 'text3', 1, 1),
    (4, 'header4', 'text4', 1, 2),
    (5, 'header5', 'text5', 2, 3);