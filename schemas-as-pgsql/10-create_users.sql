CREATE TABLE users (
  user_id varchar(36) primary key NOT NULL,
  name varchar(128) NOT NULL,
  created_at SPANNER.COMMIT_TIMESTAMP NOT NULL,
  updated_at SPANNER.COMMIT_TIMESTAMP NOT NULL
);
