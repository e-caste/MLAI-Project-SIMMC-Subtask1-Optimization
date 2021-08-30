#!/bin/bash

DOMAIN="fashion"
ROOT="./data/simmc_${DOMAIN}/"

# Input files.
TRAIN_JSON_FILE="${ROOT}${DOMAIN}_train_dials.json"
DEV_JSON_FILE="${ROOT}${DOMAIN}_dev_dials.json"
DEVTEST_JSON_FILE="${ROOT}${DOMAIN}_devtest_dials.json"
DEMO_JSON_FILE="${ROOT}train_demo_small.json"

if [ "$DOMAIN" == "fashion" ]; then
    METADATA_FILE="${ROOT}fashion_metadata.json"
else
    echo "Invalid domain!"
    exit 0
fi

for CONT in 0 6 12; do
  if [ $CONT == 0 ]; then
    HISTORY_PAD=""
    HISTORY_NAME=""
  else
    HISTORY_PAD="_history$CONT"
    HISTORY_NAME="_history"
  fi

  echo -n "Generating model input files"
  [[ "$HISTORY_PAD" == "" ]] && echo -n " without" || echo -n " with"
  echo " history with $CONT preceding phrases..."
  echo

  # Step 1: Extract assistant API.
  echo "Starting step 1"
  INPUT_FILES="${TRAIN_JSON_FILE} ${DEV_JSON_FILE} ${DEVTEST_JSON_FILE}"
      python ./extract_actions_fashion.py \
          --json_path="${INPUT_FILES}" \
          --save_root="${ROOT}" \
          --metadata_path="${METADATA_FILE}"
  echo "Finished step 1"
  echo
  echo "Starting step 2"
  # Step 2: create a json with important info of dialogs and actions for each splits.
  SPLIT_JSON_FILES=("${TRAIN_JSON_FILE}" "${DEV_JSON_FILE}" "${DEVTEST_JSON_FILE}")
  for SPLIT_JSON_FILE in "${SPLIT_JSON_FILES[@]}" ; do
       DIALOGS="${SPLIT_JSON_FILE/.json}_clean_info${HISTORY_PAD}.json"
       python ./extract_dialogs_info${HISTORY_NAME}_json.py \
          --json_path="${SPLIT_JSON_FILE}" \
          --save_path="${DIALOGS}" \
          --action_json_path="${SPLIT_JSON_FILE/.json/_api_calls.json}" \
          --num_prec_phrases="$CONT"
  done
  echo "Finished step 2"
  echo
  echo "Starting step 3"
  # Step 3: convert every user utterance in BERT token and add information useful for BERT model
  SPLIT_JSON_FILES=("${TRAIN_JSON_FILE}" "${DEV_JSON_FILE}" "${DEVTEST_JSON_FILE}")
  for SPLIT_JSON_FILE in "${SPLIT_JSON_FILES[@]}" ; do
       DIALOGS="${SPLIT_JSON_FILE/.json}_clean_info${HISTORY_PAD}.json"
       DIALOGS_TOKENIZED="${SPLIT_JSON_FILE/.json}_info_tokenized${HISTORY_PAD}.json"
       python ./tokenize_user_utterance.py \
          --json_path="${DIALOGS}" \
          --save_path="${DIALOGS_TOKENIZED}"
  done
  echo "Finished step 3"
  echo
done

echo "Finished Preprocessing"
