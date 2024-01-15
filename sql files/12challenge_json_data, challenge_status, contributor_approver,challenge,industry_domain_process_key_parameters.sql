select * from industry_domain_process_key_factors;

drop table industry_domain_process_key_factors;

select * from industry_domain_process_key_parameters;

select * from challenge;

SELECT column_name, data_type
FROM information_schema.columns
WHERE table_name = 'challenge';


SELECT *
FROM information_schema.table_constraints
WHERE table_name = 'challenge';


SELECT constraint_name, constraint_type
FROM information_schema.table_constraints
WHERE table_name = 'challenge';



-- Drop FOREIGN KEY constraint
-- ALTER TABLE challenge
-- DROP CONSTRAINT fk_challenge_user_login;

-- Drop CHECK constraint
-- ALTER TABLE challenge
-- DROP CONSTRAINT "2200_18439_1_not_null";

-- Drop PRIMARY KEY constraint
-- ALTER TABLE challenge
-- DROP CONSTRAINT challenge_pkey;

-- Now, drop the challenge table
DROP TABLE challenge cascade;




CREATE TABLE challenge (
    challenge_id smallint,
    initiator_id character varying,
    initiation_timestamp timestamp without time zone,
    industry character varying,
    process character varying,
    domain character varying,
    creation_timestamp timestamp without time zone,
    name character varying,
    description text,
    contributor_id text[], -- Change the data type to an array of text
    approver_id character varying
);


-- Recreate PRIMARY KEY constraint
ALTER TABLE challenge
ADD CONSTRAINT challenge_pkey PRIMARY KEY (challenge_id);

-- Recreate FOREIGN KEY constraint
ALTER TABLE challenge
ADD CONSTRAINT fk_challenge_user_login
FOREIGN KEY (initiator_id) REFERENCES user_login(email);

-- Recreate CHECK constraint
-- ALTER TABLE challenge
-- ADD CONSTRAINT c_2200_18439_1_not_null CHECK (description IS NOT NULL);

SELECT *
FROM information_schema.table_constraints
WHERE table_name = 'challenge';


SELECT constraint_name, constraint_type
FROM information_schema.table_constraints
WHERE table_name = 'challenge';

select * from challenge;

select * from challenge_status;

delete from challenge_status;

select * from challenge_json_data;

SELECT *
FROM information_schema.table_constraints
WHERE table_name = 'challenge_status';

drop table contributor_approver;

CREATE TABLE contributor_approver (
    challenge_id smallint PRIMARY KEY,
    contributor_id text[],
    json_data json,
    approver_id varchar,
    approver_comment varchar
);


-- For challenge_json_data
ALTER TABLE challenge_json_data
ADD CONSTRAINT fk_challenge_id_json_data
FOREIGN KEY (challenge_id) REFERENCES challenge(challenge_id)
ON DELETE NO ACTION;

-- For challenge_status
ALTER TABLE challenge_status
ADD CONSTRAINT fk_challenge_id_status
FOREIGN KEY (challenge_id) REFERENCES challenge(challenge_id)
ON DELETE NO ACTION;

-- For contributor_approver
ALTER TABLE contributor_approver
ADD CONSTRAINT fk_challenge_id_contributor_approver
FOREIGN KEY (challenge_id) REFERENCES challenge(challenge_id)
ON DELETE NO ACTION;


select * from contributor_approver;
