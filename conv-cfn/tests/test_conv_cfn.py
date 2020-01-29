import os
import yaml

from conv_cfn import conv_cfn


class TestYamlToEnv:
    def init_test_yaml(self, contents, tmpdir):
        f = tmpdir.join("test.yaml")
        f.write(contents)
        tmpdir.chdir()

    def test_hogehoge_1_on_yaml_is_in_to_env_as_key_hogehoge_val_1(self, tmpdir):
        contents = '''
hogehoge: 1
'''
        self.init_test_yaml(contents, tmpdir)
        conv_cfn.set_yaml_to_env("test.yaml")

        assert os.environ['hogehoge'] == '1'

    def test_hogehoge_ohoho_1_on_yaml_is_in_to_env_as_key_hogehoge_ohoho_val_1(self, tmpdir):
        contents = '''
hogehoge:
    ohoho: 1
'''
        self.init_test_yaml(contents, tmpdir)
        conv_cfn.set_yaml_to_env("test.yaml")

        assert os.environ['hogehoge.ohoho'] == '1'

    def test_array_on_yaml_is_in_to_env_as_key_word_plus_index_val_word(self, tmpdir):
        contents = '''
hogehoge:
    - 5
    - 6
'''
        self.init_test_yaml(contents, tmpdir)
        conv_cfn.set_yaml_to_env("test.yaml")

        assert os.environ['hogehoge.0'] == '5'
        assert os.environ['hogehoge.1'] == '6'


class TestEnvToYaml:
    def init_test_yaml(self, contents, tmpdir):
        f = tmpdir.join("test.yaml")
        f.write(contents)
        tmpdir.chdir()

    def test_hogehoge_1_on_env_is_set_hogehoge_on_yaml(self, tmpdir):
        os.environ['hogehoge'] = '1'
        contents = '''
test: ${hogehoge}
'''
        self.init_test_yaml(contents, tmpdir)

        assert yaml.safe_load(conv_cfn.convert("test.yaml")) == {"test": 1}

    def test_hogehoge_12_on_env_is_set_hogehoge_on_yaml(self, tmpdir):
        os.environ['hogehoge'] = '12'
        contents = '''
test: ${hogehoge}
'''
        self.init_test_yaml(contents, tmpdir)

        assert yaml.safe_load(conv_cfn.convert("test.yaml")) == {"test": 12}
