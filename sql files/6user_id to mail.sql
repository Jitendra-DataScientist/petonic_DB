ALTER TABLE user_login
DROP CONSTRAINT IF EXISTS user_login_pkey
CASCADE;

ALTER TABLE user_login
DROP COLUMN IF EXISTS user_id;

DROP TABLE company CASCADE;

-- Add a new primary key constraint on the "email" column
ALTER TABLE user_login
ADD PRIMARY KEY (email);


-- To get all constraints for the user_login table
SELECT *
FROM information_schema.table_constraints
WHERE table_name = 'user_login';


SELECT
    constraint_name,
    constraint_type
FROM
    information_schema.table_constraints
WHERE
    table_name = 'user_login';



select * from user_login;
select * from user_signup;


SELECT *
FROM information_schema.table_constraints
WHERE table_name = 'user_signup';


-- Drop the dependent foreign key constraint
ALTER TABLE validation
DROP CONSTRAINT IF EXISTS validation_user_id_fkey;


CREATE TABLE user_signup_backup AS
SELECT * FROM user_signup;

DROP TABLE IF EXISTS user_signup;

ALTER TABLE user_signup_backup
RENAME TO user_signup;	


CREATE TABLE user_signup (
    email VARCHAR(255) PRIMARY KEY,
    f_name VARCHAR(50),
    l_name VARCHAR(50)
);

INSERT INTO user_signup (email, f_name, l_name)
VALUES
    ('johndoe@example.com', 'John', 'Doe'),
    ('janesmith@example.com', 'Jane', 'Smith'),
    ('alicejohnson@example.com', 'Alice', 'Johnson'),
    ('bobwilson@example.com', 'Bob', 'Wilson'),
    ('evaadams@example.com', 'Eva', 'Adams'),
    ('charliebrown@example.com', 'Charlie', 'Brown'),
    ('graceharrison@example.com', 'Grace', 'Harrison'),
    ('lucasanderson@example.com', 'Lucas', 'Anderson'),
    ('oliviamartin@example.com', 'Olivia', 'Martin'),
    ('jitendra.nayak@petonic.in', 'Jitendra', 'Nayak');


ALTER TABLE user_signup
ADD CONSTRAINT fk_user_signup_login
FOREIGN KEY (email) REFERENCES user_login(email)
ON DELETE CASCADE;


select * from validation;
DROP TABLE validation;

CREATE TABLE validation (
    email VARCHAR(255) PRIMARY KEY
);

INSERT INTO validation (email) VALUES
('johndoe@example.com'),
('jitendra.nayak@petonic.in');

ALTER TABLE validation
ADD CONSTRAINT fk_validation_user_login
FOREIGN KEY (email)
REFERENCES user_login(email)
ON DELETE CASCADE; -- Choose appropriate action on delete (CASCADE, SET NULL, etc.)



SELECT *
FROM information_schema.table_constraints
WHERE table_name = 'challenge';


CREATE TABLE challenge_backup AS
SELECT * FROM challenge;


DROP TABLE IF EXISTS challenge CASCADE;


ALTER TABLE challenge_backup
RENAME TO challenge;

ALTER TABLE challenge
ADD PRIMARY KEY (challenge_id);


SELECT *
FROM information_schema.table_constraints
WHERE table_name = 'challenge';


UPDATE challenge
SET initiator_id = NULL;

-- Set initiator_id to 'jitendra.nayak@petonic.in' for rows with id 1, 3, 5
UPDATE challenge
SET initiator_id = 'jitendra.nayak@petonic.in'
WHERE challenge_id in (1, 3, 5, 7);

-- Set initiator_id to 'johndoe@example.com' for rows with id 2, 4, 6
UPDATE challenge
SET initiator_id = 'johndoe@example.com'
WHERE challenge_id IN (2, 4, 6);


select * from challenge;


-- Add foreign keys to challenge_status table
ALTER TABLE challenge_status
ADD CONSTRAINT fk_challenge_status
FOREIGN KEY (challenge_id) REFERENCES challenge(challenge_id);

-- Add foreign keys to score_params_user table
ALTER TABLE score_params_user
ADD CONSTRAINT fk_score_params_user
FOREIGN KEY (challenge_id) REFERENCES challenge(challenge_id);


-- Add foreign key to challenge table
ALTER TABLE challenge
ADD CONSTRAINT fk_challenge_user_login
FOREIGN KEY (initiator_id) REFERENCES user_login(email);
