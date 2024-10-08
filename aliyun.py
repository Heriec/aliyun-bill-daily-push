import os

from typing import List

from alibabacloud_bssopenapi20171214.client import Client as BssOpenApi20171214Client
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_bssopenapi20171214 import models as bss_open_api_20171214_models
from alibabacloud_tea_util import models as util_models
from alibabacloud_tea_util.client import Client as UtilClient


class AliyunClient:
    def __init__(self):
        pass

    def create_client(self) -> BssOpenApi20171214Client:
        """
        使用AK&SK初始化账号Client
        @return: Client
        @throws Exception
        """
        config = open_api_models.Config(
            access_key_id=os.environ['ALIBABA_CLOUD_ACCESS_KEY_ID'],
            access_key_secret=os.environ['ALIBABA_CLOUD_ACCESS_KEY_SECRET']
        )
        config.endpoint = f'business.aliyuncs.com'
        return BssOpenApi20171214Client(config)

    def billList(self, month) -> None:
        client = self.create_client()
        query_bill_request = bss_open_api_20171214_models.QueryBillRequest(
            billing_cycle=month,
            page_size=100
        )
        runtime = util_models.RuntimeOptions()
        try:
            response = client.query_bill_with_options(
                query_bill_request, runtime)
            body = UtilClient.to_map(response.body)
            return body['Data']['Items']['Item']
        except Exception as error:
            print(error.message)
            print(error.data.get("Recommend"))
            UtilClient.assert_as_string(error.message)