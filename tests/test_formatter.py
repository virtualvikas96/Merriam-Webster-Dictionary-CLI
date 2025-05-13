from mwcli.formatter import format_definition

def test_format_definition():
    mock_data = [{
        "fl": "noun",
        "hwi": {"prs": [{"mw": "ek-sər-ˌsīz"}]},
        "shortdef": ["the act of bringing into play or realizing in action"]
    }]
    result = format_definition("exercise", mock_data)
    assert "exercise" in result
    assert "noun" in result

