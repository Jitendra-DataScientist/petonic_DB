select * from user_login;

select * from validation;

ALTER TABLE validation
ADD COLUMN active BOOLEAN;

UPDATE validation
SET active = true
WHERE email='johndoe@example.com';

select * from user_signup;

select * from validation;

