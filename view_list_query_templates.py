"""this script contains the template queries for view-list API"""

class ViewListQueryTemplates:   #pylint: disable=too-few-public-methods
    """this class contains the template queries for view-list API"""
    where_limit = """SELECT
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
                    c.pm_id,
                    c.pm_tool,
                    CONCAT_WS(' ', COALESCE(um.f_name, ''), COALESCE(um.l_name, '')) AS pm_name,
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
                LEFT JOIN 
                    user_signup um ON c.pm_id = um.email
                LEFT JOIN 
                    user_login ul ON ul.email = ui.email OR ul.email = ua.email OR ul.email = um.email
                WHERE
                    %s
                GROUP BY
                    c.challenge_id, 
                    c.initiator_id, 
                    ui.f_name,
                    ui.l_name,
                    ua.f_name,
                    ua.l_name,
                    um.f_name,
                    um.l_name,
                    c.initiation_timestamp, 
                    c.industry, 
                    c.domain,
                    c.process, 
                    c.creation_timestamp, 
                    c.name, 
                    c.description,
                    c.pm_id,
                    c.pm_tool,
                    cs.challenge_status,
                    cs.challenge_status_json::TEXT, 
                    ca.approver_id, 
                    ca.approver_comment
                %s;
                """
    where = """SELECT
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
                    c.pm_id,
                    c.pm_tool,
                    CONCAT_WS(' ', COALESCE(um.f_name, ''), COALESCE(um.l_name, '')) AS pm_name,
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
                LEFT JOIN 
                    user_signup um ON c.pm_id = um.email
                LEFT JOIN 
                    user_login ul ON ul.email = ui.email OR ul.email = ua.email OR ul.email = um.email
                WHERE
                    %s
                GROUP BY
                    c.challenge_id, 
                    c.initiator_id, 
                    ui.f_name,
                    ui.l_name,
                    ua.f_name,
                    ua.l_name,
                    um.f_name,
                    um.l_name,
                    c.initiation_timestamp, 
                    c.industry, 
                    c.domain,
                    c.process, 
                    c.creation_timestamp, 
                    c.name, 
                    c.description,
                    c.pm_id,
                    c.pm_tool,
                    cs.challenge_status,
                    cs.challenge_status_json::TEXT, 
                    ca.approver_id, 
                    ca.approver_comment;
                """
    limit = """SELECT
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
                    c.pm_id,
                    c.pm_tool,
                    CONCAT_WS(' ', COALESCE(um.f_name, ''), COALESCE(um.l_name, '')) AS pm_name,
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
                LEFT JOIN 
                    user_signup um ON c.pm_id = um.email
                LEFT JOIN 
                    user_login ul ON ul.email = ui.email OR ul.email = ua.email OR ul.email = um.email
                GROUP BY
                    c.challenge_id, 
                    c.initiator_id, 
                    ui.f_name,
                    ui.l_name,
                    ua.f_name,
                    ua.l_name,
                    um.f_name,
                    um.l_name,
                    c.initiation_timestamp, 
                    c.industry, 
                    c.domain,
                    c.process, 
                    c.creation_timestamp, 
                    c.name, 
                    c.description,
                    c.pm_id,
                    c.pm_tool,
                    cs.challenge_status,
                    cs.challenge_status_json::TEXT, 
                    ca.approver_id, 
                    ca.approver_comment
                %s;
                """
    no_filter = """SELECT
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
                        c.pm_id,
                        c.pm_tool,
                        CONCAT_WS(' ', COALESCE(um.f_name, ''), COALESCE(um.l_name, '')) AS pm_name,
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
                    LEFT JOIN 
                        user_signup um ON c.pm_id = um.email
                    LEFT JOIN 
                        user_login ul ON ul.email = ui.email OR ul.email = ua.email OR ul.email = um.email
                    GROUP BY
                        c.challenge_id, 
                        c.initiator_id, 
                        ui.f_name,
                        ui.l_name,
                        ua.f_name,
                        ua.l_name,
                        um.f_name,
                        um.l_name,
                        c.initiation_timestamp, 
                        c.industry, 
                        c.domain,
                        c.process, 
                        c.creation_timestamp, 
                        c.name, 
                        c.description,
                        c.pm_id,
                        c.pm_tool,
                        cs.challenge_status,
                        cs.challenge_status_json::TEXT, 
                        ca.approver_id, 
                        ca.approver_comment;
                    """
