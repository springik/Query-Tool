import tkinter
import psycopg2

def run_query(inp, out):
    try:
        # Connection creation
        conn = psycopg2.connect(
            dbname='dvdrental',
            user='postgres',
            host='localhost',
            port='5432',
            password='kobliha456'#shh don't tell anyone
        )
        # Query execution
        cur = conn.cursor()
        cur.execute(inp.get('1.0', 'end'))
        response = cur.fetchall()
        # Response formatting
        formatted_response = "\n".join([str(row) for row in response])
        # Output into the output Text
        out.delete('1.0', 'end')
        out.insert('end', formatted_response)
    except Exception as error:
        print("Error when executing query")
        print(error)


def main():
    m = tkinter.Tk(screenName="Query Tool")
    
    inp = tkinter.Text(m)
    out = tkinter.Text(m)
    btn = tkinter.Button(m, text="Run Query", width="80", command=lambda:run_query(inp, out))


    inp.pack()
    btn.pack()
    out.pack()
    m.mainloop()

main()
