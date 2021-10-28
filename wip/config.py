from bottle import get

@get("/config")
def test():
    ret = db.execute_SELECT("SELECT users.name,roles.name FROM users JOIN roles ON users.role_id = roles.id")
    if ret[1] != None:
        return f"<h1>{ret[1]}</h1>"
    else:
        s = "<ol>"
        for l in ret[0]:
            s += f"<li>{l}</li>"
        s+= "</ol>"
        return s
            