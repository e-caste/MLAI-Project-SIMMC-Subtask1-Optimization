"""Create fashion preprocess tokenization of user utterance
"""

import argparse
import json
import numpy as np

from enums import Action
from enums import Attribute
from transformers import BertTokenizer


def main(args):
    print(f"Reading dialogs cleaned: {args['json_path']}")
    with open(args["json_path"], "r") as file_id:
        dials_clean = json.load(file_id)

    tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')
    dials_info = []
    all_utterance = []
    for dial in dials_clean:
        for turn in dial:
            all_utterance.append(turn["user_utterance"])

    tokens = tokenizer(all_utterance, padding=True)
    i = 0
    for dial in dials_clean:
        turns_info = []
        for turn in dial:
            attributes_enum = np.zeros(Attribute.length()).astype(int).tolist()
            for attribute in turn["attributes"]:
                attributes_enum[Attribute.from_str(attribute)] = 1
            turns_info.append({
                             "dialog_id": turn["dialog_id"],
                             "turn_idx": turn["turn_idx"],
                             "user_utterance": {
                                 "input_ids": tokens["input_ids"][i],
                                 "attention_mask": tokens["attention_mask"][i],
                             },
                             "action": Action.from_str(turn["action"]),
                             "attributes": attributes_enum,
                        })
            i = i + 1
        dials_info.append(turns_info)
    print(f"Saving information tokenized: {args['save_path']}")
    with open(args["save_path"], "w") as f:
        json.dump(dials_info, f)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Tokenize user utterance")
    parser.add_argument(
        "--json_path",
        default="data/fashion_train_dials.json",
        help="JSON dials info",
    )
    parser.add_argument(
        "--save_path",
        default="data/fashion_train_dials_api_calls.json",
        help="JSON API Call",
    )
    try:
        parsed_args = vars(parser.parse_args())
    except IOError as msg:
        parser.error(str(msg))
    main(parsed_args)
