DELETE FROM challenge_status
WHERE challenge_id IN ('EDU011', 'ENV000', 'ENV001', 'ENV002', 'ENV003', 'AUT005', 'AUT006', 'RET002', 'RET001', 'RET004');

DELETE FROM challenge_json_data
WHERE challenge_id IN ('EDU011', 'ENV000', 'ENV001', 'ENV002', 'ENV003', 'AUT005', 'AUT006', 'RET002', 'RET001', 'RET004');


DELETE FROM contributor_approver
WHERE challenge_id IN ('EDU011', 'ENV000', 'ENV001', 'ENV002', 'ENV003', 'AUT005', 'AUT006', 'RET002', 'RET001', 'RET004');


DELETE FROM gen_ai_analytics
WHERE challenge_id IN ('EDU011', 'ENV000', 'ENV001', 'ENV002', 'ENV003', 'AUT005', 'AUT006', 'RET002', 'RET001', 'RET004');


DELETE FROM gen_ai_token_usage
WHERE challenge_id IN ('EDU011', 'ENV000', 'ENV001', 'ENV002', 'ENV003', 'AUT005', 'AUT006', 'RET002', 'RET001', 'RET004');


DELETE FROM challenge
WHERE challenge_id IN ('EDU011', 'ENV000', 'ENV001', 'ENV002', 'ENV003', 'AUT005', 'AUT006', 'RET002', 'RET001', 'RET004');


select * from gen_ai_analytics;
ALTER TABLE gen_ai_analytics
ALTER COLUMN gen_ai_api TYPE VARCHAR(100);


select * from gen_ai_token_usage;


select challenge_id from challenge;

ALTER TABLE gen_ai_token_usage
ADD COLUMN ai_tokens int,
ADD COLUMN ai_cost decimal(9,6);

ALTER TABLE gen_ai_analytics
ADD COLUMN timestamp TIMESTAMP WITHOUT TIME ZONE;

ALTER TABLE gen_ai_analytics
ALTER COLUMN timestamp TYPE FLOAT;

ALTER TABLE gen_ai_analytics
DROP COLUMN timestamp;

ALTER TABLE gen_ai_analytics
ADD COLUMN timestamp float;

select * from gen_ai_analytics;

select * from challenge;
select * from user_signup;


update gen_ai_analytics
set timestamp ='1710491483.138055';