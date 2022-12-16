CREATE TABLE user_items (
  user_id varchar(36) NOT NULL,
  item_id varchar(36) NOT NULL,
  created_at timestamptz NOT NULL,
  updated_at timestamptz NOT NULL,
  primary key (user_id, item_id)
) INTERLEAVE IN PARENT users ON DELETE CASCADE;
