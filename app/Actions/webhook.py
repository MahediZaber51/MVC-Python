import requests

# Define the function to send a webhook
def send_webhook(url, data):
    """
    Send a webhook to the specified URL with the given data.

    Args:
        url (str): The webhook URL.
        data (dict): The data to send in the webhook.

    Returns:
        Response: The response from the webhook request.
    """
    response = requests.post(url, json=data)
    return response

# Define the function to process a webhook
def process_webhook(data):
    """
    Process the incoming webhook data.

    This function processes the incoming webhook data and returns a response.

    Args:
        data (dict): The webhook data.

    Returns:
        str: A response message.
    """
    # Process the webhook data here
    return f"Webhook received with data: {data}"