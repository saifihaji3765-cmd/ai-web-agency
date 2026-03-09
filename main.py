from agents.client_finder import find_clients
from agents.lead_collector import save_leads
from agents.email_agent import send_email
from agents.website_builder import build_website
from agents.deploy_agent import deploy_site
from agents.payment_agent import send_payment_link


def run_ai_agency():

    print("AI Web Agency Started")

    # Step 1: Find clients
    clients = find_clients("small business near me")

    # Step 2: Save leads
    save_leads(clients)

    # Step 3: Send emails
    for client in clients:
        send_email(client)

    print("Emails sent to potential clients")

    # Example response simulation
    interested_client = clients[0]

    # Step 4: Build website
    site_path = build_website(interested_client)

    # Step 5: Deploy website
    live_url = deploy_site(site_path)

    # Step 6: Send payment link
    send_payment_link(interested_client, live_url)

    print("AI process completed")


if __name__ == "__main__":
    run_ai_agency()
