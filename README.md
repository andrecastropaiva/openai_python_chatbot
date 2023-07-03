# AI OrderBot: Automated Ordering Service

OrderBot is an automated service designed to collect orders for a Burger restaurant. It is built using the OpenAI GPT-3.5 language model and provides a conversational interface to interact with customers. This repository contains the code for OrderBot and allows you to set up your own automated ordering system.

## Features

- **Conversational Interface:** OrderBot engages in a friendly conversation with customers, guiding them through the order process.
- **Order Collection:** OrderBot collects customer orders by asking for specific menu items, sizes, and extras.
- **Pickup or Delivery:** Customers can specify whether they want to pick up their order or have it delivered.
- **Address Collection:** In case of a delivery, BurgerBot asks for the customer's address.
- **Payment Collection:** OrderBot asks for type of payment information to complete the order.

## Prerequisites

Before running the OrderBot code, make sure you have the following:

- Python 3.6 or above
- OpenAI Python library
- Python `dotenv` library

## Installation

1. Clone the repository:

```shell
git clone (https://github.com/andrecastropaiva/openai_python_chatbot.git)
```

2. Install the required dependencies:

```shell
pip install openai 
pip install python-dotenv 
pip install panel
```

3. Set up your OpenAI API key:

   - Rename the `.env.example` file to `.env`.
   - Open the `.env` file and replace `YOUR_API_KEY` with your OpenAI API key.

## Usage
To interact with OrderBot, follow these steps:

1 - Run the OrderBot code.

2 - The OrderBot interface will be displayed in the console or terminal.

3 - Input your messages and press enter to send them to OrderBot.

4 - OrderBot will respond with appropriate messages based on the conversation flow.

5 - Follow the prompts and provide the necessary information to complete your order.

6 - Once the conversation is finished, OrderBot will summarize the order and provide the final details.

NOTE: Please make sure to have the necessary dependencies installed and configured as mentioned in the Prerequisites section of the README file.



## Customisation

You can customise the behaviour of BurgerBot by modifying the code. Here are a few areas you can consider:

- **Menu Items:** Update the menu items, prices, and options in the `context` variable to match your restaurant's menu.
- **Conversation Flow:** Modify the conversation flow by adjusting the messages and responses in the `collect_messages` function.
- **User Interface:** Change the look and feel of the OrderBot interface by modifying the Panel components in the `dashboard` layout.

## Limitations

BurgerBot is based on the GPT-3.5 turbo language model, which has certain limitations. It may occasionally generate responses that are nonsensical or unrelated to the context. It's important to review and validate the generated responses to ensure accurate order collection.

## License

This project is licensed under the [MIT License](LICENSE).

## Acknowledgments

- [OpenAI](https://openai.com/) for providing the GPT-3.5 language model.
- [Panel](https://panel.holoviz.org/) for the interactive user interface components.

## Contributing

Contributions are welcome! If you find any issues or want to enhance the functionality of OrderBot, please open an issue or submit a pull request.
