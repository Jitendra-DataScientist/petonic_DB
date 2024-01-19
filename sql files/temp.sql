select * from contributor_approver;


delete from contributor_approver;


UPDATE contributor_approver
SET approver_id = 'your_approver_id'
WHERE challenge_id = 'your_challenge_id' AND approver_id IS NULL
RETURNING *;


UPDATE contributor_approver
SET contributor_id = ARRAY_APPEND(contributor_id, 'new_contributor_id')
WHERE challenge_id = 1;




