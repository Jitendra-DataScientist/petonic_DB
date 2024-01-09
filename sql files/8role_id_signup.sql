select * from user_login;

select * from user_signup;


ALTER TABLE user_signup
ADD COLUMN role VARCHAR(15),    -- Set the length to 15
ADD COLUMN employee_id INT;

UPDATE user_signup
SET
  role = CASE
           WHEN email = 'johndoe@example.com' THEN 'initiator'
           WHEN email = 'janesmith@example.com' THEN 'stakeholder'
           WHEN email = 'alicejohnson@example.com' THEN 'contributor'
           WHEN email = 'bobwilson@example.com' THEN 'initiator'
           WHEN email = 'evaadams@example.com' THEN 'stakeholder'
           WHEN email = 'charliebrown@example.com' THEN 'contributor'
           WHEN email = 'graceharrison@example.com' THEN 'initiator'
           WHEN email = 'lucasanderson@example.com' THEN 'stakeholder'
           WHEN email = 'oliviamartin@example.com' THEN 'contributor'
           WHEN email = 'jitendra.nayak@petonic.in' THEN 'initiator'
         END,
  employee_id = CASE
                  WHEN email = 'johndoe@example.com' THEN 1
                  WHEN email = 'janesmith@example.com' THEN 2
                  WHEN email = 'alicejohnson@example.com' THEN 3
                  WHEN email = 'bobwilson@example.com' THEN 4
                  WHEN email = 'evaadams@example.com' THEN 5
                  WHEN email = 'charliebrown@example.com' THEN 6
                  WHEN email = 'graceharrison@example.com' THEN 7
                  WHEN email = 'lucasanderson@example.com' THEN 8
                  WHEN email = 'oliviamartin@example.com' THEN 9
                  WHEN email = 'jitendra.nayak@petonic.in' THEN 10
                END;

ALTER TABLE user_login
DROP COLUMN employee_id,
DROP COLUMN role;

