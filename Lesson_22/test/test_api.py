import pytest
from ..API import api_images

@pytest.mark.parametrize("url, header",
                         [("https://httpbin.org/image", "image/*"), ("https://httpbin.org/image/jpeg", "image/jpeg"),
                          ("https://httpbin.org/image/png", "image/png"), ("https://httpbin.org/image/svg", "image/svg"),
                          ("https://httpbin.org/image/webp", "image/webp")])
def test_status_codes(url, header):
    assert api_images.get_images(url, header) == 200