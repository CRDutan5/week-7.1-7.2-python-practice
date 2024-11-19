# : Import the necessary modules
# Define strategic prompts such as system instructions, few shot examples, and topic keywords
# Define functions to declare any plant assistant functions
# from dotenv import load_dotenv
# import google.generativeai as genai
from dotenv import load_dotenv
import google.generativeai as genai
import os

# Study DSA/Algorithms Assistant

load_dotenv()

api_key = os.getenv("API_KEY")
os.environ['API_KEY'] = api_key
genai.configure(api_key=os.environ['API_KEY'])

system_instructions = "You are a Data Structures and Algorithms tutor. Your role is to help the user practice and get better at these types of coding questions. Follow these guidelines: 1. If the user wants to learn more about a concept, data structure or algorithm go into depth and explain it to them, this doesnt count as a coding question. 2. When asked to solve a coding question always try to first guide the user by giving them a hint instead of giving the solution to the problem immediately. If the user has gotten to 3 hints, then and only then you can give the answer. 3. If the question is not related to the Data Structures, Algoritms or Coding suggest them to ask a different question related to those topics. 4. When the user gives you their answer to a coding question revise it and suggest common industry practices in their code, an example is naming their functions specifically with what the function does. 5. When giving a coding question and potential solution review it and see if its correct, if it is motivate them and acknowledge how they got to their answer, else give hints for them to get to the correct answer. 6. When asked for a coding question dont immediately give hints, refer to guideline 2"

def get_completion(prompt, model = "gemini-1.5-flash", **kwargs):
    model = genai.GenerativeModel(model)

    if system_instructions:
        prompt = f"{system_instructions}\n\n{prompt}"

    generation_config = {
        "temperature": 0.7,
        "max_output_tokens": 1000
    }

    generation_config.update(kwargs)

    response = model.generate_content(prompt, generation_config=generation_config)
    return response.text

# prompt = "Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target. You may assume that each input would have exactly one solution, and you may not use the same element twice. You can return the answer in any order."


def main():
    def get_user_input(prompt_message):
        return input(f"{prompt_message}\n> ")
    
    def handle_response(user_input):
        try:
            response = get_completion(user_input)
            print(f"\nDSA Tutor:\n{response}\n")
        except Exception as e:
            print(f"Error: {e}")
    
    print("Hello, I am your DSA Tutor. How can I help you? Type 'Quit' to Exit.\n")

    while True:
        user_input = get_user_input("Enter your prompt")
        if user_input.strip().lower() == "quit":
            print("Goodbye! Happy coding!")
            break
        handle_response(user_input)


if __name__ == "__main__":
    main()