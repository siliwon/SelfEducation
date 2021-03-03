import sqlite3 as lite


def create_database(database_path: str):
    connection = lite.connect(database_path)
    with connection:
        cur = connection.cursor()
        cur.execute("drop table if exists words")
        ddl = 'CREATE TABLE "words" (' \
              '"word" TEXT NOT NULL UNIQUE, ' \
              '"usage_count"	INTEGER NOT NULL DEFAULT 1, ' \
              'PRIMARY KEY("word"))'
        cur.execute(ddl)
        ddl = "CREATE UNIQUE INDEX words_word_uindex ON words (word)"
        cur.execute(ddl)
    connection.close()


def save_words_to_database(database_path: str, words_list: list):
    connection = lite.connect(database_path)
    with connection:
        cur = connection.cursor()
        for word in words_list:
            # check to see if the word is in there
            sql = "SELECT count(word) FROM words WHERE word='" + word + "'"
            cur.execute(sql)
            count = cur.fetchone()[0]
            if count > 0:
                sql = "UPDATE words SET usage_count = usage_count + 1 " \
                      "WHERE word= '" + word + "'"
            else:
                sql = "INSERT INTO words(word) VALUES('" + word + "')"
            cur.execute(sql)
        # connection.close()
        print("Database save complete!")
