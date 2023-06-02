import os
import sys
import openai
import codecs

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
    
    exercise = response.choices[0]['message']['content']
    
    # Set the issue title and body
    title = "🤖 Here is a bonus exercise for you!"
    body = codecs.escape_decode(bytes(exercise, "utf-8"))[0].decode("utf-8")

    print(f"::set-output name=title::{title}")
    print(f"::set-output name=body::{body}")

if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])
