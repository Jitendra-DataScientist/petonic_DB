"""
    this code primarily contains the funtion related to Business
    Scenario Tab's dropdowns to connect python code to PostgreSQL
    database by calling relevant pyscopg2 operation files (CRUD)
"""
import sys
import logging
import pandas as pd
from db_read import db_read
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


# class BSD:
#     """
#        this class primarily contains the funtions related to Business
#        Scenario Tab's dropdowns to connect python code to PostgreSQL
#        database by calling relevant pyscopg2 operation files (CRUD)
#     """
    # def business_scenario_industry_dropdown(self):
    #     """function to fetch data for "Industry" dropdown
    #        under "Business Scenario tab
    #     """

    #     try:
    #         return db_read(query = "select * from industry_list;", query_data = None)

    #     except Exception as db_error:  # pylint: disable=broad-exception-caught
    #         exception_type, _, exception_traceback = sys.exc_info()
    #         filename = exception_traceback.tb_frame.f_code.co_filename
    #         line_number = exception_traceback.tb_lineno
    #         logger.error("%s||||%s||||%s", exception_type, filename, line_number)
    #         return {
    #             "helpText": f"Exception: {exception_type}||||{filename}||||{line_number}||||{db_error}"    # pylint: disable=line-too-long
    #         }


    # def business_scenario_domain_dropdown(self, req_body):
    #     """function to fetch data for "Domain" dropdown
    #        under "Business Scenario tab
    #     """

    #     try:
    #         query = "select domain_id,name\
    #                 from domain_list\
    #                 where industry_id = %s;"
    #         query_data = (req_body["industry_id"],)

    #         return db_read(query, query_data)

    #     except Exception as db_error:  # pylint: disable=broad-exception-caught
    #         exception_type, _, exception_traceback = sys.exc_info()
    #         filename = exception_traceback.tb_frame.f_code.co_filename
    #         line_number = exception_traceback.tb_lineno
    #         logger.error("%s||||%s||||%s", exception_type, filename, line_number)
    #         return {
    #             "helpText": f"Exception: {exception_type}||||{filename}||||{line_number}||||{db_error}"    # pylint: disable=line-too-long
    #         }


    # def business_scenario_process_dropdown(self, req_body):
    #     """function to fetch data for "Process" dropdown
    #        under "Business Scenario tab
    #     """

    #     try:
    #         query = "select process_id,name\
    #                     from process_list\
    #                     where domain_id = %s;"
    #         query_data = (req_body["domain_id"],)

    #         return db_read(query, query_data)

    #     except Exception as db_error:  # pylint: disable=broad-exception-caught
    #         exception_type, _, exception_traceback = sys.exc_info()
    #         filename = exception_traceback.tb_frame.f_code.co_filename
    #         line_number = exception_traceback.tb_lineno
    #         logger.error("%s||||%s||||%s", exception_type, filename, line_number)
    #         return {
    #             "helpText": f"Exception: {exception_type}||||{filename}||||{line_number}||||{db_error}"    # pylint: disable=line-too-long
    #         }


def business_scenario_complete_dropdown():
    """function to fetch data for all dropdowns
        under "Business Scenario tab
    """

    try:
        # data_frame_data = db_read(query = "select il.name as industry,\
        #                         dl.name as domain, pl.name as process\
        #                         from industry_list as il\
        #                         join domain_list as dl\
        #                         on il.industry_id = dl.industry_id\
        #                         join process_list as pl\
        #                         on dl.domain_id = pl.domain_id;",
        #                 query_data = None)

        data_frame_data = db_read(query = "select industry_name,\
                                            domain_name,process_name\
                                            from industry_domain_process_key_parameters;",
                        query_data = None)
        data_frame = pd.DataFrame(
            data_frame_data,
            columns=["Business", "Domain", "Process"],
        )

        data_frame.drop_duplicates(inplace=True)

        dct = {}
        for business in data_frame["Business"].unique():
            dct[business] = {}
        for business in data_frame["Business"].unique():
            data_frame1 = data_frame[data_frame["Business"] == business]
            for domain in data_frame1["Domain"].unique():
                dct[business][domain] = []
        for business in data_frame["Business"].unique():
            data_frame1 = data_frame[data_frame["Business"] == business]
            for domain in data_frame1["Domain"].unique():
                dct[business][domain] = list(
                    data_frame[(data_frame["Business"] == business) &
                            (data_frame["Domain"] == domain)]["Process"]
                )

        return dct

    except Exception as db_error:  # pylint: disable=broad-exception-caught
        exception_type, _, exception_traceback = sys.exc_info()
        filename = exception_traceback.tb_frame.f_code.co_filename
        line_number = exception_traceback.tb_lineno
        logger.error("%s||||%s||||%s", exception_type, filename, line_number)
        return {
            "helpText": f"Exception: {exception_type}||||{filename}||||{line_number}||||{db_error}"    # pylint: disable=line-too-long
        }
