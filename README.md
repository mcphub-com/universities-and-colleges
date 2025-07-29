markdown
# Universities and Colleges MCP Server

Welcome to the Universities and Colleges MCP server! This server provides a comprehensive set of tools to retrieve information about universities and colleges around the world, with a focus on institutions located in the United States. Whether you're interested in general university listings or detailed insights into specific institutions, this server has you covered.

## Overview

The Universities and Colleges MCP server offers different subscription tiers to cater to your needs, ranging from basic to mega plans, each with varying levels of access and pricing. The server is designed to provide high-quality service with efficient response times and robust data.

### Key Features

- **Global University and College Information**: Access a vast array of data on universities and colleges worldwide.
- **Detailed US-based College Insights**: For US institutions, retrieve detailed information such as school colors, type (private/public), nickname, mascot, address, city, state, state code, zip, and website.
- **Flexible Subscription Plans**: Choose the subscription plan that best fits your needs, from basic to mega.

## Tool List

The server offers the following tools to interact with university and college data:

1. **Universities**
   - **Description**: Retrieve a list of universities.
   - **Parameters**:
     - `page` (optional, Number): The default is 0. Specify the page number for pagination.
     - `includeUniversityDetails` (optional, Boolean): Include additional university details such as school colors, mascot, website, address, and more. Note that including details incurs a cost.
     - `countryCode` (optional, String): Filter results by country code (e.g., US).
     - `limit` (optional, Number): The default is 10, with a maximum page size of 50.
     - `search` (optional, String): Filter results by searching the name value.

2. **University Details by ID**
   - **Description**: Retrieve a single university by ID. Automatically includes any available university details, which may incur a cost if additional details are present.
   - **Parameters**:
     - `id` (String): The unique identifier for the university.

### Billing Information

- The server operates on a freemium model, with certain features available for free and others accessible through paid subscriptions.
- You will only be billed for the 'University Details' billing object if details such as school colors, mascot, website, and address are present in the response.
- For the `GET /Universities` endpoint, setting `includeUniversityDetails` to true will result in billing for the number of universities returned that include the specified details.

## Additional Information

Currently, detailed university information is supported for US-based colleges only. For requests to support other countries or additional school details (e.g., departments, acceptance rates), please contact us.

Thank you for using the Universities and Colleges MCP server. We are committed to providing the most accurate and comprehensive data available for educational institutions worldwide.