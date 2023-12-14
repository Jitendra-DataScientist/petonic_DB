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
    def challenge_initiation(self, req_body):
        """function for challenge initiation (an entry added in challenge table)"""
        try:
            # challenge_id for this new challenge would be 1 plus
            # the count of challenges created by the same initiator
            challenge_id = self.challenge_count(
                {"initiator_id": req_body["initiator_id"]}
                )[0]['count'] + 1

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
            if "initiator_id" in req_body:
                query = "select count(*) from challenge where initiator_id=%s;"
                query_data = (
                                req_body["initiator_id"],
                            )
            else:
                query = "select count(*) from challenge where challenge_id=%s;"
                query_data = (
                                req_body["challenge_id"],
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
