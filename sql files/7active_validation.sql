select * from user_login;

select * from user_signup;

select * from validation;

ALTER TABLE validation
ADD COLUMN active BOOLEAN;

UPDATE validation
SET active = true
WHERE email='johndoe@example.com';

select * from user_signup;

select * from validation;

select * from challenge;

select * from challenge_json_data;

delete from challenge;

delete from challenge_status;

select * from challenge_status;

delete from user_login where email='jitendra.nayak@petonic.in';

delete from user_signup where email='jitendra.nayak@petonic.in';

delete from validation where email='jitendra.nayak@petonic.in';

select * from user_login;

select * from user_signup;

select * from validation;

UPDATE validation
SET active = NOT active
where email = 'jitendra.nayak@petonic.in';


