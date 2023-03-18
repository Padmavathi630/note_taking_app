from flask import Flask, render_template, request, make_response

app = Flask(__name__)

@app.route('/', methods=["GET", "POST"])
def index():
    notes = request.cookies.get('notes')
    if not notes:
        notes = []
    else:
        notes = notes.split(',')
    
    if request.method == "POST":
        note = request.form.get("note")
        notes.append(note)
        notes_str = ','.join(notes)
        resp = make_response(render_template("home.html", notes=notes))
        resp.set_cookie('notes', notes_str)
        return resp
    
    return render_template("home.html", notes=notes)

if __name__ == '__main__':
    app.run(debug=True)
