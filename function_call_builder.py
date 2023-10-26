from ai import completion, token_count

class FunctionCallBuilder:
    """
    FunctionCallBuilder Class
    
    This class serves as a dynamic constructor for OpenAI function call definitions with a variable set of attributes
    and entities. In addition, it provides a mechanism to invoke the defined function via OpenAI's chat completion
    service, returning the results, and saving them to a file.
    
    Attributes:
        entities (list): A list of entities (e.g., countries, characters) for which attributes are to be defined.
        attributes (list): A list of attributes (e.g., "Tourist_Attractions", "Cultural_Experience") to be defined for each entity.
        function_name (str): The name of the function to be defined.
        function_description (str): A description outlining the purpose and scope of the function.
    """

    def __init__(self, entities, attributes, function_name, function_description):
        self.entities = entities
        self.attributes = attributes
        self.function_name = function_name
        self.function_description = function_description

    def generate_function_definition(self):
        parameters = {}
        for entity in self.entities:
            for attribute in self.attributes:
                param_name = f"{entity}_{attribute}".replace(" ", "_")
                parameters[param_name] = {
                    "type": "string",
                    "description": f"Define the {attribute} for {entity}"
                }

        function_definition = {
            "name": self.function_name,
            "description": self.function_description,
            "parameters": {
                "type": "object",
                "properties": parameters,
                "required": list(parameters.keys())
            }
        }

        return function_definition

   
    def completion(self, user_message):
        function_def = self.generate_function_definition()
        
        # Simulate the function call with user message
        msg = {"role": "user", "content": user_message}
        
        # Invoke the completion function
        response = completion(messages=[msg], max_token_count=11000, functions=[function_def], temperature=0.7)

        # Print the results and the token count
        print(response)

        print(f"Token count: {token_count(response)}")

        # Save the response to a .txt file named after the function
        with open(f"{self.function_name}.txt", 'w') as file:
            file.write(str(response))
            file.write(f"\nToken count: {token_count(response)}")

        return response

# Usage
if __name__ == "__main__":
    entities = ["USA", "Canada", "Germany"]
    attributes = ["Tourist_Attractions", "Cultural_Experience", "Cuisine"]
    function_name = "define_country_attributes"
    function_description = "Define attributes for various countries."
    builder = FunctionCallBuilder(entities, attributes, function_name, function_description)

    user_message = "Please use your `define_country_attributes` function to define the tourist attractions, cultural experiences, and cuisine for each country."
    builder.completion(user_message)
