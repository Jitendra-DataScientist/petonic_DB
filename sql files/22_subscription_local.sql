select us.email,us.role,ul.password from user_signup us join user_login ul on us.email=ul.email;

select * from subscription;
delete from subscription where plan='basic';
-- INSERT INTO subscription (subscription_id, plan, users_count, company_name, phone,
-- 						  f_name, l_name, email, country, address_line1, address_line2)
-- VALUES ('l9KXbn0U1e_automail1.petonic@gmail.com', 'Basic Plan', 100, 'Petonic', '123-456-7890',
-- 		'John', 'Doe', 'automail1.petonic@gmail.com', 'USA', '123 Main St', 'Apt 101');
select * from user_signup where role='admin';
delete from user_signup where email='automail2.petonic@gmail.com';
delete from user_login where email='automail2.petonic@gmail.com';

INSERT INTO subscription (
  subscription_id, 
  plan, 
  users_count, 
  company_name, 
  phone, 
  f_name, 
  l_name, 
  email, 
  country, 
  address_line1, 
  address_line2, 
  payment_mode, 
  amount, 
  payment_status, 
  otp
) VALUES (
  'RfxC5qfaff_automail.petonic@gmail.com', 
  'Basic Plan', 
  100, 
  'Petonic', 
  '+1234567890', 
  'John', 
  'Doe', 
  'automail.petonic@gmail.com', 
  'United States', 
  '123 Main St', 
  'Apt 101', 
  'Credit Card', 
  '99.99', 
  true, 
  '1234567890'
);

		
DROP TABLE IF EXISTS subscription;

CREATE TABLE subscription (
  subscription_id VARCHAR(100) PRIMARY KEY,
  plan VARCHAR(40),
  users_count SMALLINT,
  company_name VARCHAR(100),
  phone VARCHAR(20),
  f_name VARCHAR(50),
  l_name VARCHAR(50),
  email VARCHAR(100),
  country VARCHAR(100),
  address_line1 VARCHAR(200),
  address_line2 VARCHAR(200),
  payment_mode VARCHAR(50),
  amount VARCHAR(50),
  payment_status BOOLEAN,
  otp VARCHAR(10)
);


ALTER TABLE user_login
ADD subscription_id VARCHAR(100);

select us.email,us.role,ul.password from user_signup us join user_login ul on us.email=ul.email where us.role='admin';
select * from subscription;
select count(*) from subscription where email = 'automail2.petonic@gmail.com1';
UPDATE user_login
SET subscription_id = 'RfxC5qfaff_automail.petonic@gmail.com';

select us.email,us.role,ul.password,ul.subscription_id from user_signup us join user_login ul on us.email=ul.email;

delete from user_login where email='automail2.petonic@gmail.com';
delete from user_signup where email='automail2.petonic@gmail.com';


ALTER TABLE subscription
DROP COLUMN payment_mode,
DROP COLUMN amount,
DROP COLUMN payment_status;

ALTER TABLE subscription
ADD COLUMN payment_mode JSON,
ADD COLUMN amount JSON,
ADD COLUMN payment_status JSON;

ALTER TABLE user_login
ADD COLUMN first_time BOOLEAN;

UPDATE user_login
SET first_time = TRUE;

select * from user_login;

select first_time from user_login where email = 'johndoe@example.com';

select first_time from user_login where email = 'johndoe@example.com1';

update user_login
set first_time = false
where email = 'johndoe@example.com';