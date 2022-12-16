CREATE TABLE users (
  user_id varchar(36) primary key NOT NULL,
  name varchar(128) NOT NULL,
  created_at timestamptz NOT NULL,
  updated_at timestamptz NOT NULL
);
