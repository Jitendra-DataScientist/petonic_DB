-- select * from challenge_json_data;

-- delete from challenge_json_data where challenge_identifier='1234';

-- ALTER TABLE challenge
-- ADD COLUMN contributor_id VARCHAR(255),
-- ADD COLUMN approver_id VARCHAR(255);


SELECT column_name
FROM information_schema.columns
WHERE table_name = 'contributor_approver';

CREATE TABLE contributor_approver (
    challenge_identifier VARCHAR(255),
    contributor_id VARCHAR(255),
    json_data JSON,
    CONSTRAINT unique_combination UNIQUE (challenge_identifier, contributor_id)
);

SELECT constraint_name, constraint_type
FROM information_schema.table_constraints
WHERE table_name = 'contributor_approver';

SELECT *
FROM information_schema.constraint_column_usage
WHERE table_name = 'contributor_approver';

INSERT INTO contributor_approver (challenge_identifier, contributor_id, json_data, approver_id, approver_comment)
VALUES
    ('1234', 'contributor_jitendra.nayak@petonic.in', '{"parameters": {"desirability":5,"validity":50},"description":"example1"}', 'approver_anne.smith@example.com','comment1'),
    ('234', 'contributor_anne.smith@example.com', '{"parameters": {"desirability":5,"validity":50},"description":"example2"}', 'approver_michael.doe@example.org','comment2'),
    ('45778', 'contributor_michael.doe@example.org', '{"parameters": {"desirability":5,"validity":50},"description":"example3"}', 'approver_jitendra.nayak@petonic.in','comment3');


select * from contributor_approver;

delete from contributor_approver;

-- ALTER TABLE contributor_json RENAME TO contributor_approver;

ALTER TABLE contributor_approver
ADD COLUMN approver_id VARCHAR(255),
ADD COLUMN approver_comment TEXT;
