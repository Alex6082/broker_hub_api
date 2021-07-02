class ServiceError(Exception):
    """
    If response code not in (200, 201).
    """

    def __init__(self, status, response_data):
        self.status = status
        self.response_data = response_data

    def __str__(self):
        return "BrokerHub ServiceError: Response code is %s. Response data: %s" % (self.status, self.response_data)
