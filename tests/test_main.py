import pytest
import main

def test_envconfiglinter_instantiation():
    # Verify that the class EnvConfigLinter is inspectable and loadable
    assert hasattr(main, 'EnvConfigLinter')

