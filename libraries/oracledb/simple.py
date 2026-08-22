#!/usr/bin/env python3

import oracledb
import sys

"""
Connects to an Oracle Database using python-oracledb in Thin mode,
executes a query, and prints the results.
"""

username = 'elar'
password = 'elar'
dsn = '10.72.68.16:1522/sva18mig'

try:

  # Run in thick mode:
    oracledb.init_oracle_client(lib_dir = '/home/rene/bin/instantclient_23_26')

    connection = oracledb.connect(user=username, password=password, dsn=dsn)
    print("✅ Successfully connected to Oracle Database.")

    with connection.cursor() as cursor:

        cursor.execute('''
            select
               object_name obj,
               object_type typ,
               created     cre
            FROM
               user_objects
            fetch first 5 rows only
       ''')

        rows = cursor.fetchall()
        if not rows:
           print("No data found.")
        else:
           print("\nEmployee Data:")

         # Align the three displayed columns for easier scanning.
           print(f"{'Object Name':<30} {'Object Type':<20} {'Created'}")
           for obj, typ, cre in rows:
               print(f"{obj:<30} {typ:<20} {cre}")

except oracledb.DatabaseError as e:
    error_obj, = e.args
    print(f"❌ Database error: {error_obj.message}", file=sys.stderr)

except Exception as e:
    print(f"❌ Unexpected error: {e}", file=sys.stderr)

finally:
    try:
        if connection:
           connection.close()
           print("🔒 Connection closed.")
    except NameError:
      # connection was never created
        pass
