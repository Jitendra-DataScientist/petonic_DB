-- Drop the foreign key constraint
ALTER TABLE challenge_json_data DROP CONSTRAINT fk_challenge_id_json_data;
-- Drop the foreign key constraint
ALTER TABLE challenge_status DROP CONSTRAINT fk_challenge_id_status;
-- Drop the foreign key constraint
ALTER TABLE contributor_approver DROP CONSTRAINT fk_challenge_id_contributor_approver;


-- Alter the datatype of the challenge_id column in the challenge table
ALTER TABLE challenge ALTER COLUMN challenge_id TYPE varchar;
ALTER TABLE challenge_json_data ALTER COLUMN challenge_id TYPE varchar;
ALTER TABLE contributor_approver ALTER COLUMN challenge_id TYPE varchar;
ALTER TABLE challenge_status ALTER COLUMN challenge_id TYPE varchar;


-- Recreate the foreign key constraint with the updated datatype
ALTER TABLE contributor_approver ADD CONSTRAINT fk_challenge_id_contributor_approver FOREIGN KEY (challenge_id) REFERENCES challenge(challenge_id);
-- Recreate the foreign key constraint with the updated datatype
ALTER TABLE challenge_status ADD CONSTRAINT fk_challenge_id_status FOREIGN KEY (challenge_id) REFERENCES challenge(challenge_id);
-- Recreate the foreign key constraint with the updated datatype
ALTER TABLE challenge_json_data ADD CONSTRAINT fk_challenge_id_json_data FOREIGN KEY (challenge_id) REFERENCES challenge(challenge_id);


select * from challenge;