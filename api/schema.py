instructions = [
        "DROP TABLE IF EXISTS playersdata;",

        """CREATE TABLE IF NOT EXISTS playersdata (
        id INT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(60) NOT NULL,
        position VARCHAR(12) NOT NULL,
        nation VARCHAR(60) NOT NULL,
        club VARCHAR(60) NOT NULL
        );"""
        ]
