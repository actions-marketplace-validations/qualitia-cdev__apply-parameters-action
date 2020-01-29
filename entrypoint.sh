#!/bin/bash -eu

echo "Start convert yaml file"

readonly PARAMETER_FILE=$1
readonly TARGET_DIR=$2
readonly FILE_FILTER_OPTION=$3

readonly files=$(\find ${TARGET_DIR} -name "${FILE_FILTER_OPTION}")

echo "PARAMETER_FILE: ${PARAMETER_FILE}"
echo "TARGET_DIR: ${TARGET_DIR}"
echo "FILE_FILTER_OPTION: ${FILE_FILTER_OPTION}"
echo "files: ${files}"

for target_file in ${files}; do
    echo "target_file: ${target_file}"
    cat ${target_file}

    conv-cfn ${PARAMETER_FILE} ${target_file} > ${target_file}.tmp
    if [[ -x "${target_file}" ]]; then
        echo "File ${target_file} is executable"
        chmod +x ${target_file}.tmp
    fi

    mv ${target_file}.tmp ${target_file}
    echo "---------------------------------------------------"
    cat ${target_file}

done

echo "End convert"
