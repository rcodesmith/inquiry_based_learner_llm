import unittest
from unittest.mock import patch, Mock
import genai_wb.claude_api as claude_api

CLAUDE_MODEL_VERS = "claude-3-5-sonnet-20240620"

class TestClaudeAPI(unittest.TestCase):

    def setUp(self):
        # Mock out Anthropic API
        self.mock_anthropic = patch('genai_wb.claude_api.Anthropic').start()
        self.mock_anthropic_instance = self.mock_anthropic.return_value

        #self.mock_anthropic_instance = MockAnthropic.return_value
        self.mock_messages = self.mock_anthropic_instance.messages = Mock()
        self.mock_create = Mock()

        self.mock_messages.create = self.mock_create

        # Call the function you wish to test (replace 'function_using_anthropic' with the actual function name)
        self.genai = claude_api.GenAI()

        self.system_msg = "you are a...."

    def test_messages_create_basic_user_text(self):

        # Set up the return value for create()
        self.mock_create.return_value = Mock(content=[Mock(text="Mocked response")])
        
        resp_msg, messages = self.genai.messages_create(self.system_msg, user_text="what is the meaning of life?")

        self.mock_create.assert_called_once_with(model=CLAUDE_MODEL_VERS, max_tokens=2048, 
                                            system=self.system_msg, 
                                            messages=[{"role": "user", "content": "what is the meaning of life?"}],
                                            temperature=1.0)

        resp_txt = claude_api.extract_text(resp_msg)
        
        self.assertEqual(resp_txt, "Mocked response")

        self.assertEqual(1, len(messages))
        
    def test_messages_create_both_message_and_user_text_error(self):
        with self.assertRaises(ValueError):
            self.genai.messages_create("system", message={"role": "user", "content": "message"}, user_text="user_text")

    def test_messages_create_message_basic(self):
        # Set up the return value for create()
        self.mock_create.return_value = Mock(content=[Mock(text="Mocked response2")])
        
        resp_msg, messages = self.genai.messages_create(self.system_msg, message={"role":"user", "content": "what is the meaning of life again?"},
                                              messages=[{"role": "assistant", "content": "42"}],
                                              temperature=0.0)

        self.mock_create.assert_called_once_with(model=CLAUDE_MODEL_VERS, max_tokens=2048, 
                                            system=self.system_msg, 
                                            messages=[{"role": "assistant", "content": "42"},
                                                      {"role": "user", "content": "what is the meaning of life again?"}],
                                            temperature=0.0)

        resp_txt = claude_api.extract_text(resp_msg)
        
        self.assertEqual(resp_txt, "Mocked response2")

        self.assertEqual(2, len(messages))


if __name__ == '__main__':
    unittest.main()