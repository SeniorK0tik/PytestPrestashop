import os, requests, json, base64
from configuration.structions import root_dir
from configuration.ui import get_ui_config
from utils.logger_loguru.logger import logger


def send_to_allure():
    config = get_ui_config()
    allure_results_directory = root_dir.joinpath(*config.allure.results_path)
    # This url is where the Allure container is deployed. We are using localhost as example
    allure_server = config.allure.url
    # Project ID according to existent projects in your Allure container - Check endpoint for project creation >> `[POST]/projects`
    project_id = config.allure.project_id
    logger.info('RESULTS DIRECTORY PATH: {}'.format(allure_results_directory))
    files = os.listdir(allure_results_directory)

    logger.info('FILES:')
    results = []
    for file in files:
        result = {}

        file_path = allure_results_directory.joinpath(file)
        logger.info('ALLURE FILEPATH: {}'.format(file_path))

        if os.path.isfile(file_path):
            try:
                with open(file_path, "rb") as f:
                    content = f.read()
                    if content.strip():
                        b64_content = base64.b64encode(content)
                        result['file_name'] = file
                        result['content_base64'] = b64_content.decode('UTF-8')
                        results.append(result)
                    else:
                        logger.info('Empty File skipped: {}'.format(file_path))
            finally:
                f.close()
        else:
            logger.info('Directory skipped: {}'.format(file_path))

    headers = {'Content-type': 'application/json'}
    request_body = {
        "results": results
    }
    json_request_body = json.dumps(request_body)

    ssl_verification = True

    logger.info("------------------SEND-RESULTS------------------")
    response = requests.post(
        allure_server + '/allure-docker-service/send-results?project_id=' + project_id,
        headers=headers,
        data=json_request_body,
        verify=ssl_verification
    )

    logger.info("STATUS CODE: {}".format(response.status_code))
    json_response_body = json.loads(response.content)
    json_prettier_response_body = json.dumps(json_response_body, indent=4, sort_keys=True)
    logger.info("RESPONSE: {}".format(json_prettier_response_body))
    logger.info("------------------SUCCESS------------------")

    # If you want to generate reports on demand use the endpoint `GET /generate-report` and disable the Automatic Execution >> `CHECK_RESULTS_EVERY_SECONDS: NONE`
    logger.info("------------------GENERATE-REPORT------------------")
    execution_name = 'prestashop test'
    execution_from = 'http://localhost.com'
    execution_type = 'automated'
    response = requests.get(allure_server + '/allure-docker-service/generate-report?project_id=' + project_id + '&execution_name=' + execution_name + '&execution_from=' + execution_from + '&execution_type=' + execution_type, headers=headers, verify=ssl_verification)
    logger.info("STATUS CODE: {}".format(response.status_code))
    logger.info("RESPONSE: {}".format(response.content))
    json_prettier_response_body = json.dumps(json_response_body, indent=4, sort_keys=True)
    logger.info(json_prettier_response_body)
    logger.info('ALLURE REPORT URL: {}'.format(json.loads(response.content)['data']['report_url']))
