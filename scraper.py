def fetch_case_data(case_type, case_number, filing_year):
    # For demo: return dummy data
    parsed_result = {
        'parties': 'ABC vs XYZ',
        'filing_date': '2021-06-01',
        'next_hearing': '2025-09-12',
        'latest_order_url': 'https://example.com/sample-order.pdf'
    }
    raw_response = '<html>...original HTML content...</html>'

    return parsed_result, raw_response
