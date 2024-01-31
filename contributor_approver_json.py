"""
    this code primarily contains the contributor and approver
    json related funtions to connect python code to PostgreSQL
    database by calling relevant pyscopg2 operation files (CRUD)
"""
import os
import sys
import json
import logging
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
file_handler = logging.FileHandler(os.path.join(log_directory, "contributor_approver_json.log"))
file_handler.setLevel(logging.DEBUG)  # Set the logging level for this handler

# Create a formatter
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
file_handler.setFormatter(formatter)

# Add the file handler to the logger
logger.addHandler(file_handler)


utils = Utils()


class CAJ:
    """
       this class primarily contains the contributor and approver
       json related funtions to connect python code to PostgreSQL
       database by calling relevant pyscopg2 operation files (CRUD)
    """
    def update_json(self, req_body):
        """function adding/updating an entry in the contributor_approver table"""
        try:
            # Queries Formation
            query = [
                        "INSERT INTO contributor_approver (challenge_id, contributor_approver_json)\
                        VALUES (%s, %s)\
                        ON CONFLICT (challenge_id) DO UPDATE SET contributor_approver_json = %s;",
                ]
            query_data = [
                            (
                                req_body["challenge_id"],
                                json.dumps(req_body["json_data"]),
                                json.dumps(req_body["json_data"])
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


    def fetch_json(self, req_body):
        """function for fetchting an entry from the contributor_approver table"""
        try:
            query = "select * from contributor_approver where challenge_id=%s;"
            query_data = (req_body["challenge_id"],)

            try:
                res = db_return(query, query_data)

                try:
                    return {"fetch": True,
                            "json_data": res[0][2]}, 200
                except IndexError:
                    return {"fetch": False,
                            "json_data": {},
                            "helpText": "challenge_id not found"}, 400

            except Exception as db_error:  # pylint: disable=broad-exception-caught
                exception_type, _, exception_traceback = sys.exc_info()
                filename = exception_traceback.tb_frame.f_code.co_filename
                line_number = exception_traceback.tb_lineno
                logger.error("%s||||%s||||%d||||%d", exception_type, filename, line_number, db_error)    # pylint: disable=line-too-long
                return {
                    "fetch": False,
                    "helpText": f"Exception: {exception_type}||||{filename}||||{line_number}||||{db_error}",    # pylint: disable=line-too-long
                }, 500

        except Exception as db_error:  # pylint: disable=broad-exception-caught
            exception_type, _, exception_traceback = sys.exc_info()
            filename = exception_traceback.tb_frame.f_code.co_filename
            line_number = exception_traceback.tb_lineno
            logger.error("%s||||%s||||%d||||%d", exception_type, filename, line_number, db_error)
            return {
                "fetch": False,
                "helpText": f"Exception: {exception_type}||||{filename}||||{line_number}||||{db_error}",    # pylint: disable=line-too-long
            }, 500


    def contributor_solution_upload(self, req_body):    # pylint: disable=too-many-locals
        """add a contributor solution json to contributor_approver
           table for a specific challenge_id
        """
        try:

            # Retrieving request data
            challenge_id = req_body["challenge_id"]
            contributor_id = req_body["contributor_id"]
            solution_json = req_body["solution_json"]

            # check if challenge_id exists
            # query = "select count(*) from contributor_approver\
            #         where challenge_id = %s;"
            # query_data = (challenge_id,)

            # challenge_id_count = db_return(query, query_data)

            # if challenge_id_count[0][0] == 0:
            #     return {"update": False,
            #             "helpText": "challenge_id not present in \
            #                 contributor_approver table"}, 400

            # check if contributor_id exists
            # query = "select count(*) from contributor_approver\
            #         where challenge_id = %s and %s = ANY(contributor_id);;"
            # query_data = (challenge_id, contributor_id,)

            # contributor_id_count = db_return(query, query_data)

            # if contributor_id_count[0][0] == 0:
            #     return {"update": False,
            #             "helpText": "contributor_id not present for corresponding \
            #                 challenge in contributor_approver table"}, 400


            if req_body["contributor_id"] != "ai_solution@petonic.in":
                # check if contributor_id exists
                query = "select count(*) from user_signup\
                        where email = %s and role = 'contributor';"
                query_data = (req_body["contributor_id"],)

                contributor_id_count = db_return(query, query_data)

                if contributor_id_count[0][0] == 0:
                    return {"update": False,
                            "helpText": "Invalid contributor_id"}, 400

            # Check if the challenge_id exists in the contributor_approver table
            select_query = "SELECT challenge_id FROM contributor_approver WHERE challenge_id = %s;"
            challenge_exists = db_return(select_query, (challenge_id,))

            # If challenge_id doesn't exist, insert a new entry
            if not challenge_exists:
                insert_query = "INSERT INTO contributor_approver \
                                (challenge_id, contributor_approver_json) VALUES (%s, %s);"
                insert_data = (challenge_id, json.dumps({contributor_id: [solution_json]}))
                result = db_no_return([insert_query], [insert_data])
                return ({"update": True}, 201) if result == "success" else ({"update": False}, 500)


            # Fetch existing JSON data
            select_query = "SELECT contributor_approver_json FROM \
                            contributor_approver WHERE challenge_id = %s FOR UPDATE;"
            existing_json = db_return(select_query, (challenge_id,))

            if not existing_json or not existing_json[0] or not existing_json[0][0]:
                # If no existing JSON data found, create a new JSON object
                new_json = json.dumps({contributor_id: [solution_json]})
                update_query = "UPDATE contributor_approver SET \
                                contributor_approver_json = %s WHERE challenge_id = %s;"
                result = db_no_return([update_query], [(new_json, challenge_id)])
            else:
                # Otherwise, update the existing JSON object
                existing_json_dict = existing_json[0][0]
                if contributor_id not in existing_json_dict:
                    existing_json_dict[contributor_id] = [solution_json]
                else:
                    existing_json_dict[contributor_id].append(solution_json)
                updated_json = json.dumps(existing_json_dict)
                update_query = "UPDATE contributor_approver SET \
                                contributor_approver_json = %s WHERE challenge_id = %s;"
                result = db_no_return([update_query], [(updated_json, challenge_id)])

            return ({"update": True}, 201) if result == "success" else ({"update": False}, 500)

        except Exception as db_error:  # pylint: disable=broad-exception-caught
            exception_type, _, exception_traceback = sys.exc_info()
            filename = exception_traceback.tb_frame.f_code.co_filename
            line_number = exception_traceback.tb_lineno
            logger.error("%s||||%s||||%d||||%d", exception_type, filename, line_number, db_error)
            return {
                "update": False,
                "helpText": f"Exception: {exception_type}||||{filename}||||{line_number}||||{db_error}",    # pylint: disable=line-too-long
            }, 500
