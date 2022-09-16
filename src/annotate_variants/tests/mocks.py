import json

from unittest.mock import MagicMock


def mock_requests_get(url, **_):
    variant = url.split('/')[-1]
    return MockResponse(data_for_variant[variant])


class MockResponse(MagicMock):
    def __init__(self, data, **kwargs):
        super(MockResponse, self).__init__(data, **kwargs)
        self._data = data

    def json(self):
        return [self._data]

    @property
    def ok(self):
        if 'error' not in self._data:
            return True

    @property
    def status_code(self):
        if 'error' in self._data:
            return 400
        return 200

    @property
    def text(self):
        if 'error' in self._data:
            return self._data['error']


with open('src/annotate_variants/tests/mock_data.json', 'r') as mock_data_file:
    mock_data = mock_data_file.read()

data_for_variant = json.loads(mock_data)
