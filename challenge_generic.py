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
from view_list_query_templates import ViewListQueryTemplates
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
view_list_query_templates_instance = ViewListQueryTemplates()

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


    def view_list_query(self, req_body):    # pylint: disable=too-many-branches, too-many-statements
        """
           function for query formation for view-list page
        """
        # Queries Formation based on request method payload
        if req_body:
            where_elements = []
            limit_offset = None

            # set limit and offset
            if req_body['upper_index'] and isinstance(req_body['lower_index'], int):
                if int(req_body['lower_index']) < 1:
                    return "Bad Request. lower_index < 1"
                limit_offset = f"LIMIT {req_body['upper_index']} \
                    OFFSET {req_body['lower_index'] - 1}"
            elif req_body['upper_index']:
                limit_offset = f"LIMIT {req_body['upper_index']}"
            elif isinstance(req_body['lower_index'], int):
                if int(req_body['lower_index']) < 1:
                    return "Bad Request. lower_index < 1"
                limit_offset = f"OFFSET {req_body['lower_index'] - 1}"

            # set WHERE clause - initiator_id
            if req_body['initiator_id']:
                if len(req_body['initiator_id']) == 1:
                    where_elements.append(f"c.initiator_id IN \
                                          {str(tuple(req_body['initiator_id']))[:-2]})")
                else:
                    where_elements.append(f"c.initiator_id IN \
                                          {str(tuple(req_body['initiator_id']))}")

            # set WHERE clause - industry
            if req_body['industry']:
                if len(req_body['industry']) == 1:
                    where_elements.append(f"c.industry IN {str(tuple(req_body['industry']))[:-2]})")
                else:
                    where_elements.append(f"c.industry IN {str(tuple(req_body['industry']))}")

            # set WHERE clause - domain
            if req_body['domain']:
                if len(req_body['domain']) == 1:
                    where_elements.append(f"c.domain IN {tuple(req_body['domain'])[:-2]})")
                else:
                    where_elements.append(f"c.domain IN {tuple(req_body['domain'])}")

            # set WHERE clause - process
            if req_body['process']:
                if len(req_body['process']) == 1:
                    where_elements.append(f"c.process IN {str(tuple(req_body['process']))[:-2]})")
                else:
                    where_elements.append(f"c.process IN {tuple(req_body['process'])}")

            # set WHERE clause - approver_id
            if req_body['approver_id']:
                if len(req_body['approver_id']) == 1:
                    where_elements.append(f"ca.approver_id IN \
                                          {str(tuple(req_body['approver_id']))[:-2]})")
                else:
                    where_elements.append(f"ca.approver_id IN {tuple(req_body['approver_id'])}")

            # set WHERE clause - initiation_start_date and/or initiation_end_date
            if req_body['initiation_start_date'] and req_body['initiation_end_date']:
                where_elements.append(f"c.initiation_timestamp BETWEEN \
                                      '{req_body['initiation_start_date']}' \
                                        AND '{req_body['initiation_end_date']}'")
            elif req_body['initiation_start_date']:
                where_elements.append(f"c.initiation_timestamp >= \
                                      '{req_body['initiation_start_date']}'")
            elif req_body['initiation_end_date']:
                where_elements.append(f"c.initiation_timestamp <= \
                                      '{req_body['initiation_end_date']}'")

            # set WHERE clause - creation_date_null, creation_start_date and/or creation_end_date
            if req_body['creation_date_null']:
                if req_body['creation_start_date'] and req_body['creation_end_date']:
                    where_elements.append(f"(c.creation_timestamp IS NULL OR \
                                          (c.creation_timestamp BETWEEN \
                                          '{req_body['creation_start_date']}' AND \
                                            '{req_body['creation_end_date']}'))")
                elif req_body['creation_start_date']:
                    where_elements.append(f"(c.creation_timestamp IS NULL \
                                          OR (c.creation_timestamp >= \
                                          '{req_body['creation_start_date']}'))")
                elif req_body['creation_end_date']:
                    where_elements.append(f"(c.creation_timestamp IS NULL \
                                          OR (c.creation_timestamp <= \
                                          '{req_body['creation_end_date']}'))")
            else:
                if req_body['creation_start_date'] and req_body['creation_end_date']:
                    where_elements.append(f"c.creation_timestamp BETWEEN \
                                          '{req_body['creation_start_date']}' AND \
                                            '{req_body['creation_end_date']}'")
                elif req_body['creation_start_date']:
                    where_elements.append(f"c.creation_timestamp >= \
                                          '{req_body['creation_start_date']}'")
                elif req_body['creation_end_date']:
                    where_elements.append(f"c.creation_timestamp <= \
                                          '{req_body['creation_end_date']}'")

            # set WHERE clause - status
            if req_body['status']:
                if len(req_body['status']) == 1:
                    where_elements.append(f"cs.challenge_status IN \
                                          {str(tuple(req_body['status']))[:-2]})")
                else:
                    where_elements.append(f"cs.challenge_status IN \
                                          {str(tuple(req_body['status']))}")


            if where_elements and limit_offset:
                query_template = view_list_query_templates_instance.where_limit
                if len(where_elements) == 1:
                    where_clause = where_elements[0]
                else:
                    where_clause = " AND ".join(where_elements[:-1]) + " AND " + where_elements[-1]
                query = query_template % (where_clause, limit_offset)
            elif where_elements:
                query_template = view_list_query_templates_instance.where
                if len(where_elements) == 1:
                    where_clause = where_elements[0]
                else:
                    where_clause = " AND ".join(where_elements[:-1]) + " AND " + where_elements[-1]
                query = query_template % where_clause
            elif limit_offset:
                query_template = view_list_query_templates_instance.limit
                query = query_template % limit_offset
            # elif not where_elements and (not limit and not offset):
            #     return "Bad Request", None
            else:
                return "Bad Request", None
        else:
            query = view_list_query_templates_instance.no_filter
        return query

    # def cont_name_func(self, email_list, mapping_dict):
    #     return [mapping_dict.get(element) for element in email_list]

    def view_list(self, req_body=None):
        """function for view-list page for all roles"""
        try:
            query = self.view_list_query(req_body)
            if query == "Bad Request":
                return {"fetch": False,
                        "helpText": "Bad Request"}, 400
            if query == "Bad Request. lower_index < 1":
                return {"fetch": False,
                        "helpText": "Bad Request. lower_index < 1"}, 400
            try:
                ret_data = db_return(query, query_data = None)
                # print ("\n\n\n\n")
                # print (json.dumps(ret_data,indent=4, default=json_util.default))
                # print (json.dumps(ret_data,indent=4, cls=DjangoJSONEncoder))
                # print ("\n\n\n\n")
                cont_list = [item for sublist in ret_data for item in sublist[-4] if item]
                cont_list = list(set(cont_list))
                modified_ret_data = None
                if cont_list:
                    query = "SELECT email, f_name, l_name FROM user_signup WHERE email IN %s"
                    query_data = (tuple(cont_list),)
                    cont_name_list = db_return(query, query_data)
                    cont_name_dict = {element[0]:element[1]+' '+element[2]
                                      for element in cont_name_list}
                    # modified_ret_data = [element+(self.cont_name_func(
                    #                                     element[-4],cont_name_dict
                    #                                 ),)
                    #                      for element in ret_data]
                    cont_name_dict["ai_solution@petonic.in"] = "GenAI Solution"
                    cont_name_dict["ai_solution@petonic.in"] = "GenAI Solution"
                    print ("\n\n{}\n\n".format(cont_list))
                    print ("\n\n{}\n\n".format(cont_name_dict))
                    # print ("\n\n{}\n\n".format(ret_data[-2]))
                    modified_ret_data = [element+(list(map(
                                        lambda x: cont_name_dict[x] if x else None,element[-4]
                                                )),)
                                         for element in ret_data]
                if modified_ret_data:   # pylint: disable=no-else-return
                    # ret_data = list(map(lambda sublist: list(map(lambda x: None\
                    #          if x ==" " and sublist[-2] == " " else x, sublist)), ret_data))
                    modified_ret_data = list(map(
                                                lambda sublist: list(map(
                                                    lambda x: None if x == " " else x,sublist
                                                    )),
                                                modified_ret_data))
                    return {"fetch": True,
                            "data": json.loads(
                                            json.dumps(modified_ret_data, cls=DjangoJSONEncoder)
                                            ),
                            "fields": ["challenge_id","initiator_id","initiator_name",
                                       "initiation_timestamp","industry","domain","process",
                                       "creation_timestamp","name","description",
                                       "current_challenge_status", "challenge_status_json",
                                       "contributor_ids","approver_id","approver_name",
                                        "approver_comment","contributor_names"]
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
