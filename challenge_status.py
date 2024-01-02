"""
    this code primarily contains the challenge status related
    funtions to connect python code to PostgreSQL database by
    calling relevant pyscopg2 operation files (CRUD)
"""
import sys
import time
import logging
import json
from db_read import db_read
from db_create_update import db_create_update
from utils import Utils


# Configure logging
logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    handlers=[logging.StreamHandler()],
)

# Create a logger instance
logger = logging.getLogger(__name__)


utils = Utils()


class CS:
    """
       this class primarily contains the challenge status related
       funtions to connect python code to PostgreSQL database by
       calling relevant pyscopg2 operation files (CRUD)
    """
    def update_challenge_status(self, req_body):
        """function adding/updating an entry in the challenge_status table"""
        try:
            # read the json (if present) for the corresponding
            # challenge_id from challenge_status table
            query = "select json_data from challenge_status where challenge_id=%s;"
            query_data = (req_body["challenge_id"],)
            json_res = db_read(query, query_data)

            # Queries Formation
            # query = [
            #     "INSERT INTO challenge_status (challenge_id, challenge_status, json_data) \
            #     VALUES (%s, %s, jsonb_build_object(%s, %s)) \
            #     ON CONFLICT (challenge_id) DO UPDATE \
            #     SET challenge_status = %s, \
            #     json_data = jsonb_build_object(%s, %s);",
            # ]
            # query_data = [
            #     (
            #         req_body["challenge_id"],
            #         req_body["challenge_status"],
            #         req_body["challenge_status"],
            #         time.time(),
            #         req_body["challenge_status"],
            #         req_body["challenge_status"],
            #         time.time(),
            #     )
            # ]

            if json_res and json_res[0][0] is not None:
                json_res[0][0].update({req_body["challenge_status"]: time.time()})
                query = [
                    "UPDATE challenge_status \
                    SET challenge_status = %s, \
                    json_data = %s \
                    WHERE challenge_id = %s;",
                ]
                query_data = [
                    (
                        req_body["challenge_status"],
                        json.dumps(json_res[0][0]),
                        req_body["challenge_id"],
                    )
                ]
            else:
                query = [
                    "INSERT INTO challenge_status (challenge_id, challenge_status, json_data) \
                    VALUES (%s, %s, jsonb_build_object(%s, %s)) \
                    ON CONFLICT (challenge_id) DO UPDATE \
                    SET challenge_status = %s, \
                    json_data = jsonb_build_object(%s, %s);",
                ]
                query_data = [
                    (
                        req_body["challenge_id"],
                        req_body["challenge_status"],
                        req_body["challenge_status"],
                        time.time(),
                        req_body["challenge_status"],
                        req_body["challenge_status"],
                        time.time(),
                    )
                ]

            try:
                res = db_create_update(query, query_data)
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


    def fetch_challenge_status(self,req_body):
        """function fetchting an entry from the challenge_status table"""
        try:
            # Queries Formation
            query = "select challenge_status, json_data from challenge_status where challenge_id=%s;"
            query_data = (req_body["challenge_id"],)

            try:
                res = db_read(query, query_data)

                try:
                    return {"fetch": True,
                            "status": res[0][0],
                            "json_data": res[0][1]}, 200
                except IndexError:
                    return {"fetch": False,
                            "status": None,
                            "json_data": None,
                            "helpText": "challenge_id not found"}, 400

            except Exception as db_error:  # pylint: disable=broad-exception-caught
                exception_type, _, exception_traceback = sys.exc_info()
                filename = exception_traceback.tb_frame.f_code.co_filename
                line_number = exception_traceback.tb_lineno
                logger.error("%s||||%s||||%d||||%d", exception_type, filename, line_number, db_error)    # pylint: disable=line-too-long
                return {
                    "fetch": False,
                    "status": None,
                    "json_data": None,
                    "helpText": f"Exception: {exception_type}||||{filename}||||{line_number}||||{db_error}",    # pylint: disable=line-too-long
                }, 500

        except Exception as db_error:  # pylint: disable=broad-exception-caught
            exception_type, _, exception_traceback = sys.exc_info()
            filename = exception_traceback.tb_frame.f_code.co_filename
            line_number = exception_traceback.tb_lineno
            logger.error("%s||||%s||||%d||||%d", exception_type, filename, line_number, db_error)
            return {
                "fetch": False,
                "status": None,
                "json_data": None,
                "helpText": f"Exception: {exception_type}||||{filename}||||{line_number}||||{db_error}",    # pylint: disable=line-too-long
            }, 500
