# Author: mendrika261
# Date: April 14, 2023
# Description: Generate SQL file from fihirana JSON file

import json


def generate_sql_from_fihirana_json(json_file, sql_file='data.sql', sql_dir='sql'):
    with open(json_file) as f:
        data = json.load(f)

    with open(sql_dir + '/' + sql_file, 'w') as f:
        for hira_index, row in enumerate(data.values()):
            sokajy = row['sokajy'].replace("'", "''")  # Escape single quote
            lohateny = row['lohateny'].replace("'", "''")  # Escape single quote
            isa_andininy = row['isa_andininy']
            mpanoratra = ','.join(row['mpanoratra']).replace("'", "''")  # Escape single quote
            hira = row['hira']

            # Generate sokajy
            if sokajy not in sokajy_list:
                sokajy_list.append(sokajy)  # Add sokajy to the list to avoid duplicate
                f.write(f"INSERT INTO sokajy (anarana)"
                        f"VALUES ('{sokajy}')"
                        f";\n")
            sokajy_index = sokajy_list.index(sokajy) + 1  # +1 because of the auto-increment

            # Generate hira
            f.write(f"INSERT INTO hira (sokajy_id, lohateny, isa_andininy, mpanoratra)"
                    f"VALUES ({sokajy_index}, '{lohateny}', {isa_andininy}, '{mpanoratra}')"
                    f";\n")

            # Generate tononkira
            for tonony in hira:
                andininy = tonony['andininy']
                tononkira = tonony['tononkira'].replace("'", "''").replace("\n", "\\n")  # Escape single quote and new line
                fiverenany = tonony['fiverenany']

                f.write(f"INSERT INTO tononkira (hira_id, andininy, tononkira, fiverenany)"
                        f"VALUES ({hira_index + 1}, {andininy}, '{tononkira}', '{fiverenany}')"
                        f";\n")

    print(f"SQL file generated: {sql_file}")


if __name__ == '__main__':
    sokajy_list = []  # List of sokajy to avoid duplicate
    generate_sql_from_fihirana_json('01_fihirana_ffpm.json', '01_fihirana_ffpm.sql')
    generate_sql_from_fihirana_json('02_fihirana_fanampiny.json', '02_fihirana_fanampiny.sql')
    generate_sql_from_fihirana_json('03_antema.json', '03_antema.sql')
