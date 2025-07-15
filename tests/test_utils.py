from src.utils import helpers


def test_load_and_save_json(tmp_path):
    data = {'a': 1}
    json_file = tmp_path / 'data.json'
    json_file.write_text('{"a": 1}')
    assert helpers.load_json(str(json_file)) == data
    txt_file = tmp_path / 'out.txt'
    helpers.save_text(str(txt_file), 'hello')
    assert txt_file.read_text() == 'hello'
