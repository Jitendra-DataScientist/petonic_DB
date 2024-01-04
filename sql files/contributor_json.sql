-- select * from challenge_json_data;

-- select * from contributor_json;

-- delete from challenge_json_data where challenge_identifier='1234';

-- ALTER TABLE challenge
-- ADD COLUMN contributor_id VARCHAR(255),
-- ADD COLUMN approver_id VARCHAR(255);


SELECT column_name
FROM information_schema.columns
WHERE table_name = 'contributor_json';

CREATE TABLE contributor_json (
    challenge_identifier VARCHAR(255),
    contributor_id VARCHAR(255),
    json_data JSON,
    CONSTRAINT unique_combination UNIQUE (challenge_identifier, contributor_id)
);

SELECT constraint_name, constraint_type
FROM information_schema.table_constraints
WHERE table_name = 'contributor_json';

SELECT *
FROM information_schema.constraint_column_usage
WHERE table_name = 'contributor_json';

INSERT INTO contributor_json (challenge_identifier, contributor_id, json_data)
VALUES
    ('initiator_jitendra.nayak@petonic.in', 'contributor_123', '{"data": "example1"}'),
    ('initiator_anne.smith@example.com', 'contributor_456', '{"data": "example2"}'),
    ('initiator_michael.doe@example.org', 'contributor_789', '{"data": "example3"}');


select * from contributor_json;

delete from contributor_json;