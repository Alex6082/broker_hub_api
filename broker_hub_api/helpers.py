from hashlib import sha1


def get_signature(secret_key: str, params: dict):
    """
    Generate signature from secret_key and post params
    :param secret_key: secret key
    :param params: post params
    :return: signature string
    """
    data = [secret_key]
    data.extend(
        [str(params[key]) for key in sorted(iter(params.keys()))
         if params[key] != '' and not params[key] is None]
    )
    return sha1('|'.join(data).encode('utf-8')).hexdigest()


def is_signature_valid(data: dict, secret_key: str):
    """
    Verify data and secret_key by signature check
    :param data: post params
    :param secret_key: secret key
    :return: bool - is signature valid
    """
    result_signature = data.pop('signature', None)
    if not result_signature:
        raise ValueError('Incorrect data')
    signature = get_signature(secret_key=secret_key, params=data)
    return result_signature == signature
