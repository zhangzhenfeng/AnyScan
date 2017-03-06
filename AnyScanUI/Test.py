import cx_Oracle

if __name__ == "__main__":

    dsn = cx_Oracle.makedsn("192.168.1.1", "1521", "orcl")
    con = cx_Oracle.cx_Oracle("root", "root", dsn)