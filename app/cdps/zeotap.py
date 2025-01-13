def handle_zeotap_query(query):
    if "integrate my data" in query.lower():
        return (
            "To integrate your data with Zeotap:\n"
            "1. Log in to the Zeotap platform.\n"
            "2. Go to the 'Integrations' section.\n"
            "3. Select the desired integration type (e.g., API, SFTP, or partner).\n"
            "4. Follow the provided setup instructions to configure data ingestion.\n"
            "5. Test the integration to ensure data transfer is successful."
        )
    elif "analyze audience insights" in query.lower():
        return (
            "To analyze audience insights in Zeotap:\n"
            "1. Navigate to the 'Audience Insights' section of the dashboard.\n"
            "2. Select the audience you want to analyze.\n"
            "3. View demographic, behavioral, and contextual data for the audience.\n"
            "4. Use filters and segmentation options to refine the insights."
        )
    else:
        return (
            "Query not recognized. Please refer to the Zeotap documentation "
            "at https://docs.zeotap.com/home/en-us/ for detailed guidance."
        )
