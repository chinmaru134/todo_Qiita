USE flask_db;

-- todoリスト
CREATE TABLE todo_list (
    todo_id INT AUTO_INCREMENT PRIMARY KEY,
    title varchar(500) NOT NULL,
    insert_time timestamp NOT NULL default CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);