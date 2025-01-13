def handle_mparticle_query(query):
    if "create a user profile" in query.lower():
        return (
            "To create a user profile in mParticle:\n"
            "1. Use the mParticle SDK to send user attributes.\n"
            "2. Define user attributes such as email, phone number, or custom fields.\n"
            "3. Send the data to mParticle using the SDK's 'logUser' or 'identify' methods.\n"
            "4. The profile will be created or updated in the mParticle dashboard."
        )
    elif "set up a new data feed" in query.lower():
        return (
            "To set up a new data feed in mParticle:\n"
            "1. Go to the 'Inputs' section of the dashboard.\n"
            "2. Click 'Add Input'.\n"
            "3. Choose the appropriate input type (e.g., SDK, API, or partner integration).\n"
            "4. Follow the setup wizard to configure your data feed."
        )
    else:
        return (
            "Query not recognized. Please refer to the mParticle documentation "
            "at https://docs.mparticle.com for detailed steps."
        )
