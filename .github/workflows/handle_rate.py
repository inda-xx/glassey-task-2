import os
import sys
import openai
import json

def main(key, readme_path, compile_path, tests_path):
    openai.api_key = key
    
    # Concatenate all java files found in repo
    all_source_code = ""
    for source_file in sys.stdin:
        source_file = source_file.strip("./")
        source_file = source_file.strip()
        with open(source_file, 'r') as file:
            all_source_code += file.read()
            
    with open(readme_path, 'r') as file:
        readme = file.read()
    
    with open(compile_path, 'r') as file:
        compile_output = file.read()
        if compile_output == "":
            compile_output = "The code compiled sucessfully."
    
    with open(tests_path, 'r') as file:
        tests_output = file.read()
        
    # Call openai api to generate question
    # See: https://platform.openai.com/docs/guides/chat/introduction for more information on the call
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are a teacher that wants to help a student by giving them a grading decision on their work."},
            {"role": "assistant", "content": "Here is all of the source code they have submitted so far in their task:"},
            {"role": "assistant", "content": all_source_code},
            {"role": "assistant", "content": "First, we have the results of running the Java Compiler:"},
            {"role": "assistant", "content": compile_output},
            {"role": "assistant", "content": "Second, we have the results of running the unit tests:"},
            {"role": "assistant", "content": tests_output},
            {"role": "assistant", "content": "Together, the compiler output and unit tests give us an objective measure of the code.},
            {"role": "assistant", "content": "Finally, here is the task they are attempting to complete.},
            {"role": "assistant", "content": readme},
            {"role": "assistant", "content": "Provide a decision for each exercise if they have managed to satisfy it or not, based on their source code, compilation status and unit tests."},
            {"role": "assistant", "content": "Format the decisions as a list with each exercise as an item, followed by the decision feedback"},
            {"role": "assistant", "content": "Finally, provide a grading decision as Looks good to me, or, Needs more work, with an appropriate emojii"},
            {"role": "assistant", "content": "The response should be formatted in markdown format"},
        ]
    )
    fix_apostrophe = response.choices[0]['message']['content'].replace("\'","'")
    remove_quotes = json.dumps(fix_apostrophe)[1:-1]
    print(remove_quotes)
    
if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])
 
