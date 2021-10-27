from pyptables import default_tables, restore
from pyptables.rules import Rule, Accept, Reject, Redirect, Return
import tools.database as db
import subprocess
from bottle import get

active_tables = default_tables()
   

def load_iptable():
    pass
    


@get("/api/iptables/list/:table/:chain")
def get_all_rules_table_chain(table, chain):
    rules = active_tables[table][chain]
    return rules

@get("/api/iptables/list/:table")
def get_all_rules_table(table):
    rules = active_tables[table]
    return rules

@get("/api/iptables/list")
def get_all_rules_table():
    rules = active_tables
    return rules

@get("/api/iptables/get/:table/:chain/:id")
def get_rule(table, chain, id):
    pass

@get("/api/iptables/append/:table/:chain/:rule")
def append_rule(table, chain, rule):
    pass

@get("/api/iptables/insert/:table/:chain/:id")
def insert_rule(table, chain, id):
    pass

@get("/api/iptables/remove/:table/:chain/:id")
def remove_rule(table, chain, id):
    pass

