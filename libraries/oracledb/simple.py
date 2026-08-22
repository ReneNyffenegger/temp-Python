#!/usr/bin/env python3

import oracledb
import sys

"""
Connects to an Oracle Database using python-oracledb in Thin mode,
executes a query, and prints the results.
"""

# Database connection details
username = 'elar'
password = 'elar'
dsn = '10.72.68.16:1522/sva18mig'

try:

    oracledb.init_oracle_client(lib_dir = '/home/rene/bin/instantclient_23_26') # Run in thick mode

    connection = oracledb.connect(user=username, password=password, dsn=dsn)
    print("✅ Successfully connected to Oracle Database.")

  # Create a cursor
    with connection.cursor() as cursor:
      # Example query: fetch first 5 employees
        cursor.execute('''
            select
               object_name obj,
               object_type typ,
               created     cre
            FROM
               user_objects
            fetch first 5 rows only
       ''')

      # Fetch and display results
        rows = cursor.fetchall()
        if not rows:
           print("No data found.")
        else:
           print("\nEmployee Data:")
           for obj, typ, cre in rows:
               print(f"ID: {obj}, Name: {typ} {cre}")

except oracledb.DatabaseError as e:
    error_obj, = e.args
    print(f"❌ Database error: {error_obj.message}", file=sys.stderr)

except Exception as e:
    print(f"❌ Unexpected error: {e}", file=sys.stderr)
finally:
    # Ensure connection is closed
    try:
        if connection:
            connection.close()
            print("🔒 Connection closed.")
    except NameError:
        pass  # connection was never created
