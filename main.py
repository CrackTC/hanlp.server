import os
import hanlp
import hanlp.utils
import hanlp.pretrained
from flask import Flask, request, jsonify

def split(s):
    for i in range(0, len(s), 500):
        yield s[i:i+500]

def flatten(xss):
    return [x for xs in xss for x in xs]


HanLP = (
    hanlp.pipeline()
    .append(hanlp.utils.rules.split_sentence, output_key="sentences")
    .append(lambda ss: flatten(map(split, ss)))
    .append(hanlp.load(hanlp.pretrained.tok.COARSE_ELECTRA_SMALL_ZH), output_key="tok")
    .append(hanlp.load(hanlp.pretrained.pos.CTB9_POS_ELECTRA_SMALL), output_key="pos")
)


app = Flask(__name__)


@app.post("/")
def cut():
    result = HanLP(request.form["text"])
    return jsonify(list(zip(flatten(result["tok"]), flatten(result["pos"]))))


if __name__ == "__main__":
    port = int(os.environ.get("PORT", "5000"))
    app.run(host="::", port=port)
