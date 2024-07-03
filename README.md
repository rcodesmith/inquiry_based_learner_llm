# Inquiry based learner

This project demonstrates a technique for building an LLM model which 'learns' via a process of asking a person questions and incorporating
the answers into a knowledge base.  The model is an inquiry-based learner using Anthropic Claude APIs.  The learner
generates questions based on some base information, which a person then answers.  The learner then switches roles and 
answers questions based on the person's answers, in its own words.

See [this blog post](https://medium.com/@rcodesmith/implementing-an-inquiry-based-learning-chatbot-ea5b01d8d364) for a walkthrough and
more information.

## Setup

1. Install the required packages:

```
pip install -r requirements.txt
pip install -r requirements-dev.txt
```

2. Create a `.env` file in the root directory and add your Anthropic API key:

```
ANTHROPIC_API_KEY=your_api_key_here
```

3. Run the Jupyter notebook:

```
# From root directory:
PYTHONPATH=$(pwd)/src:$PYTHONPATH jupyter notebook
```

4. Open one of the notebooks listed under the Workbooks section below, and start running them!

If you're using Vscode, it has a really good [Jupyter notebook mode](https://code.visualstudio.com/docs/datascience/jupyter-notebooks).

## Project Structure

- `notebooks/`: Contains Jupyter notebooks testing and demonstrating usage.
- `src/`: Python helper classes and implementation of learner.
- `tests/`: Unit tests
- `requirements.txt`: Required Python packages.
- `requirements-dev.txt`: Required Python packages for development (unit tests).
- `.env`: Stores the Anthropic API key (not tracked by git).

## Workbooks

- `notebooks/job_candidate_interview_basic_test.ipynb`: Test the model answering questions based on a resume and background information.
- `notebooks/job_candidate_learn_about_candidate.ipynb`: Test the model generating questions as a hiring manager.  Then as an interviewee, being
   able to incorporate the answers into its knowledge base, and answer questions based on them.
- `notebooks/conversation_history_test.ipynb`: Test GenAIConversation and the model's ability to answer questions consistent with past message history.
- `notebooks/inquiry_based_learner_test.ipynb`: Test out the full inquiry-based learner chatbot.