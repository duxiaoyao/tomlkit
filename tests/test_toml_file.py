import io
import os

import pytest

from tomlkit.exceptions import EmptyKeyError
from tomlkit.toml_document import TOMLDocument
from tomlkit.toml_file import TOMLFile


def test_toml_file(example):
    original_content = example("example")

    toml_file = os.path.join(os.path.dirname(__file__), "examples", "example.toml")
    toml = TOMLFile(toml_file)

    content = toml.read()
    assert isinstance(content, TOMLDocument)
    assert content["owner"]["organization"] == "GitHub"

    toml.write(content)

    try:
        with io.open(toml_file, encoding="utf-8") as f:
            assert original_content == f.read()
    finally:
        with io.open(toml_file, "w", encoding="utf-8") as f:
            assert f.write(original_content)


def test_toml_file_in_utf8_with_bom_format():
    toml_file = os.path.join(os.path.dirname(__file__), "examples", "utf8_with_bom.toml")
    try:
        TOMLFile(toml_file).read()
    except EmptyKeyError:
        pytest.fail("Unexpected EmptyKeyError ...")
