
CREATE TABLE items (
  item_id varchar(36) NOT NULL,
  item_name varchar(64) NOT NULL,
  price INT NOT NULL,
  created_at SPANNER.COMMIT_TIMESTAMP NOT NULL,
  updated_at SPANNER.COMMIT_TIMESTAMP NOT NULL,
  primary key(item_id)
) 
