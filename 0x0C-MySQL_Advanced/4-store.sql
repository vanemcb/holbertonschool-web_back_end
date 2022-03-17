--  script that creates a trigger that decreases the quantity of an item after
-- adding a new order.

CREATE TRIGGER my_trigger
AFTER INSERT
ON orders FOR EACH ROW
UPDATE items SET quantity = quantity - 1;
