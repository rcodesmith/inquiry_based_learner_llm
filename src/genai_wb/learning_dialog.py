import json

from genai_wb.genai_conversation import GenAIConversation

QA_JSON_FORMAT = """{
  "questions": [{
      "question": "string",
      "reasoning": "string"
  }]
}"""


class LearningDialog:
    genai_conversation: GenAIConversation
    question_generator_system_prompt: str
    interviewee_system_prompt: str

    # TODO: Specify keys for dict
    qas: list[dict[str, str]]

    interview_messages = []

    def __init__(self, genai_conversation: GenAIConversation, question_generator_system_prompt: str, interviewee_system_prompt: str):
        self.genai_conversation = genai_conversation
        self.question_generator_system_prompt = question_generator_system_prompt
        self.interviewee_system_prompt = interviewee_system_prompt
        self.qas = []

    def generate_question(self, user_text: str):
        response = self.genai_conversation.dialog_json(self.question_generator_system_prompt, user_text, self.qas)

        # TODO: Verify response structure first
        return response[1]['content']['questions']


    def learn_answer_question(self, question: str, answer: str):
        self.qas.append({"question": question, "answer": answer})

    def interview_answer_question(self, question_txt: str):
        system_prompt = self.interviewee_system_prompt % {'learning_qas': json.dumps(self.qas)}
        updated_messages = self.genai_conversation.dialog_text(system_prompt, question_txt, self.interview_messages)
        self.interview_messages = updated_messages

        answer = updated_messages[-1]['content']

        return answer



