import sqlite3


def sqlite_con(db="./videos.db"):
    con = sqlite3.connect(db)
    con.row_factory = sqlite3.Row
    return con


def fetchall_dict(con, *args):
    return [dict(r) for r in con.execute(*args).fetchall()]


def single_column_tolist(array_of_half_tuplets, column_name=1):
    return list(
        map(
            lambda x: x[column_name],
            array_of_half_tuplets,
        )
    )
