select * from contributor_approver;

select * from challenge;

delete from contributor_approver;


UPDATE contributor_approver
SET approver_id = 'your_approver_id'
WHERE challenge_id = 'your_challenge_id' AND approver_id IS NULL
RETURNING *;


UPDATE contributor_approver
SET contributor_id = ARRAY_APPEND(contributor_id, 'new_contributor_id')
WHERE challenge_id = 1;

select count(*) from user_signup
where email = 'oliviamartin@example.com' and role = 'contributor';

select * from user_signup;
-- alicejohnson@example.com
-- oliviamartin@example.com
-- charliebrown@example.com

-- janesmith@example.com
-- evaadams@example.com


-- UPDATE user_signup
-- SET role = 'approver'
-- WHERE role = 'stakeholder';

