def send_payment_link(client, site_url):

    payment_link = "https://payment-link-example.com"

    message = f"""
Your website is ready!

Preview:
{site_url}

To receive the final version please complete payment:
{payment_link}
"""

    print("Payment message sent to client")
    print(message)
