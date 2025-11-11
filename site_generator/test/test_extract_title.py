import pytest
from site_generator import extract_title

@pytest.mark.parametrize(
    "markdown_input, expected_output",
    [
        (
            "# header",
            "header"
        ),
        (
            "## not h1\n\n# h1",
            "h1"
        ),
        (
            "# 1\n\n# 2",
            "1"
        )
    ]
)

def test_extract_title(markdown_input, expected_output):
    assert extract_title(markdown_input) == expected_output


def test_extract_title_raises_error():
    with pytest.raises(Exception) as exit_info:
        extract_title("11111")
    assert str(exit_info.value) == "File doesn't have 'h1' header!"