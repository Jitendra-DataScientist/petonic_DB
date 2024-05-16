select * from user_login;

select * from user_signup where role='admin';

delete from 

select * from validation;

select * from subscription;

DELETE FROM subscription 
WHERE subscription_id <> 'RfxC5qfaff_automail.petonic@gmail.com';

DELETE FROM user_login 
WHERE subscription_id <> 'RfxC5qfaff_automail.petonic@gmail.com';

-- Delete from user_signup where email not in user_login
DELETE FROM user_signup
WHERE email NOT IN (SELECT email FROM user_login);

-- Delete from validation where email not in user_login
DELETE FROM validation
WHERE email NOT IN (SELECT email FROM user_login);

