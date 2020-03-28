#封装通用断言函数
def assert_common_uitls(self,
                        response,
                        http_code,
                        success,
                        code,
                        message):
    # self：是从测试脚本中传入的测试类，继承了unittest.TestCase
    # response：也是从测试脚本中传入的响应数据
    # http_code,success,code,message4个是预期要断言的响应状态码、success的值、code和message的值
    self.assertEqual(http_code,response.status_code)
    #与用例中文档的预期响应状态码进行比较断言
    self.assertEqual(success,response.json().get("success")) # 与用例文档中的预期json数据中的success的值进行比较
    self.assertEqual(code, response.json().get("code")) # 与用例文档中预期json数据中的code进行比较
    self.assertIn(message, response.json().get(",essage")) # 与用例文档中预期的json数据中的message进行比较
