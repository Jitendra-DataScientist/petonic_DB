"""
    this code primarily contains the challenge json related
    funtions to connect python code to PostgreSQL database
    by calling relevant pyscopg2 operation files (CRUD)
"""
import sys
import json
import logging
from db_return import db_return
from db_no_return import db_no_return
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


class CJ:
    """
       this class primarily contains the challenge json related
       funtions to connect python code to PostgreSQL database by
       calling relevant pyscopg2 operation files (CRUD)
    """
    def update_challenge_json(self, req_body):
        """function adding/updating an entry in the challenge_json_data table"""
        try:
            # Queries Formation
            query = [
                        "INSERT INTO challenge_json_data (challenge_id, challenge_json)\
                        VALUES (%s, %s)\
                        ON CONFLICT (challenge_id) DO UPDATE SET challenge_json = %s;",
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


    def fetch_challenge_json(self, req_body):
        """function for fetchting an entry from the challenge_json_data table"""
        try:
            query = "select * from challenge_json_data where challenge_id=%s;"
            query_data = (req_body["challenge_id"],)

            try:
                res = db_return(query, query_data)

                try:
                    return {"fetch": True,
                            "json_data": res[0][0]}, 200
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
