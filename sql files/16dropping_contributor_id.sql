SELECT c.challenge_id, c.initiator_id, c.initiation_timestamp, c.industry,
           c.domain, c.process, c.creation_timestamp, c.name, c.description,
           cs.challenge_status, cs.challenge_status_json, 
           json_object_keys(ca.contributor_approver_json) AS contributor_approver_keys,
           ca.approver_id, ca.approver_comment
    FROM challenge c
    LEFT JOIN challenge_status cs ON c.challenge_id = cs.challenge_id
    LEFT JOIN contributor_approver ca ON c.challenge_id = ca.challenge_id;


select * from contributor_approver;


SELECT c.challenge_id, c.initiator_id, c.initiation_timestamp, c.industry,
                        c.domain, c.process, c.creation_timestamp, c.name, c.description, cs.challenge_status,
                        cs.challenge_status_json, ca.contributor_id, ca.approver_id, ca.approver_comment
                        FROM challenge c
                        LEFT JOIN challenge_status cs
                        ON c.challenge_id = cs.challenge_id
                        LEFT JOIN contributor_approver ca
                        ON c.challenge_id = ca.challenge_id;


SELECT c.challenge_id, c.initiator_id, c.initiation_timestamp, c.industry,
       c.domain, c.process, c.creation_timestamp, c.name, c.description,
       cs.challenge_status, cs.challenge_status_json,
       keys.contributor_approver_keys,
       ca.approver_id, ca.approver_comment
FROM challenge c
LEFT JOIN challenge_status cs ON c.challenge_id = cs.challenge_id
LEFT JOIN (
    SELECT DISTINCT challenge_id, json_object_keys(contributor_approver_json) AS contributor_approver_keys
    FROM contributor_approver
) keys ON c.challenge_id = keys.challenge_id
LEFT JOIN contributor_approver ca ON c.challenge_id = ca.challenge_id;


SELECT 
    c.challenge_id, 
    c.initiator_id, 
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
FROM challenge c
LEFT JOIN challenge_status cs ON c.challenge_id = cs.challenge_id
LEFT JOIN (
    SELECT DISTINCT challenge_id, json_object_keys(contributor_approver_json) AS contributor_approver_keys
    FROM contributor_approver
) keys ON c.challenge_id = keys.challenge_id
LEFT JOIN contributor_approver ca ON c.challenge_id = ca.challenge_id
GROUP BY 
    c.challenge_id, 
    c.initiator_id, 
    c.initiation_timestamp, 
    c.industry,
    c.domain, 
    c.process, 
    c.creation_timestamp, 
    c.name, 
    c.description,
    cs.challenge_status, 
    cs.challenge_status_json::TEXT;

