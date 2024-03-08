CREATE TABLE gen_ai_analytics (
    gen_ai_api VARCHAR(30),
    challenge_id VARCHAR(20),
    input JSON,
    prompt TEXT,
    output JSON,
    human_feedback JSON,
    model_params JSON
);


select * from gen_ai_analytics;

ALTER TABLE gen_ai_analytics
ADD CONSTRAINT fk_challenge_id
FOREIGN KEY (challenge_id)
REFERENCES challenge(challenge_id);

ALTER TABLE gen_ai_analytics
ADD PRIMARY KEY (challenge_id);


select * from gen_ai_analytics;

SELECT
    tc.constraint_name,
    tc.constraint_type,
    kcu.column_name,
    ccu.table_name AS foreign_table_name,
    ccu.column_name AS foreign_column_name
FROM
    information_schema.table_constraints AS tc
    JOIN information_schema.key_column_usage AS kcu
      ON tc.constraint_name = kcu.constraint_name
    LEFT JOIN information_schema.constraint_column_usage AS ccu
      ON ccu.constraint_name = tc.constraint_name
WHERE
    tc.table_name = 'gen_ai_analytics';
	
ALTER TABLE gen_ai_analytics
DROP CONSTRAINT gen_ai_analytics_pkey;

ALTER TABLE gen_ai_analytics
ADD CONSTRAINT composite_key_challenge_gen_ai_api UNIQUE (challenge_id, gen_ai_api);


ALTER TABLE gen_ai_analytics
DROP COLUMN human_feedback;
