select * from challenge;

select * from challenge_status;

select * from contributor_approver;

delete from contributor_approver where challenge_id in (3,2);


SELECT c.challenge_id, c.initiator_id, c.initiation_timestamp, c.industry, c.domain, c.process,
c.creation_timestamp, c.name, c.description, cs.challenge_status, cs.challenge_status_json,
ca.contributor_id, ca.approver_id, ca.approver_comment
FROM challenge c
LEFT JOIN challenge_status cs
ON c.challenge_id = cs.challenge_id
LEFT JOIN contributor_approver ca
ON c.challenge_id = ca.challenge_id;


SELECT c.challenge_id, c.initiator_id, c.initiation_timestamp, c.industry, c.domain, c.process,
c.creation_timestamp, c.name, c.description, cs.challenge_status, cs.challenge_status_json,
ca.contributor_id, ca.approver_id, ca.approver_comment
FROM challenge c
LEFT JOIN challenge_status cs
ON c.challenge_id = cs.challenge_id
LEFT JOIN contributor_approver ca
ON c.challenge_id = ca.challenge_id
where c.initiator_id = 'johndoe@example.com';
