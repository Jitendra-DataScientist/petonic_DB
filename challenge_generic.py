"""
    this code primarily contains the generic challenge related
    funtions to connect python code to PostgreSQL database by
    calling relevant pyscopg2 operation files (CRUD)
"""
import sys
import logging
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


class CG:
    """
       this class primarily contains the generic challenge related
       funtions to connect python code to PostgreSQL database by
       calling relevant pyscopg2 operation files (CRUD)
    """
    def challenge_creation(self, req_body):
        """function for challenge creation (an entry in challenge table)"""
        try:
            # Queries Formation
            query = ["INSERT INTO challenge\
                     (challenge_id, initiator_id, date,\
                     industry, process, domain, background)\
                     VALUES (%s, %s,%s,%s,%s,%s,%s);",]
            query_data = [
                            (
                                req_body["challenge_id"],
                                req_body["initiator_id"],
                                req_body["date"],
                                req_body["industry"],
                                req_body["process"],
                                req_body["domain"],
                                req_body["background"]
                            ),
                        ]

            try:
                res = db_create_update(query, query_data)

                if res == "success":   # pylint: disable=no-else-return
                    return {"creation": True}, 201
                else:
                    logger.warning("challenge_id already present")
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
            query = "select count(*) from challenge where initiator_id=%s;"
            query_data = (
                            req_body["initiator_id"],
                        )

            try:
                ret_data = db_read(query, query_data)

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
