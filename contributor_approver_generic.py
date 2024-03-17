"""
    this code primarily contains the contributor and approver
    generic funtions to connect python code to PostgreSQL
    database by calling relevant pyscopg2 operation files (CRUD)
"""
import os
import sys
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
file_handler = logging.FileHandler(os.path.join(log_directory, "contributor_approver_generic.log"))
file_handler.setLevel(logging.DEBUG)  # Set the logging level for this handler

# Create a formatter
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
file_handler.setFormatter(formatter)

# Add the file handler to the logger
logger.addHandler(file_handler)


utils = Utils()


class CAG:
    """
       this class primarily contains the contributor and approver
       generic funtions to connect python code to PostgreSQL
       database by calling relevant pyscopg2 operation files (CRUD)
    """
    # def add_contributor(self, req_body):       # pylint: disable=too-many-branches,too-many-return-statements
    #     """function for adding/updating a contributor_id to
    #        contributor_id column in the contributor_approver
    #        table.
    #     """
    #     try:
    #         if req_body["contributor_id"] != "ai_solution@petonic.in":
    #             # check if contributor_id exists
    #             query = "select count(*) from user_signup\
    #                     where email = %s and role = 'contributor';"
    #             query_data = (req_body["contributor_id"],)

    #             contributor_id_count = db_return(query, query_data)

    #             if contributor_id_count[0][0] == 0:
    #                 return {"update": False,
    #                         "helpText": "Invalid contributor_id"}, 400

    #         # check if challenge_id exists
    #         query = "select count(*) from contributor_approver where challenge_id=%s;"
    #         query_data = (req_body["challenge_id"],)

    #         challenge_count = db_return(query, query_data)

    #         if challenge_count[0][0] == 0:
    #             query = ["INSERT INTO contributor_approver (challenge_id, contributor_id)\
    #                      VALUES (%s, ARRAY[%s]);",
    #                      ]
    #             query_data = [ (
    #                             req_body["challenge_id"],
    #                             req_body["contributor_id"],
    #                         ),]

    #             res = db_no_return(query, query_data)

    #             if res == "success":   # pylint: disable=no-else-return
    #                 return {"update": True}, 201
    #             else:
    #                 res.update({"update": False})
    #                 return res, 500

    #         else:
    #             # check if contributor already added for the same challenge
    #             query = "select contributor_id from contributor_approver\
    #                     where challenge_id = %s;"
    #             query_data = (req_body["challenge_id"],)

    #             contributors = db_return(query, query_data)

    #             if contributors[0][0]:
    #                 if req_body["contributor_id"] in contributors[0][0]:       # pylint: disable=no-else-return
    #                     return {"update": False,
    #                             "helpText": "contributor_id already present\
    #                                         for this challenge"}, 400
    #                 else:
    #                     query = ["UPDATE contributor_approver\
    #                             SET contributor_id = ARRAY_APPEND(contributor_id, %s)\
    #                             WHERE challenge_id = %s AND contributor_id IS NOT NULL;",]
    #                     query_data = [ (
    #                                     req_body["contributor_id"],
    #                                     req_body["challenge_id"],
    #                                 ),]

    #                     res = db_no_return(query, query_data)

    #                     if res == "success":   # pylint: disable=no-else-return
    #                         return {"update": True}, 201
    #                     else:
    #                         res.update({"update": False})
    #                         return res, 500
    #             else:

    #                 query = ["UPDATE contributor_approver\
    #                         SET contributor_id = ARRAY_APPEND(contributor_id, %s)\
    #                         WHERE challenge_id = %s;",]
    #                 query_data = [ (
    #                                 req_body["contributor_id"],
    #                                 req_body["challenge_id"],
    #                             ),]

    #                 res = db_no_return(query, query_data)

    #                 if res == "success":   # pylint: disable=no-else-return
    #                     return {"update": True}, 201
    #                 else:
    #                     res.update({"update": False})
    #                     return res, 500

    #     except Exception as db_error:  # pylint: disable=broad-exception-caught
    #         exception_type, _, exception_traceback = sys.exc_info()
    #         filename = exception_traceback.tb_frame.f_code.co_filename
    #         line_number = exception_traceback.tb_lineno
    #         logger.error("%s||||%s||||%d||||%d", exception_type, filename, line_number, db_error)
    #         return {
    #             "update": False,
    #             "helpText": f"Exception: {exception_type}||||{filename}||||{line_number}||||{db_error}",    # pylint: disable=line-too-long
    #         }, 500


    def add_approver(self, req_body):
        """function for adding an approver_id to approver_id
           column in the contributor_approver table
        """
        try:
            # check if approver_id exists
            query = "select count(*) from user_signup\
                    where email = %s and role = 'approver';"
            query_data = (req_body["approver_id"].lower(),)

            approver_id_count = db_return(query, query_data)

            if approver_id_count[0][0] == 0:
                return {"update": False,
                        "helpText": "Invalid approver_id"}, 400

            # check if approver aleady assigned
            query = "select approver_id from contributor_approver where challenge_id=%s;"
            query_data = (req_body["challenge_id"],)

            approver = db_return(query, query_data)
            if  not approver or not approver[0][0]:
                pass
            else:
                return {"update": False,
                        "helpText": "approver_id already assigned"}, 400

            query = ["INSERT INTO contributor_approver (challenge_id, approver_id)\
                        VALUES (%s, %s)\
                        ON CONFLICT (challenge_id) DO UPDATE SET approver_id = %s;",
                    ]
            query_data = [(
                            req_body["challenge_id"],
                            req_body["approver_id"].lower(),
                            req_body["approver_id"].lower(),
                        ),]

            res = db_no_return(query, query_data)

            if res == "success":   # pylint: disable=no-else-return
                return {"update": True}, 201
            else:
                res.update({"update": False})
                return res, 500

        except Exception as db_error:  # pylint: disable=broad-exception-caught
            exception_type, _, exception_traceback = sys.exc_info()
            filename = exception_traceback.tb_frame.f_code.co_filename
            line_number = exception_traceback.tb_lineno
            logger.error("%s||||%s||||%d||||%d", exception_type, filename, line_number, db_error)
            return {
                "update": False,
                "helpText": f"Exception: {exception_type}||||{filename}||||{line_number}||||{db_error}",    # pylint: disable=line-too-long
            }, 500


    def add_approver_comment(self, req_body):
        """function for adding approver's comment to
           contributor_approver table corresponding
           to a challenge_id
        """
        try:
            # check if approver_id is correct (assigned to the corresponding challenge)
            query = "select approver_id,approver_comment from\
                     contributor_approver where challenge_id=%s;"
            query_data = (req_body["challenge_id"],)

            approver_details = db_return(query, query_data)
            if  not approver_details or not approver_details[0][0] or\
            approver_details[0][0] != req_body["approver_id"].lower()\
            or approver_details[0][1]:
                return {"update": False,
                        "helpText": "Invalid challenge_id/approver_id,\
                            or approver comment already set"}, 400

            query = ["UPDATE contributor_approver\
                     SET approver_comment = %s\
                     WHERE challenge_id = %s;",
                    ]
            query_data = [(
                            req_body["approver_comment"],
                            req_body["challenge_id"],
                        ),]

            res = db_no_return(query, query_data)

            if res == "success":   # pylint: disable=no-else-return
                return {"update": True}, 201
            else:
                res.update({"update": False})
                return res, 500

        except Exception as db_error:  # pylint: disable=broad-exception-caught
            exception_type, _, exception_traceback = sys.exc_info()
            filename = exception_traceback.tb_frame.f_code.co_filename
            line_number = exception_traceback.tb_lineno
            logger.error("%s||||%s||||%d||||%d", exception_type, filename, line_number, db_error)
            return {
                "update": False,
                "helpText": f"Exception: {exception_type}||||{filename}||||{line_number}||||{db_error}",    # pylint: disable=line-too-long
            }, 500
