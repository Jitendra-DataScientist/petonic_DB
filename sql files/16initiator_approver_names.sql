			SELECT c.challenge_id, c.initiator_id, c.initiation_timestamp,
					c.industry, c.domain, c.process, c.creation_timestamp, c.name,
					c.description, cs.challenge_status,
					cs.challenge_status_json::TEXT AS challenge_status_json_text,
					ARRAY_AGG(keys.contributor_approver_keys) AS contributor_approver_keys,
					ca.approver_id AS approver_id, ca.approver_comment AS approver_comment
							FROM challenge c
					LEFT JOIN challenge_status cs ON c.challenge_id = cs.challenge_id
					LEFT JOIN (
					SELECT DISTINCT challenge_id,
						json_object_keys(contributor_approver_json) AS contributor_approver_keys
						FROM contributor_approver
					) keys ON c.challenge_id = keys.challenge_id
					LEFT JOIN contributor_approver ca ON c.challenge_id = ca.challenge_id
					GROUP BY
					c.challenge_id, c.initiator_id, c.initiation_timestamp, c.industry, c.domain,
					c.process, c.creation_timestamp, c.name, c.description,cs.challenge_status,
					cs.challenge_status_json::TEXT, ca.approver_id, ca.approver_comment;
					




--added initiator names
SELECT 
    c.challenge_id, 
    c.initiator_id, 
    CONCAT_WS(' ', COALESCE(u.f_name, ''), COALESCE(u.l_name, '')) AS initiator_name,
    c.initiation_timestamp,
    c.industry, 
    c.domain, 
    c.process, 
    c.creation_timestamp, 
    c.name,
    c.description, 
    cs.challenge_status,
    cs.challenge_status_json::TEXT AS challenge_status_json_text,
    ARRAY_AGG(keys.contributor_approver_keys) AS contributor_approver_keys,
    ca.approver_id AS approver_id, 
    ca.approver_comment AS approver_comment
FROM 
    challenge c
LEFT JOIN 
    challenge_status cs ON c.challenge_id = cs.challenge_id
LEFT JOIN (
    SELECT 
        DISTINCT challenge_id,
        json_object_keys(contributor_approver_json) AS contributor_approver_keys
    FROM 
        contributor_approver
) keys ON c.challenge_id = keys.challenge_id
LEFT JOIN 
    contributor_approver ca ON c.challenge_id = ca.challenge_id
LEFT JOIN 
    user_signup u ON c.initiator_id = u.email
GROUP BY
    c.challenge_id, 
    c.initiator_id, 
    u.f_name,
    u.l_name,
    c.initiation_timestamp, 
    c.industry, 
    c.domain,
    c.process, 
    c.creation_timestamp, 
    c.name, 
    c.description,
    cs.challenge_status,
    cs.challenge_status_json::TEXT, 
    ca.approver_id, 
    ca.approver_comment;



--added approver names
SELECT 
    c.challenge_id, 
    c.initiator_id, 
    CONCAT_WS(' ', COALESCE(ui.f_name, ''), COALESCE(ui.l_name, '')) AS initiator_name,
    c.initiation_timestamp,
    c.industry, 
    c.domain, 
    c.process, 
    c.creation_timestamp, 
    c.name,
    c.description, 
    cs.challenge_status,
    cs.challenge_status_json::TEXT AS challenge_status_json_text,
    ARRAY_AGG(keys.contributor_approver_keys) AS contributor_approver_keys,
    ca.approver_id AS approver_id, 
    CONCAT_WS(' ', COALESCE(ua.f_name, ''), COALESCE(ua.l_name, '')) AS approver_name,
    ca.approver_comment AS approver_comment
FROM 
    challenge c
LEFT JOIN 
    challenge_status cs ON c.challenge_id = cs.challenge_id
LEFT JOIN (
    SELECT 
        DISTINCT challenge_id,
        json_object_keys(contributor_approver_json) AS contributor_approver_keys
    FROM 
        contributor_approver
) keys ON c.challenge_id = keys.challenge_id
LEFT JOIN 
    contributor_approver ca ON c.challenge_id = ca.challenge_id
LEFT JOIN 
    user_signup ui ON c.initiator_id = ui.email
LEFT JOIN 
    user_signup ua ON ca.approver_id = ua.email
GROUP BY
    c.challenge_id, 
    c.initiator_id, 
    ui.f_name,
    ui.l_name,
    ua.f_name,
    ua.l_name,
    c.initiation_timestamp, 
    c.industry, 
    c.domain,
    c.process, 
    c.creation_timestamp, 
    c.name, 
    c.description,
    cs.challenge_status,
    cs.challenge_status_json::TEXT, 
    ca.approver_id, 
    ca.approver_comment;


-- with where clause
SELECT 
    c.challenge_id, 
    c.initiator_id, 
    CONCAT_WS(' ', COALESCE(ui.f_name, ''), COALESCE(ui.l_name, '')) AS initiator_name,
    c.initiation_timestamp,
    c.industry, 
    c.domain, 
    c.process, 
    c.creation_timestamp, 
    c.name,
    c.description, 
    cs.challenge_status,
    cs.challenge_status_json::TEXT AS challenge_status_json_text,
    ARRAY_AGG(keys.contributor_approver_keys) AS contributor_approver_keys,
    ca.approver_id AS approver_id, 
    CONCAT_WS(' ', COALESCE(ua.f_name, ''), COALESCE(ua.l_name, '')) AS approver_name,
    ca.approver_comment AS approver_comment
FROM 
    challenge c
LEFT JOIN 
    challenge_status cs ON c.challenge_id = cs.challenge_id
LEFT JOIN (
    SELECT 
        DISTINCT challenge_id,
        json_object_keys(contributor_approver_json) AS contributor_approver_keys
    FROM 
        contributor_approver
) keys ON c.challenge_id = keys.challenge_id
LEFT JOIN 
    contributor_approver ca ON c.challenge_id = ca.challenge_id
LEFT JOIN 
    user_signup ui ON c.initiator_id = ui.email
LEFT JOIN 
    user_signup ua ON ca.approver_id = ua.email
WHERE
    c.initiator_id = 'your_initiator_id_here'
GROUP BY
    c.challenge_id, 
    c.initiator_id, 
    ui.f_name,
    ui.l_name,
    ua.f_name,
    ua.l_name,
    c.initiation_timestamp, 
    c.industry, 
    c.domain,
    c.process, 
    c.creation_timestamp, 
    c.name, 
    c.description,
    cs.challenge_status,
    cs.challenge_status_json::TEXT, 
    ca.approver_id, 
    ca.approver_comment;
