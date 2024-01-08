select * from challenge;

select * from challenge_status;

select * from challenge
join challenge_status
on (challenge.challenge_id = challenge_status.challenge_id)
where initiator_id = 'initiator_jitendra.nayak@petonic.in';

select * from challenge
join challenge_status
on (challenge.challenge_id = challenge_status.challenge_id);

select * from user_login;
select * from validation;