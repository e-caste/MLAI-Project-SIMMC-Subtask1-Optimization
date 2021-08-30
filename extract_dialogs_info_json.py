"""Create fashion preprocess general info for dials
"""

import argparse
import json


def main(args):
    print(f"Reading dialogs: {args['json_path']}")
    with open(args["json_path"], "r") as file_id1:
        dials = json.load(file_id1)
    print(f"Reading API calls: {args['action_json_path']}")
    with open(args["action_json_path"], "r") as file_id2:
        actions = json.load(file_id2)

    dials_info = []
    i = 0
    for dial in dials["dialogue_data"]:
        turns_info = []
        j = 0
        for turn in dial["dialogue"]:
            user_utterance = turn["transcript"]
            dials_actions = actions[i]["actions"]
            dialog_id = actions[i]["dialog_id"]
            turn_idx = dials_actions[j]["turn_idx"]
            action = dials_actions[j]["action"]
            action_supervision = dials_actions[j]["action_supervision"]
            attributes = []
            if action_supervision:
                attributes = action_supervision['attributes']
            turns_info.append({
                             "dialog_id": dialog_id,
                             "turn_idx": turn_idx,
                             "user_utterance": user_utterance,
                             "action": action,
                             "attributes": attributes
                        })
            j = j+1
        dials_info.append(turns_info)
        i = i + 1
    print(f"Savings principal information of dialogs: {args['save_path']}")
    with open(args["save_path"], "w") as f:
        json.dump(dials_info, f)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Extract Dialogs info")
    parser.add_argument(
        "--json_path",
        default="data/fashion_train_dials.json",
        help="JSON dataset",
    )
    parser.add_argument(
        "--action_json_path",
        default="data/fashion_train_dials_api_calls.json",
        help="JSON API Call",
    )
    parser.add_argument(
        "--save_path",
        default="data/fashion_train_dials_info_dataloader.json",
        help="path of output clean info of dials",
    )
    parser.add_argument(
        "--num_prec_phrases",
        default=0,
        help="number of preceding phrases",
    )
    try:
        parsed_args = vars(parser.parse_args())
    except IOError as msg:
        parser.error(msg)
    main(parsed_args)
