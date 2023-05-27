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
        body = ("**" + response_json['question'] + "**" +
            "\n(Context)[" + source_file + "]" +
            "\nA: " + response_json['answer1'] +
            "\n<details><summary>...</summary>" +
            "\n_Explanation: " + response_json['explanation1'] + "_" +
            "\n</details>" +
            "\nB: " + response_json['answer2'] +
            "\n<details><summary>...</summary>" +
            "\n_Explanation: " + response_json['explanation2'] + "_" +
            "\n</details>" +
            "\nC: " + response_json['answer3'] +
            "\n<details><summary>...</summary>" +
            "\n_Explanation: " + response_json['explanation3'] + "_" +
            "\n</details>")
        body = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."

        print(f"::set-output name=title::{title}")
        print(f"::set-output name=body::{body}")

if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2:])
 
