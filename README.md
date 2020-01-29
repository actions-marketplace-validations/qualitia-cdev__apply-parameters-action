# apply parameters action

Currently, under developing.
Apply parameters which is in a parameter file to target files.
The parameter file is YAML.

## Inputs

### - parameter

A parameter YAML file path.

### - target-dir

A target directory path which you want to apply parameters.
This action will search recursively under the directory.

### - filter-file

You need to specify which type of file you want to change.
You can use a file name or filename extension such as "\*.yaml".

## Example usage

```
- uses: qualitia-cdev/apply-parameters-action
  with:
  parameter: ./develop.yaml
  target-dir: ./build
  filter-file: "_.yaml_"
```
