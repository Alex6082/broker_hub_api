from broker_hub_api.base_api import CommonBrokerHubApi


class LenderApi(CommonBrokerHubApi):
    def send_decision(self, uid, decision: str):
        """
        Obtaining a decision to issue a loan from lender, after lender send request
        """

        decision = decision.lower()
        if decision not in ["approved", "rejected"]:
            raise ValueError('Decision may be be either "approved" or "rejected"')

        data = dict(
            uid=uid,
            decision=decision
        )
        return self.post('/lender/set_loan_request_decision/', data=data)

    def send_ready_to_issue(self, uid, processed_result):
        """
        Receiving a response on the result of loan processing
        """

        processed_result = processed_result.lower()
        if processed_result not in ["signed", "client_refusal"]:
            raise ValueError('Processed result may be be either "signed" or "client_refusal"')

        data = dict(
            uid=uid,
            processed_result=processed_result
        )
        return self.post('/lender/loan_processed_callback/', data=data)
