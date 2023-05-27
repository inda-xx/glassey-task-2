import os
import sys
import openai
import json

def main(key, files):
    openai.api_key = key
    for source_file in files:
        source_file = source_file.strip("./")
        source_file = source_file.strip()
        with open(source_file, 'r') as file:
            source_code = file.read()
        prompt = "Given the following student source code, generate a multiple choice question about the code to test understanding of the code. The question should have three answer options and explanations for each answer option.\n\n"
    
        # Call openai api to generate question
        # See: https://platform.openai.com/docs/guides/chat/introduction for more information on the call
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are a teacher that wants to help a student understand their programming assignment."},
                {"role": "assistant", "content": prompt + source_code},
                {"role": "assistant", "content": "The response should be formatted as a json object with the following fields: question, answer1, answer2, answer3, explanation1, explanation2, explanation3."},
            ]
        )
        # Extract the question from the response
        question = response.choices[0]['message']['content']

        # Parse json object from response
        response_json = json.loads(question)

        # Open issue on the repository with the question
        title = "🤖 Question about code!"
        body = "**A**\\n<h1>B</h1>\\n<strong>C</strong>"

        print(f"::set-output name=title::{title}")
        print(f"::set-output name=body::{body}")

if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2:])
 
