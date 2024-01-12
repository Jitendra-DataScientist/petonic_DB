select * from user_login;

select * from user_signup;

select * from validation;


SELECT ul.*, us.*, v.user_id as validation
FROM user_login ul
LEFT JOIN user_signup us ON ul.user_id = us.user_id
LEFT JOIN validation v ON ul.user_id = v.user_id;


ALTER TABLE user_login
RENAME COLUMN company_id TO employee_id;


SELECT 
    ul.email,ul.role,ul.employee_id,
    us.f_name,us.l_name,
    CASE WHEN v.user_id IS NOT NULL THEN 'True' ELSE 'False' END as validation
FROM 
    user_login ul
LEFT JOIN 
    user_signup us ON ul.user_id = us.user_id
LEFT JOIN 
    validation v ON ul.user_id = v.user_id;


SELECT
    ul.email,ul.role,ul.employee_id,
    us.f_name,us.l_name
FROM user_login ul
LEFT JOIN user_signup us ON ul.user_id = us.user_id
LEFT JOIN validation v ON ul.user_id = v.user_id
WHERE v.user_id IS NOT NULL;


SELECT 
    us.email,us.role,us.employee_id,us.f_name,us.l_name,
    v.active
FROM 
    user_signup us
LEFT JOIN 
    validation v ON us.email = v.email;


select * from user_signup us;
join validation v
on us.email = v.email;

INSERT INTO validation (email)
SELECT ul.email
FROM user_login ul
WHERE ul.email NOT IN (SELECT v.email FROM validation v);


INSERT INTO validation (email, active)
SELECT ul.email, 
       ROW_NUMBER() OVER (ORDER BY ul.email) % 2 = 0 as active
FROM user_login ul
WHERE ul.email NOT IN (SELECT v.email FROM validation v);

