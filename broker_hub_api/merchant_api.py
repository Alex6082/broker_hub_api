from broker_hub_api.base_api import CommonBrokerHubApi


class MerchantApi(CommonBrokerHubApi):
    def cancel_order(self, uid):
        """
        Cancellation of the order (The goods were not delivered to the client)
        """

        data = dict(
            uid=uid
        )
        return self.post('/merchant/cancel_order/', data=data)

    def confirm_order(self, uid):
        """
        Confirmation of delivery of goods to the client
        """

        data = dict(
            uid=uid
        )
        return self.post('/merchant/confirm_order/', data=data)

    def create_loan_request(self, order_id, amount, success_redirect_url, fail_redirect_url, callback_url, products, invoice):
        """
        Creating merchant loan request
        """

        data = dict(
            order_id=order_id,
            amount=amount,
            success_redirect_url=success_redirect_url,
            fail_redirect_url=fail_redirect_url,
            callback_url=callback_url,
            products=products,
            invoice=invoice
        )
        return self.post('/merchant/create_loan_request/', data=data)
