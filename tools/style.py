from os import listdir


def get(who, path):
    real_path = "/".join(who.split(".")[:2]) + "/res/style/" + path
    with open(real_path, "r") as f:
        return f"<style> {''.join([l for l in f])} </style>"
