from broker_hub_api.base_api import CommonBrokerHubApi


class LenderApi(CommonBrokerHubApi):
    def send_decision(self, uid, decision: str, redirect_url):
        decision = decision.lower()
        if decision not in ["approved", "rejected"]:
            raise ValueError('Decision may be be either "approved" or "rejected"')

        data = dict(
            uid=uid,
            decision=decision,
            redirect_url=redirect_url
        )
        return self.post('/lender/set_loan_request_decision/', data=data)

    def send_ready_to_issue(self, uid, signed, guaranteed, guaranty_data):
        data = dict(
            uid=uid,
            signed=signed,
            guaranteed=guaranteed,
            guaranty_data=guaranty_data,
        )
        return self.post('/lender/loan_processed_callback/', data=data)
