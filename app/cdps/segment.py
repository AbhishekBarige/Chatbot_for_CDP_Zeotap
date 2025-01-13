def handle_segment_query(query):
    if "set up a new source" in query.lower():
        return (
            "To set up a new source in Segment:\n"
            "1. Log in to your Segment workspace.\n"
            "2. Navigate to the 'Sources' tab.\n"
            "3. Click 'Add Source' and select the source type (e.g., Web, Mobile, Server).\n"
            "4. Follow the setup instructions for the chosen source type.\n"
            "5. Once configured, Segment will start collecting data from this source."
        )
    elif "send data to a destination" in query.lower():
        return (
            "To send data to a destination in Segment:\n"
            "1. Go to the 'Destinations' tab in your workspace.\n"
            "2. Click 'Add Destination' and select the desired destination (e.g., Google Analytics, Facebook Ads).\n"
            "3. Follow the configuration wizard to connect your destination.\n"
            "4. Ensure your source is connected to this destination in the Connections view.\n"
            "5. Test the integration to confirm data is flowing correctly."
        )
    elif "track events" in query.lower():
        return (
            "To track events in Segment:\n"
            "1. Use the Segment SDK appropriate for your platform (e.g., JavaScript, iOS, Android).\n"
            "2. Call the 'track' method provided by the SDK to log custom events.\n"
            "3. Include event names and properties as required.\n"
            "4. Ensure your source is sending data to the desired destination."
        )
    else:
        return (
            "Query not recognized. For detailed steps and guidance, refer to the Segment documentation at "
            "https://segment.com/docs/?ref=nav."
        )
