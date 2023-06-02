import os
import sys
import openai

def main(key, file_path):
    openai.api_key = key

    with open(file_path, 'r') as file:
        readme = file.read()
        
    # Call openai api to generate question
    # See: https://platform.openai.com/docs/guides/chat/introduction for more information on the call
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are a teacher that wants to help a student by extending their programming task with a fun bonus exercise. Here is their overall task:"},
            {"role": "assistant", "content": readme},
            {"role": "assistant", "content": "Provide the next exercise in markdown format."},
        ]
    )
    
    print(response.choices[0]['message']['content'])
    print(response.choices[0]['message']['content'].encode("unicode_escape"))
    
    # Set the issue title and body
    title = "🤖 Here is a bonus exercise for you!"
    body = "blah"

    print(f"::set-output name=title::{title}")
    print(f"::set-output name=body::{body}")

if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])
