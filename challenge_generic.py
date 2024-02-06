"""
    this code primarily contains the generic challenge related
    funtions to connect python code to PostgreSQL database by
    calling relevant pyscopg2 operation files (CRUD)
"""
import os
import sys
import json
# from bson import json_util
# from pymongo import json_util
import logging
from django.core.serializers.json import DjangoJSONEncoder
from db_return import db_return
from db_no_return import db_no_return
from utils import Utils


# Determine the directory for logs
log_directory = os.path.join(os.getcwd(), 'logs')

# Create the logs directory if it doesn't exist
if not os.path.exists(log_directory):
    os.mkdir(log_directory)

# Configure logging
# logging.basicConfig(
#     level=logging.DEBUG,
#     format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
#     handlers=[logging.StreamHandler()],
# )

# Create a logger instance
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

# Create a file handler for this script's log file
file_handler = logging.FileHandler(os.path.join(log_directory, "challenge_generic.log"))
file_handler.setLevel(logging.DEBUG)  # Set the logging level for this handler

# Create a formatter
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
file_handler.setFormatter(formatter)

# Add the file handler to the logger
logger.addHandler(file_handler)


utils = Utils()


class CG:
    """
       this class primarily contains the generic challenge related
       funtions to connect python code to PostgreSQL database by
       calling relevant pyscopg2 operation files (CRUD)
    """
    def challenge_initiation(self, req_body):
        """function for challenge initiation (an entry added in challenge table)"""
        try:
            # challenge_id for this new challenge would be 1 plus
            # the count of challenges created by the same initiator
            try:
                challenge_id = self.challenge_count("max_of_ch_id")[0]['count'] + 1
            except TypeError:
                challenge_id = 1

            # Queries Formation
            query = ["INSERT INTO challenge\
                     (challenge_id, initiator_id, initiation_timestamp,\
                     industry, process, domain)\
                     VALUES (%s, %s,%s,%s,%s,%s);",]
            query_data = [
                            (
                                challenge_id,
                                req_body["initiator_id"],
                                req_body["initiation_timestamp"],
                                req_body["industry"],
                                req_body["process"],
                                req_body["domain"],
                            ),
                        ]

            try:
                res = db_no_return(query, query_data)

                if res == "success":   # pylint: disable=no-else-return
                    return {"creation": True,
                            "challenge_id": challenge_id}, 201
                else:
                    # logger.warning("challenge_id already present")
                    res.update({"creation": False})
                    return res, 400

            except Exception as db_error:  # pylint: disable=broad-exception-caught
                exception_type, _, exception_traceback = sys.exc_info()
                filename = exception_traceback.tb_frame.f_code.co_filename
                line_number = exception_traceback.tb_lineno
                logger.error("%s||||%s||||%d||||%d", exception_type, filename, line_number, db_error)    # pylint: disable=line-too-long
                return {
                    "creation": False,
                    "helpText": f"Exception: {exception_type}||||{filename}||||{line_number}||||{db_error}",    # pylint: disable=line-too-long
                }, 500

        except Exception as db_error:  # pylint: disable=broad-exception-caught
            exception_type, _, exception_traceback = sys.exc_info()
            filename = exception_traceback.tb_frame.f_code.co_filename
            line_number = exception_traceback.tb_lineno
            logger.error("%s||||%s||||%d||||%d", exception_type, filename, line_number, db_error)
            return {
                "creation": False,
                "helpText": f"Exception: {exception_type}||||{filename}||||{line_number}||||{db_error}",    # pylint: disable=line-too-long
            }, 500


    def challenge_count(self, req_body):
        """function for counting the number of
           challenges corresponding to a user_id
        """
        try:
            # Queries Formation
            if req_body == "max_of_ch_id":
                query = "select max(challenge_id) from challenge;"
                query_data = None
            elif "initiator_id" in req_body:
                query = "select count(*) from challenge where initiator_id=%s;"
                query_data = (
                                req_body["initiator_id"],
                            )
                query_data = (
                                req_body["initiator_id"],
                            )
            else:
                query = "select count(*) from challenge where challenge_id=%s;"
                query_data = (
                                req_body["challenge_id"],
                            )

            try:
                ret_data = db_return(query, query_data)

                return {"count_fetch": True,
                        "count": ret_data[0][0]}, 200

            except Exception as db_error:  # pylint: disable=broad-exception-caught
                exception_type, _, exception_traceback = sys.exc_info()
                filename = exception_traceback.tb_frame.f_code.co_filename
                line_number = exception_traceback.tb_lineno
                logger.error("%s||||%s||||%d||||%d", exception_type, filename, line_number, db_error)    # pylint: disable=line-too-long
                return {
                    "count_fetch": False,
                    "helpText": f"Exception: {exception_type}||||{filename}||||{line_number}||||{db_error}",    # pylint: disable=line-too-long
                }, 500

        except Exception as db_error:  # pylint: disable=broad-exception-caught
            exception_type, _, exception_traceback = sys.exc_info()
            filename = exception_traceback.tb_frame.f_code.co_filename
            line_number = exception_traceback.tb_lineno
            logger.error("%s||||%s||||%d||||%d", exception_type, filename, line_number, db_error)
            return {
                "count_fetch": False,
                "helpText": f"Exception: {exception_type}||||{filename}||||{line_number}||||{db_error}",    # pylint: disable=line-too-long
            }, 500


    def challenge_creation(self, req_body):
        """function for updating challenge creation date, name and description in challenge table"""
        try:
            # check if the challenge_id is present in challenge table
            challenge_check = self.challenge_count(
                {"challenge_id": req_body["challenge_id"]}
                )[0]['count']

            if challenge_check == 0:
                return {
                        "update": False,
                        "helpText": "Invalid challenge_id"
                    }, 400

            # check if challenge already created
            query = "SELECT creation_timestamp\
                    FROM challenge\
                    WHERE challenge_id = %s;"
            query_data = (
                            req_body["challenge_id"],
                        )

            ret_data = db_return(query, query_data)

            if ret_data[0][0] is not None:
                return {
                        "update": False,
                        "helpText": "Challenge already created"
                    }, 400

            # Queries Formation
            query = ["UPDATE challenge\
                      SET \
                      creation_timestamp = %s,\
                      name = %s,\
                      description = %s\
                      WHERE challenge_id = %s;",]
            query_data = [
                            (
                                req_body["creation_timestamp"],
                                req_body["name"],
                                req_body["description"],
                                req_body["challenge_id"],
                            ),
                        ]

            try:
                res = db_no_return(query, query_data)

                if res == "success":   # pylint: disable=no-else-return
                    return {"update": True}, 201
                else:
                    res.update({"update": False})
                    return res, 400

            except Exception as db_error:  # pylint: disable=broad-exception-caught
                exception_type, _, exception_traceback = sys.exc_info()
                filename = exception_traceback.tb_frame.f_code.co_filename
                line_number = exception_traceback.tb_lineno
                logger.error("%s||||%s||||%d||||%d", exception_type, filename, line_number, db_error)    # pylint: disable=line-too-long
                return {
                    "update": False,
                    "helpText": f"Exception: {exception_type}||||{filename}||||{line_number}||||{db_error}",    # pylint: disable=line-too-long
                }, 500

        except Exception as db_error:  # pylint: disable=broad-exception-caught
            exception_type, _, exception_traceback = sys.exc_info()
            filename = exception_traceback.tb_frame.f_code.co_filename
            line_number = exception_traceback.tb_lineno
            logger.error("%s||||%s||||%d||||%d", exception_type, filename, line_number, db_error)
            return {
                "update": False,
                "helpText": f"Exception: {exception_type}||||{filename}||||{line_number}||||{db_error}",    # pylint: disable=line-too-long
            }, 500


    def view_list(self, req_body=None):
        """function for view-list page for all roles"""
        try:
            # Queries Formation based on request method payload
            if req_body:
                query = """SELECT
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
                                c.initiator_id = %s
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
                            """
                query_data = (
                                req_body["initiator_id"],
                            )
            else:
                query = """SELECT
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
                            """
                query_data = None

            try:
                ret_data = db_return(query, query_data)
                # print ("\n\n\n\n")
                # # print (json.dumps(ret_data,indent=4, default=json_util.default))
                # print (json.dumps(ret_data,indent=4, cls=DjangoJSONEncoder))
                # print ("\n\n{}\n\n".format(ret_data[-1]))
                # print (json.dumps(ret_data[-1],indent=4, cls=DjangoJSONEncoder))
                # print ("\n\n\n\n")
                if ret_data:   # pylint: disable=no-else-return
                    return {"fetch": True,
                            "data": json.loads(
                                            json.dumps(ret_data, cls=DjangoJSONEncoder)
                                            ),
                            "fields": ["challenge_id","initiator_id","initiator_name",
                                       "initiation_timestamp","industry","domain","process",
                                       "creation_timestamp","name","description",
                                       "current_challenge_status", "challenge_status_json",
                                       "contributor_ids","approver_id","approver_name",
                                        "approver_comment"]
                            }, 200
                else:
                    return {"fetch": False,
                            "data": [],
                            "helpText": "No Challenge Found"}, 400

            except Exception as db_error:  # pylint: disable=broad-exception-caught
                exception_type, _, exception_traceback = sys.exc_info()
                filename = exception_traceback.tb_frame.f_code.co_filename
                line_number = exception_traceback.tb_lineno
                logger.error("%s||||%s||||%d||||%d", exception_type, filename, line_number, db_error)    # pylint: disable=line-too-long
                return {
                    "fetch": False,
                    "data": None,
                    "helpText": f"Exception: {exception_type}||||{filename}||||{line_number}||||{db_error}",    # pylint: disable=line-too-long
                }, 500

        except Exception as db_error:  # pylint: disable=broad-exception-caught
            exception_type, _, exception_traceback = sys.exc_info()
            filename = exception_traceback.tb_frame.f_code.co_filename
            line_number = exception_traceback.tb_lineno
            logger.error("%s||||%s||||%d||||%d", exception_type, filename, line_number, db_error)
            return {
                "fetch": False,
                "data": None,
                "helpText": f"Exception: {exception_type}||||{filename}||||{line_number}||||{db_error}",    # pylint: disable=line-too-long
            }, 500
