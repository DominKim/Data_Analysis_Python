from flask import Flask, render_template, request, redirect
import webbrowser


app = Flask(__name__)

@app.route("/")
def index():
    from database import db_conn
    _, cursor = db_conn("oracle")
    cursor.execute("select * from search")
    data = cursor.fetchall()
    if data:
        cursor.execute("select text, count(text) from search group by text order by count(text) desc")
        data2 = cursor.fetchall()
    else:
        data2 = 0

    return render_template("/test.html", data = data2)

@app.route("/search", methods = ["POST", "GET"])
def google():
    from database import db_conn
    conn, cursor = db_conn("oracle")
    import urllib.parse

    if request.method == "POST":
        search = request.form["search"]
        menu = request.form["menu"]
        sql = f"insert into search values('{search}')"
        cursor.execute(sql)
        conn.commit()
        
        if menu == "google":
            if search:
                encode = urllib.parse.quote_plus(search)
                url = "http://google.com/search?q="+ encode
            return webbrowser.open(url)
        elif menu == "scholar":
            if search:
                encode = urllib.parse.quote_plus(search)
                url = "https://scholar.google.com/scholar?&q=" + encode
            return webbrowser.open(url)
        elif menu == "news":
            if search:
                from make_df import df
                df("oracle", search)
                cursor.execute(f"select text, sum(count) from news where search = '{search}' group by text order by sum(count) desc")
                texts = cursor.fetchall()
                
            return render_template("/semi_result.html", search = search, texts = texts)
    cursor.close();conn.close()
    return "a"
        



if __name__ == "__main__":
    app.run()