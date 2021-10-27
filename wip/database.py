import sqlite3 as lite
import bcrypt
import os

con = None
database = "src/db/database.db"

def initialize():
    if not os.path.isfile(database):
        try:
            con = lite.connect(database)
            cur = con.cursor()  
            # create tables
            cur.execute('''CREATE TABLE IF NOT EXISTS roles (
                                id integer PRIMARY KEY,
                                name text NOT NULL)'''
                        )
            cur.execute('''CREATE TABLE IF NOT EXISTS users (
                                id integer PRIMARY KEY,
                                name text NOT NULL,
                                password text NOT NULL,
                                role_id integer,
                                FOREIGN KEY (role_id) REFERENCES roles (id))'''
                        )
            cur.execute('''CREATE TABLE IF NOT EXISTS wifi_known (
                                id integer PRIMARY KEY,
                                ssid text NOT NULL,
                                password text,
                                ip text NOT NULL,
                                network text NOT NULL,
                                gateway text NOT NULL,
                                last_seen date)
                                '''
                        )
            cur.execute('''CREATE TABLE IF NOT EXISTS vpn_known (
                                id integer PRIMARY KEY,
                                name text NOT NULL,
                                config text NOT NULL,
                                role_id integer)
                                '''
                        )
            cur.execute('''CREATE TABLE IF NOT EXISTS config_profiles (
                                id integer PRIMARY KEY,
                                name text NOT NULL,
                                ssid text NOT NULL,
                                password text, 
                                dhcp text,
                                vpn_id integer,
                                FOREIGN KEY (vpn_id) REFERENCES vpn_known (id))
                                '''
                        )
        except lite.Error as e:   
            error = e.args[0]
            print(error)
        finally:
            if con:
                con.close()
        # populate
        add_role("Administrator") #1
        add_role("Manager")       #2
        add_role("User")          #3
        
        add_user("root", bcrypt.hashpw(b"root", bcrypt.gensalt()), 1)
        
        add_config_profile("Main", "Green", "Green", None, None)

        
def add_role(name):
    try:
        con = lite.connect(database)
        cur = con.cursor()  
        cur.execute('INSERT INTO roles(name) VALUES(?)', [name])
        con.commit()
    except lite.Error as e:   
        error = e.args[0]
        print(error)
    finally:
        if con:
            con.close()
    
def add_user(name, password, role_id):
    try:
        con = lite.connect(database)
        cur = con.cursor()  
        cur.execute('INSERT INTO users(name,password,role_id) VALUES(?,?,?)', [name,password,role_id])
        con.commit()
    except lite.Error as e:   
        error = e.args[0]
        print(error)
    finally:    
        if con:
            con.close()

def add_wifi(ssid, password, ip, network, gateway):
    try:
        con = lite.connect(database)
        cur = con.cursor()  
        cur.execute('INSERT INTO wifi_known(ssid,password,ip,netword,gateway) VALUES(?,?,?,?,?)', [ssid,password,ip,network,gateway])
        con.commit()
    except lite.Error as e:   
        error = e.args[0]
        print(error)
    finally:
        if con:
            con.close()
            
def add_vpn(name, config):
    try:
        con = lite.connect(database)
        cur = con.cursor()  
        cur.execute('INSERT INTO vpn_known(name,config) VALUES(?,?)', [name,config])
        con.commit()
    except lite.Error as e:   
        error = e.args[0]
        print(error)
    finally:
        if con:
            con.close()

def add_config_profile(name, ssid, password, dhcp, vpn_id):
    try:
        con = lite.connect(database)
        cur = con.cursor()  
        cur.execute('INSERT INTO config_profiles(name,ssid,password,dhcp,vpn_id) VALUES(?,?,?,?,?)', [name,ssid,password,dhcp,vpn_id])
        con.commit()
    except lite.Error as e:   
        error = e.args[0]
        print(error)
    finally:
        if con:
            con.close()

def execute_SELECT(request):
    initialize()
    error = None
    
    try:
        con = lite.connect(database)
        cur = con.cursor()  
        cur.execute(request)
        data = cur.fetchall()                
    except lite.Error as e:   
        error = e.args[0]
    finally:
        if con:
            con.close()
    return (data, error)