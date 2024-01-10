select * from user_login;

select * from user_signup;

select * from validation;

delete from validation where email = 'jitendra.nayak@petonic.in';

delete from user_login where email = 'jitendra.nayak@petonic.in';

select * from challenge;

delete from challenge;

delete from challenge_status;

select * from challenge_status;

select * from challenge_json_data;

delete from challenge_json_data;

ALTER TABLE challenge_json_data
ADD COLUMN new_challenge_id smallint;


-- Step 3: Update new column with existing data
UPDATE challenge_json_data
SET new_challenge_id = CAST(challenge_identifier AS smallint);

-- Step 4: Drop old column
ALTER TABLE challenge_json_data
DROP COLUMN challenge_identifier;

-- Step 5: Rename the new column
ALTER TABLE challenge_json_data
RENAME COLUMN new_challenge_id TO challenge_identifier;

ALTER TABLE challenge_json_data
RENAME COLUMN challenge_identifier TO challenge_id;

ALTER TABLE challenge_json_data
ADD PRIMARY KEY (challenge_id);



ALTER TABLE challenge_json_data
ADD CONSTRAINT fk_challenge_id
    FOREIGN KEY (challenge_id)
    REFERENCES challenge(challenge_id)
    ON UPDATE CASCADE
    ON DELETE CASCADE;