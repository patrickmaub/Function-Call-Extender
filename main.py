#!/usr/bin/env python3

#Author: Patrick Mauboussin

import json
from function_call_builder import FunctionCallBuilder

def main_menu():
    """
    Displays the main menu of the application and handles user input to navigate to different functionalities.
    
    The user can choose to select a premade example, input custom details for a function call, or exit the application.
    """
    print("ChatGPT API-Based Application Interface")
    print("1. Select a premade example")
    print("2. Input your details")
    print("3. Exit")
    
    # User input for choosing an option
    choice = input("Enter your choice: ")
    
    # Validate the user input to ensure it's a digit
    if choice.isdigit():
        choice = int(choice)
        if choice == 1:
            premade_examples()
        elif choice == 2:
            custom_input()
        elif choice == 3:
            print("Exiting.")
            exit()
        else:
            print("Invalid choice. Please enter a number between 1 and 3.")
            main_menu()
    else:
        print("Invalid input. Please enter a number.")
        main_menu()

def premade_examples():
    """
    Handles the functionality of running premade examples.
    
    The function reads a list of examples from a JSON file, displays them to the user,
    and runs the selected example.
    """
    try:
        # Load examples from the JSON file
        with open('examples.json', 'r') as file:
            examples = json.load(file)
    except FileNotFoundError:
        print("Error: The examples.json file was not found.")
        return
    except json.JSONDecodeError:
        print("Error: The examples.json file is not in a valid JSON format.")
        return
    
    # Display the list of examples to the user
    print("Select a premade example:")
    for i, example in enumerate(examples, start=1):
        print(f"{i}. {example['name']}: {example['description']}")
    
    # User input for choosing an example
    choice = input("Choose an example: ")
    
    # Validate the user input to ensure it's a digit and within the range of examples
    if choice.isdigit() and 1 <= int(choice) <= len(examples):
        selected_example = examples[int(choice) - 1]
        run_selected_example(selected_example)
    else:
        print("Invalid choice. Please enter a number corresponding to an example.")
        premade_examples()

def run_selected_example(example):
    """
    Runs the selected example by creating a function call and getting a response from the OpenAI API.
    
    :param example: A dictionary containing details of the selected example.
    """
    # Extracting entities, attributes, function name, and description from the example
    entities = example['entities']
    attributes = example['attributes']
    function_name = example['name']
    function_description = example['description']
    
    # Creating an instance of FunctionCallBuilder with the extracted information
    builder = FunctionCallBuilder(entities, attributes, function_name, function_description)
    
    # Constructing a user message for the completion method
    user_message = f"Please use your `{function_name}` function to define the {', '.join(attributes)} for each entity."
    
    # Calling the completion method to get a response from the OpenAI API
    builder.completion(user_message)

def custom_input():
    """
    Handles the functionality of inputting custom details for a function call.
    
    The user is prompted to enter a list of entities, a list of attributes, a function name, and a function description.
    The entered details are then used to create a function call and get a response from the OpenAI API.
    """
    # User input for entities, attributes, function name, and function description
    entities_input = input("Enter a list of entities, separated by commas: ")
    attributes_input = input("Enter a list of attributes, separated by commas: ")
    function_name = input("Enter the function name: ")
    function_desc = input("Enter the function description: ")
    
    # Converting the input strings to lists of strings
    entities = [entity.strip() for entity in entities_input.split(',')]
    attributes = [attribute.strip() for attribute in attributes_input.split(',')]
    
    # Creating an instance of FunctionCallBuilder with the entered details
    builder = FunctionCallBuilder(entities, attributes, function_name, function_desc)
    
    # Constructing a user message for the completion method
    user_message = f"Please use your `{function_name}` function to define the {', '.join(attributes)} for each entity."
    
    # Calling the completion method to get a response from the OpenAI API
    builder.completion(user_message)

if __name__ == "__main__":
    # Starting the application by displaying the main menu
    main_menu()
