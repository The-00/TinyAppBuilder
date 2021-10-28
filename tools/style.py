from os import listdir


def get(who, path):
    real_path = "/".join(who.split(".")[:2]) + "/res/style/" + path
    with open(real_path, "r") as f:
        return f"<style> {''.join([l for l in f])} </style>"

def html_table(tableContent, tableHead=None):
    table  = "<table>"
    if tableHead:
        table += "<tr>" +  "".join([f"<th>{e}</th>" for e in tableHead]) +"</tr>"
    for tableLine in tableContent:
        table += "<tr>" +  "".join([f"<td>{e}</td>" for e in tableLine]) +"</tr>"
    table += "</table>"
    return table