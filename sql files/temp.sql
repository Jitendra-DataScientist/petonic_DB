select * from challenge;

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
						c.initiation_timestamp BETWEEN '2024-02-04 08:16:17' AND '2024-02-05 08:16:17'
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
                            ca.approver_comment
LIMIT 
    40 -- Replace limit_value with the desired limit
OFFSET 
    0; -- Replace offset_value with the desired offset

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
    c.initiator_id = 'initiator_id_value' -- Replace 'initiator_id_value' with the desired initiator ID
    AND c.initiation_timestamp BETWEEN '2024-02-04 08:16:17' AND '2024-02-05 08:16:17' -- Replace with the desired initiation start and end dates
    AND c.creation_timestamp BETWEEN 'creation_start_date' AND 'creation_end_date' -- Replace with the desired creation start and end dates
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
    ca.approver_comment
LIMIT 
    40 -- Replace limit_value with the desired limit
OFFSET 
    0; -- Replace offset_value with the desired offset
