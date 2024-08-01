"""
    this code primarily contains the
    functions related to leaderboard
"""
import os
import sys
import logging
import json
import time
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
file_handler = logging.FileHandler(os.path.join(log_directory, "leaderboard.log"))
file_handler.setLevel(logging.DEBUG)  # Set the logging level for this handler

# Create a formatter
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
file_handler.setFormatter(formatter)

# Add the file handler to the logger
logger.addHandler(file_handler)


utils = Utils()


class Leaderboard:
    """
        this class primarily contains the
        functions related to subscription
    """


    def best_project(self, req_body):
        """function to return the details of approved challenges
           for projects (for leaderboard page).
        """

        try:
            query = """ select ca.challenge_id, ca.contributor_approver_json,cs.challenge_status_json
                        from contributor_approver ca
                        left join challenge ch
                        on ch.challenge_id = ca.challenge_id
                        left join challenge_status cs
                        on ch.challenge_id = cs.challenge_id
                        left join user_login ul
                        on ch.initiator_id=ul.email
                        where ul.subscription_id=%s
                        and cs.challenge_status='PC';"""
            query_data = (
                req_body["subscription_id"],
            )

            res = db_return(query, query_data)
            ret_data = {}
            if res:
                for element in res:
                    for cont_id in element[1]:
                        if "approved" in element[1][cont_id][0]:
                            if element[1][cont_id][0]["approved"]:
                                if element[0] in ret_data:
                                    ret_data[element[0]]["contributor_ids"].append(cont_id)
                                else:
                                    ret_data[element[0]] = {"contributor_ids":[cont_id],"status_json":element[2]}

                query = """ select us.f_name, us.l_name, us.email, ch.challenge_id, ch.name
                            from user_signup us
                            left join user_login ul
                            on ul.email=us.email
                            left join challenge ch
                            on ch.initiator_id=ul.email
                            where challenge_id in %s;"""
                query_data = (
                    tuple(ret_data.keys()),
                )

                res1 = list(set(db_return(query, query_data)))
                mapping_dict = {element[3]:{"inititator_name":element[0]+" "+element[1],"inititator_email":element[2],"challenge_name":element[4]} for element in res1}

                for ch_id in ret_data:
                    ret_data[ch_id].update(mapping_dict[ch_id])

                contributor_ids = []
                for value in ret_data.values():
                    contributor_ids.extend(value['contributor_ids'])

                query = """ select us.f_name, us.l_name, us.email
                            from user_signup us
                            left join user_login ul
                            on ul.email=us.email
                            where us.email in %s
                            and ul.subscription_id = %s;"""
                query_data = (
                    tuple(set(contributor_ids)),
                    req_body["subscription_id"],
                )

                res2 = list(set(db_return(query, query_data)))

                mapping_dict1 = {element[2]: element[0]+" "+element[1] for element in res2}
                for ch_id in ret_data:
                    ret_data[ch_id]['contributor_names'] = [mapping_dict1[cont_id] for cont_id in ret_data[ch_id]["contributor_ids"]]

                ret_data = dict(sorted(ret_data.items(), key=lambda item: item[1]['status_json']['PC'], reverse=True))
            
            
            return {"fetch": True,
                    "data": ret_data}, 200

        except Exception as db_error:  # pylint: disable=broad-exception-caught
            exception_type, _, exception_traceback = sys.exc_info()
            filename = exception_traceback.tb_frame.f_code.co_filename
            line_number = exception_traceback.tb_lineno
            logger.error("%s||||%s||||%s", exception_type, filename, line_number)
            return {
                "fetch": False,
                "helpText": f"Exception: {exception_type}||||{filename}||||{line_number}||||{db_error}"    # pylint: disable=line-too-long
            }, 500


if __name__ == "__main__":
    inst = Leaderboard()
    print(json.dumps(inst.best_project({"subscription_id": "RfxC5qfaff_automail.petonic@gmail.com"}),indent=4))
