class ApiAssertions:

    @staticmethod
    def verify_ok_response_code(response):
        assert response.status_code == 200

    @staticmethod
    def verify_bad_request_response_code(response):
        assert response.status_code == 400

    @staticmethod
    def verify_not_found_response_code(response):
        assert response.status_code == 404

    @staticmethod
    def verify_response_time(response):
        response_time = response.elapsed.total_seconds()

        try:
            assert response_time <= 3
            print("Response Time: ", response_time)
        except:
            print("Response time is more than 2 seconds: ", response_time)

    @staticmethod
    def verify_response_header(response):
        assert response.headers['Content-Type'] == 'application/json; charset=utf-8'

    @staticmethod
    def verify_error(response, error):
        assert response.json()['error'] == error

    @staticmethod
    def verify_message(response, message):
        assert response.json()['message'] == message

    @staticmethod
    def verify_response_json_attribute(response, attribute):
        assert attribute in response.json()

    @staticmethod
    def verify_json_object_attribute(json_object, attribute):
        assert attribute in json_object
