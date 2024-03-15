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

select sum(cost), sum(tokens) from gen_ai_token_usage;


select challenge_id from challenge;

ALTER TABLE gen_ai_token_usage
ADD COLUMN ai_tokens int,
ADD COLUMN ai_cost decimal(9,6);


select gu.challenge_id, gu.tokens as total_tokens, gu.cost as total_cost, gu.ai_tokens, gu.ai_cost,
c.initiator_id,
us.f_name, us.l_name
from gen_ai_token_usage gu
left join challenge c
on gu.challenge_id=c.challenge_id
left join user_signup us
on c.initiator_id=us.email;


select gu.tokens as total_tokens, gu.cost as total_cost, gu.ai_tokens, gu.ai_cost,
CONCAT(us.f_name, ' ', us.l_name) AS name
from gen_ai_token_usage gu
left join challenge c
on gu.challenge_id=c.challenge_id
left join user_signup us
on c.initiator_id=us.email;

SELECT
    CONCAT(us.f_name, ' ', us.l_name) AS name,
    SUM(COALESCE(gu.tokens, 0)) AS total_tokens,
    SUM(COALESCE(gu.ai_tokens, 0)) AS total_ai_tokens,
    SUM(COALESCE(gu.cost, 0)) AS total_cost,
    SUM(COALESCE(gu.ai_cost, 0)) AS total_ai_cost
FROM
    gen_ai_token_usage gu
LEFT JOIN
    challenge c ON gu.challenge_id = c.challenge_id
LEFT JOIN
    user_signup us ON c.initiator_id = us.email
GROUP BY
    CONCAT(us.f_name, ' ', us.l_name);

SELECT
    CONCAT(us.f_name, ' ', us.l_name) AS name,
    SUM(COALESCE(gu.tokens, 0)) AS total_tokens,
    SUM(COALESCE(gu.ai_tokens, 0)) AS total_ai_tokens,
    SUM(COALESCE(gu.cost, 0)) AS total_cost,
    SUM(COALESCE(gu.ai_cost, 0)) AS total_ai_cost,
    SUM(COALESCE(gu.tokens, 0)) - SUM(COALESCE(gu.ai_tokens, 0)) AS user_tokens,
    SUM(COALESCE(gu.cost, 0)) - SUM(COALESCE(gu.ai_cost, 0)) AS user_cost
FROM
    gen_ai_token_usage gu
LEFT JOIN
    challenge c ON gu.challenge_id = c.challenge_id
LEFT JOIN
    user_signup us ON c.initiator_id = us.email
GROUP BY
    CONCAT(us.f_name, ' ', us.l_name);

ALTER TABLE gen_ai_analytics
ADD COLUMN timestamp TIMESTAMP WITHOUT TIME ZONE;

ALTER TABLE gen_ai_analytics
DROP COLUMN timestamp;

ALTER TABLE gen_ai_analytics
ADD COLUMN timestamp float;


SELECT
    CONCAT(us.f_name, ' ', us.l_name) AS name,
    us.employee_id,
    SUM(COALESCE(gu.tokens, 0)) AS total_tokens,
    SUM(COALESCE(gu.ai_tokens, 0)) AS total_ai_tokens,
    SUM(COALESCE(gu.cost, 0)) AS total_cost,
    SUM(COALESCE(gu.ai_cost, 0)) AS total_ai_cost,
    SUM(COALESCE(gu.tokens, 0)) - SUM(COALESCE(gu.ai_tokens, 0)) AS user_tokens,
    SUM(COALESCE(gu.cost, 0)) - SUM(COALESCE(gu.ai_cost, 0)) AS user_cost
FROM
    gen_ai_token_usage gu
LEFT JOIN
    challenge c ON gu.challenge_id = c.challenge_id
LEFT JOIN
    user_signup us ON c.initiator_id = us.email
GROUP BY
    CONCAT(us.f_name, ' ', us.l_name),
    us.employee_id;

select * from gen_ai_analytics;

SELECT column_name, data_type
FROM information_schema.columns
WHERE table_name = 'gen_ai_analytics';


select * from user_signup;

update gen_ai_analytics
set timestamp ='1710491483.138055';

SELECT challenge_id, gen_ai_api, cost, tokens, timestamp
                    FROM gen_ai_analytics
                    WHERE timestamp >= 1700491483.138055
                    AND timestamp <= 1710491483.138055;