import sqlite3


class Database:
    def __init__(self):
        self.db = sqlite3.connect(r"..\Data\database.SQLITE")

    def get_level_data(self):
        cur = self.db.cursor()
        data = cur.execute("SELECT level_number, level_stars FROM levels").fetchall()
        cur.close()
        return sorted(data, key=lambda x: x[0])

    def set_stars(self, level, stars):
        cur = self.db.cursor()
        data = cur.execute("SELECT level_stars FROM levels WHERE level_number = ?", (level,)).fetchone()[0]
        stars = max(data, stars)
        cur.execute("UPDATE levels SET level_stars = ? WHERE level_number = ?;", (stars, level))
        self.db.commit()
        cur.close()
