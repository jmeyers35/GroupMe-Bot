import json
import markovify
import os
import sys

def createModels(corpiDir, dstDir):
    directory = os.fsencode(corpiDir)
    for file in os.listdir(directory):
        fname = os.fsdecode(file)
        if not fname.startswith("."):
            person_name = fname.split("_messages")[0]
            # Build the model
            with open ("{}/{}".format(corpiDir, fname)) as f:
                text = f.read()
                text_model = markovify.NewlineText(text)
                # print("##########################################")
                # print("Five generated sentences from " + person_name)
                # for _ in range(5):
                #     print(text_model.make_sentence(tries=1000, max_overlap_ratio=0.4, max_overlap_total=10))
                model_json = text_model.to_json()
                with open("{}/{}_model.json".format(dstDir, person_name), 'w') as outfile:
                    json.dump(model_json, outfile)


def main():
    corpiDir = sys.argv[1]
    destDir = sys.argv[2]
    createModels(corpiDir, destDir)

if __name__ == "__main__":
    main()