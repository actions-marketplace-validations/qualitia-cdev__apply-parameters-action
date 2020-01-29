#!/bin/env python3
import sys
import argparse

from . import conv_cfn


def get_opt() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description='Set environment variables which is set on parmeter_file_path to target and output them to stdout')
    parser.add_argument("parmeter_yaml_file_path", action="store", nargs=1)
    parser.add_argument("target_file_path", action="store", nargs=1)

    args = parser.parse_args()

    return args


def main() -> int:
    args = get_opt()

    conv_cfn.set_yaml_to_env(args.parmeter_yaml_file_path[0])
    print(conv_cfn.convert(args.target_file_path[0]))

    return 0


if __name__ == "__main__":
    sys.exit(main())
