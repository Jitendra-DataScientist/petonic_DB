select count(*) from challenge;

select * from challenge;

select max(challenge_id) from challenge;

delete from challenge;

delete from challenge where challenge_id=1;

delete from challenge_status;


select * from challenge;

select * from challenge_json_data;

select * from challenge_status;

select * from contributor_approver;

select * from domain_list;

select * from industry_domain_process_key_factors;

select * from industry_list;

select * from process_list;

-- select * from score_params_user;

drop table score_params_user;

select * from user_login;

select * from user_signup;

select * from validation;

SELECT count(*) 
FROM information_schema.tables 
WHERE table_schema = 'public';

SELECT *
FROM information_schema.tables 
WHERE table_schema = 'public';