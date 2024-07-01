import unittest
from unittest.mock import patch, Mock
import genai_wb.claude_api as claude_api

class TestClaudeAPI(unittest.TestCase):
    @patch('genai_wb.claude_api.Anthropic')
    def test_function_using_anthropic(self, MockAnthropic):
        # Setup the mock
        mock_anthropic_instance = MockAnthropic.return_value
        mock_messages = mock_anthropic_instance.messages = Mock()
        mock_create = Mock()

        mock_messages.create = mock_create

        # Set up the return value for create()
        mock_create.return_value = Mock(content=[Mock(text="Mocked response")])

        
        # Call the function you wish to test (replace 'function_using_anthropic' with the actual function name)
        genai = claude_api.GenAI()
        
        system_msg = "you are a...."
        resp_msg = genai.messages_create(system_msg, user_message="what is the meaning of life?")

        mock_create.assert_called_once_with(model='claude-3-5-sonnet-20240620', max_tokens=2048, 
                                            system=system_msg, 
                                            messages=[{"role": "user", "content": "what is the meaning of life?"}])

        resp_txt = claude_api.extract_text(resp_msg)
        
        self.assertEqual(resp_txt, "Mocked response")
        
if __name__ == '__main__':
    unittest.main()