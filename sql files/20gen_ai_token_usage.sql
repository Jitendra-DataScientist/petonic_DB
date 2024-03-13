ALTER TABLE gen_ai_analytics
ADD COLUMN tokens INT,
ADD COLUMN cost DECIMAL(9,6);

select * from gen_ai_analytics;

delete from gen_ai_analytics;

ALTER TABLE gen_ai_analytics REPLICA IDENTITY FULL;

INSERT INTO gen_ai_analytics (challenge_id, gen_ai_api, input,prompt, output, model_params)
VALUES ('BFS021','fin_impact.py','{"a":"b"}','kuchBhi','{"a":"b"}','{"a":"b"}');

INSERT INTO gen_ai_analytics (challenge_id, gen_ai_api, input,prompt, output, model_params,tokens)
VALUES ('BFS021','non_fin_impact.py','{"a":"b"}','kuchBhi','{"a":"b"}','{"a":"b"}',123);

INSERT INTO gen_ai_analytics (challenge_id, gen_ai_api, input,prompt, output, model_params,cost)
VALUES ('BFS021','solution.py','{"a":"b"}','kuchBhi','{"a":"b"}','{"a":"b"}',123.1234);

CREATE TABLE gen_ai_token_usage (
    challenge_id varchar(20) PRIMARY KEY,
    tokens int,
    cost decimal(9,6)
);

select * from gen_ai_token_usage;
