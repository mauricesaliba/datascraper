import psycopg2
import psycopg2.extras
import pandas as pd

DB_HOST = "tststgdocker01"
DB_NAME = "jirasDB"
DB_USER = "postgres"
DB_PASS = "admin1234"

issues_filepath = "C:/Users/maurice.saliba/OneDrive - GO PLC/MANAGEMENT/JIRA/Workspace/RUNS/2022-03-15/ISSUES/"
issues_filename_input = "filtered1.csv";
issues_filename_output = "filtered2.csv";
columns = ["summary",	'issue key',	"issue id",	"issue type",	"status",	"project key",	"priority",	"resolution",	"assignee",	"reporter",	"creator",	"created",	"updated",	"resolved",	"fix version/s",	"component/s",	"due date",	"labels",	"description",	"outward issue link (depends)",	"outward issue link (relates)",	"custom field (corporate project code)",	"custom field (epic link)",	"custom field (epic name)",	"sprint",	"sprint_1",	"sprint_2",	"sprint_3",	"sprint_4",	"sprint_5",	"sprint_6",	"sprint_7",	"sprint_8",	"sprint_9",	"custom field (story points)",	"custom field (system/area)",	"custom field (team)"]

sql_table_jiras_columns =""

types_varchar_large = ['description', 'summary']
types_timestamp = ["created",	"updated",	"resolved", "due date",]

for column in columns:
    if column in types_varchar_large:
        sql_table_jiras_columns += "\"" + column + "\" VARCHAR(1000),\n"
    elif column in types_timestamp:
        sql_table_jiras_columns += "\"" + column + "\" TIMESTAMP,\n"
    else:
        sql_table_jiras_columns += "\"" + column + "\" VARCHAR(100),\n"

sql_table_jiras_columns = sql_table_jiras_columns[:-2]

sql_table_jiras_create_command = "CREATE TABLE jiras (" + sql_table_jiras_columns + ");"

print(sql_table_jiras_create_command)



def get_connection():
    conn = psycopg2.connect(dbname=DB_NAME, user=DB_USER, password=DB_PASS, host=DB_HOST)
    return conn

def create_jira_table(conn):
    with conn:
        with conn.cursor(cursor_factory=psycopg2.extras.DictCursor) as cur:
            cur.execute("SET datestyle = dmy;")
            cur.execute("DROP TABLE IF EXISTS jiras;")
            cur.execute(sql_table_jiras_create_command)
            #cur.execute("SELECT * FROM jiras;")
            #print(cur.fetchall())

def upload_csv_to_table(conn, filepath_csv_to_upload):

    sql = "COPY jiras FROM STDIN WITH CSV HEADER DELIMITER AS ','"
    f = open(filepath_csv_to_upload,encoding="utf8")

    with conn:
        with conn.cursor(cursor_factory=psycopg2.extras.DictCursor) as cur:
            #cur.copy_from(f, 'jiras', columns=(columns), sep=",")
            cur.copy_expert(sql, f)
            conn.commit()
            cur.close()



            #cur.execute("SELECT * FROM student;")
            #print(cur.fetchall())

    f.close()

conn = get_connection()
create_jira_table(conn)
#filepath_csv_to_upload = "C:/Users/maurice.saliba/OneDrive - GO PLC/MANAGEMENT/JIRA/Workspace/RUNS/2022-03-15/ISSUES/filtered1.csv"

filepath_csv_to_upload = issues_filepath + issues_filename_output
print("filepath_csv_to_upload" + filepath_csv_to_upload)
upload_csv_to_table(conn, filepath_csv_to_upload)
conn.close()












#cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)

#cur.execute("CREATE TABLE student (id SERIAL PRIMARY KEY, name VARCHAR);")

#cur.execute("INSERT INTO student (name) VALUES(%s)", ("Cristina",))

#conn.commit()

#cur.close()

#conn.close()


#cur.execute("SELECT * FROM student;")

#print(cur.fetchall())


#with conn:
    #with conn.cursor(cursor_factory=psycopg2.extras.DictCursor) as cur:
        #cur.execute("SELECT * FROM student WHERE id = %s;", (1,))

        #cur.execute("SELECT * FROM student;")
        #print(cur.fetchall())

        #print(cur.fetchone()['name'])

        #cur.execute("INSERT INTO student (name) VALUES(%s)", ("David",))




