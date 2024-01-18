select * from challenge_json_data;

select * from challenge_status;

select * from contributor_approver;


ALTER TABLE challenge_json_data
RENAME COLUMN json_data TO challenge_json;

ALTER TABLE challenge_status
RENAME COLUMN json_data TO challenge_status_json;

ALTER TABLE contributor_approver
RENAME COLUMN json_data TO contributor_approver_json;
