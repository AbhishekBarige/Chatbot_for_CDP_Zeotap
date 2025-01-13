def handle_lytics_query(query):
    if "build an audience segment" in query.lower():
        return (
            "To build an audience segment in Lytics:\n"
            "1. Log in to the Lytics dashboard.\n"
            "2. Navigate to the 'Audiences' section.\n"
            "3. Click 'Create Audience'.\n"
            "4. Define rules for your audience using the visual query builder.\n"
            "5. Save the audience, and it will start building based on your criteria."
        )
    elif "integrate" in query.lower():
        return (
            "To integrate data with Lytics:\n"
            "1. Go to the 'Integrations' section of your Lytics dashboard.\n"
            "2. Select the integration you want to set up.\n"
            "3. Follow the step-by-step guide provided for the integration.\n"
            "4. Test the integration to ensure data flows as expected."
        )
    else:
        return (
            "Query not recognized. Please consult the Lytics documentation "
            "at https://docs.lytics.com for detailed guidance."
        )
