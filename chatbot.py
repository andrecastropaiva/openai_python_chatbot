# Import necessary libraries
import os
import openai
from dotenv import load_dotenv
import json

# Load .env file
load_dotenv()

# Set API key
api_key = os.getenv('OPENAI_API_KEY')
openai.api_key = api_key


# Define the function to get the completion from the prompt
def get_completion(prompt, model="gpt-3.5-turbo-16k-0613"):
    messages = [{"role": "user", "content": prompt}]
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=0,
    )
    return response.choices[0].message["content"]  # Get the completion from the response


# Define the function to get the completion from the response
def get_completion_from_messages(messages, model="gpt-3.5-turbo-16k-0613", temperature=0):
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=temperature,
    )
    return response.choices[0].message["content"]


def main():
    # Initialise context
    context = [
        {'role': 'system', 'content': """
            You are BurgerBot, an automated service to collect orders for a Burger restaurant. \
            You first greet the customer, then collect the order, \
            and then ask if it's a pickup or delivery. \
            You wait to collect the entire order, then summarize it and check for a final \
            time if the customer wants to add anything else. \
            If it's a delivery, you ask for an address. \
            Finally you collect the payment.\
            Make sure to clarify all options, extras and sizes to uniquely \
            identify the item from the menu.\
            You respond in a short, very conversational friendly style. \
            The menu includes \
            classic burger  £12.95, £10.00, £7.00 \
            cheeseburger   £10.95, £9.25, £6.50 \
            veggie burger   £11.95, £9.75, £6.75 \
            chicken burger £11.00, £8.75, £6.00 \
            fish burger £12.00, £9.00, £7.00 \
            fries £5.00, £4.50, £3.50 \
            caesar salad £7.25 \
            Toppings: \
            extra cheese £2.00, \
            mushrooms £1.50 \
            bacon £3.00 \
            avocado £3.50 \
            AI sauce £1.50 \
            jalapenos £1.00 \
            Soft drinks: \
            coke £3.00, £2.00, £1.00 \
            sprite £3.00, £2.00, £1.00 \
            bottled water £5.00 \
            Beers: \
            lager £4.50 \
            ale £5.00 \
            stout £5.50 \
            ipa £7.00 \
            Desserts: \
            chocolate cake £4.00 \
            apple pie £4.50 \
            vanilla ice cream £3.50 \
            When user not sure or undecided, always display the FULL menu as a table in HTML format.\
            Once the order is complete, display a summary of the order and the total price.\
            Ask the user if they want to add anything else.\
            If they say no, ask if it's a pickup or delivery.\
            If it's a pickup, ask for the name of the customer.\
            If it's a delivery, ask for the address of the customer.\
            Finally, ask for the payment method.\
            If the payment method is cash, ask for the amount of cash.\
            If the payment method is card, ask for the card number, expiry date and CVV.\
            Tell the customer to write 'exit' to quit.\
            At the end, generate a JSON file with the order summary.\
            Make sure the JSON code is structured and easy to read.\
            """}
    ]

    # Generate the bot initial greeting.
    initial_greeting = get_completion_from_messages(context)
    context.append({'role': 'assistant', 'content': f"{initial_greeting}"})

    # Print the bot initial greeting.
    print("Assistant: ", initial_greeting)

    # Simulate the conversation
    while True:

        prompt = input("User: ")
        context.append({'role': 'user', 'content': f"{prompt}"})

        response = get_completion_from_messages(context)
        context.append({'role': 'assistant', 'content': f"{response}"})

        print("Assistant: ", response)

        # If the user says 'exit', break the loop
        if prompt.lower() == 'exit':
            break

    # Generate order summary
    messages = context.copy()
    messages.append(
        {'role': 'system', 'content':
            'create a json summary of the previous food order. Itemize the price for each item.\
            The fields should be \
            1) burger, include size \
            2) list of toppings \
            3) list of drinks, include size \
            4) list of sides include size \
            5) total price '}
    )
    response = get_completion_from_messages(messages, temperature=0)

    # Remove the three backticks and leading/trailing whitespaces
    response = response.replace("```json\n", "").replace("```", "").strip()

    # Save the response as a JSON file - parse the response first to make it more readable (using json.dumps)
    try:
        parsed_response = json.loads(response)
        formatted_response = json.dumps(parsed_response, indent=4)
    except json.JSONDecodeError:
        formatted_response = response

    # Save the response as a JSON file
    with open("order_summary.json", "w") as file:
        file.write(formatted_response)


# Run the main function when the script is executed directly from the command line (not imported)
if __name__ == "__main__":
    main()
