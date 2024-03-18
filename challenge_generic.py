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
import re
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


def remove_special_characters(text):
    """function to remove spaces and special characters from a string"""
    # Define the pattern to match special characters and whitespaces
    pattern = r'[^a-zA-Z0-9]'  # This pattern matches anything that is not alphanumeric

    # Use the sub() function to replace all matches of the pattern with an empty string
    clean_text = re.sub(pattern, '', text)

    return clean_text


class CG:
    """
       this class primarily contains the generic challenge related
       funtions to connect python code to PostgreSQL database by
       calling relevant pyscopg2 operation files (CRUD)
    """

    def challenge_initiation(self, req_Body):  # pylint: disable=too-many-locals
        """function for challenge initiation (an entry added in challenge table)"""
        try:
            req_body = req_Body.copy()
            req_body['initiator_id'] = req_body['initiator_id'].lower()
            # try:
            #     challenge_id = self.challenge_count("max_of_ch_id")[0]['count'] + 1
            # except TypeError:
            #     challenge_id = 1
            # try:
            prefix = remove_special_characters(req_body["industry"])[:3]
            query = "SELECT challenge_id FROM challenge WHERE LEFT(industry, 3) = %s;"
            query_data = (prefix,)
            ch_ids = db_return(query, query_data)
            ch_ids = [item[0] for item in ch_ids]
            prefix = prefix.upper()
            # ch_ids_split = [element.split(prefix) for element in ch_ids]
            cleaned_list = [num.replace(prefix, "") for num in ch_ids]
            filtered_list = [int(element) for element in cleaned_list if element.isdigit()]
            # postfix = str(self.challenge_count(
            #     {"industry_domain_process_specific": req_body["industry"]}
            #     )[0]['count'])
            if filtered_list:
                postfix = str(max(filtered_list) + 1)
            else:
                postfix = '0'
            if len(postfix)>2:
                pass
            elif len(postfix)>1:
                postfix = '0' + postfix
            else:
                postfix = '00' + postfix
            challenge_id = prefix + postfix
            # except:  # pylint: disable=bare-except
            #     challenge_id = utils.generate_random_string(6)

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
                    try:
                        utils.send_mail_trigger_ch_init(
                                req_body["initiator_id"],
                                challenge_id,
                                req_body["industry"],
                                req_body["process"],
                                req_body["domain"],
                            )
                        return {"creation": True,
                                "challenge_id": challenge_id}, 201
                    except Exception as mail_error:  # pylint: disable=broad-exception-caught
                        return {"creation": True,
                                "challenge_id": challenge_id,
                                "helpText": f"failed to send mail: {mail_error}"}, 207

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


    def challenge_count(self, req_Body):
        """function for counting the number of
           challenges corresponding to a user_id
        """
        try:
            req_body = req_Body.copy()
            req_body['initiator_id'] = req_body['initiator_id'].lower()
            # Queries Formation
            # if req_body == "max_of_ch_id":
            #     query = "select max(challenge_id) from challenge;"
            #     query_data = None
            if "industry_domain_process_specific" in req_body:
                # query = "select count(*) from challenge where industry=%s;"
                # query_data = req_body["industry_domain_process_specific"]
                query = f"""SELECT count(*) from challenge
                            WHERE industry='{req_body['industry_domain_process_specific']}';"""
                query_data = None
            elif "initiator_id" in req_body:
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


    def challenge_creation(self, req_body):  # pylint: disable=too-many-return-statements
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
            query = "SELECT creation_timestamp, initiator_id\
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
                    try:
                        query = "SELECT email\
                                FROM user_signup\
                                WHERE role = 'contributor';"
                        cont_list = db_return(query, None)
                        utils.send_mail_trigger_ch_sub(
                                ret_data[0][1],
                                req_body["challenge_id"],
                                req_body["name"],
                                req_body["description"],
                                cont_list,
                            )
                        return {"update": True}, 201
                    except Exception as mail_error:  # pylint: disable=broad-exception-caught
                        return {"update": True,
                                "helpText": f"failed to send mail: {mail_error}"}, 207
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

    def view_list(self, req_Body=None):
        """function for view-list page for all roles"""
        try:
            if req_Body:
                req_body = req_Body.copy()
                if "initiator_id" in req_body and req_body['initiator_id']:
                    req_body['initiator_id'] = [item.lower() for item in req_body['initiator_id']]
                if "approver_id" in req_body and req_body['approver_id']:
                    req_body['approver_id'] = [item.lower() for item in req_body['approver_id']]
            else:
                req_body = None
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
                # if cont_list:
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
                cont_name_dict["ai_solution"] = "GenAI Solution"
                modified_ret_data = [element+(list(map(
                                    lambda x: cont_name_dict[x] if x else None,element[-4]
                                            )),)
                                        for element in ret_data]

                    # Sameer Sir's suggestion:
                    # modified_ret_data = [
                    #                         element + (
                    #                             list(map(
                    #                                 lambda x: cont_name_dict.get(x, x) if
                    #                                 isinstance(x, str) else None,
                    #                                 [email if email != 'ai_solution' else
                    #                                 'ai_solution@petonic.in' for email in
                    #                                   element[-4]]
                    #                             )),
                    #                         )
                    #                         for element in ret_data
                    #                     ]
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
                                       "pm_id", "pm_tool","pm_name",
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
