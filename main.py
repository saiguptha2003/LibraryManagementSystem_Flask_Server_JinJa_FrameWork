
from flask import Flask, redirect, render_template, request, url_for
import utility as u
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/create_member', methods=['GET', 'POST'])
def createmember():
    if request.method == 'POST':
        memID=request.form['memID']
        name=request.form['name']
        address=request.form['address']
        email=request.form['email']
        phone=request.form['phone']
        if(u.insert_member(memID,name,address,email,phone)):
            redirect(url_for('success'))
        else:
            redirect(url_for('fail'))
    else:
        return render_template('create_member.html')
    return render_template('create_member.html')

@app.route('/create_loan', methods=['GET', 'POST'])
def createLoan():
    if request.method=='POST':
        loanID=request.form['loanID']
        bookID=request.form['bookID']
        memID=request.form['memID']
        loanDate=request.form['loanDate']
        returnDate=request.form['returnDate']
        if(u.insert_loan(loanID,bookID,memID,loanDate,returnDate)):
            redirect(url_for('success'))
        else:
            redirect(url_for('fail'))
    else:
        return render_template('create_loan.html')
    return render_template('create_loan.html')

@app.route('/create_genre', methods=['GET', 'POST'])
def create_genre():
    if request.method=='POST':
        genreID=request.form['genreID']
        genreName=request.form['genreName']
        if(u.insert_genre(genreID,genreName)):
            redirect(url_for('success'))
        else:
            redirect(url_for('fail'))
    else:
        return render_template('create_genre.html')
    return render_template('create_genre.html')

@app.route('/create_book', methods=['GET', 'POST'])
def createBook():
    if request.method=='POST':
        bookID=request.form['bookID']
        bookName=request.form['bookName']
        authorID=request.form['author_id']
        isbn=request.form['isbn']
        published_year=request.form['published_year']
        quantity=request.form['quantity']
        if(u.insert_book(bookID,bookName,authorID,isbn,published_year,quantity)):
            redirect(url_for('success'))
        else:
            redirect(url_for('fail'))
    else:
        return render_template('create_book.html')
    return render_template('create_book.html')

@app.route('/create_author', methods=['GET', 'POST'])
def create_author():
    if request.method=='POST':
        authorid=request.form['authorid']
        authorname=request.form['authorname']   
        birth_date=request.form['birth_date']
        nationality=request.form['nationality']
        if(u.insert_author(authorid,authorname,birth_date,nationality)):
            redirect(url_for('success'))
        else:
            redirect(url_for('fail'))
    else:
        return render_template('create_author.html')
    return render_template('create_author.html')

@app.route('/show_Genre', methods=['GET', 'POST'])
def show_Genre():
    header=['Genre ID','Genre Name']
    return render_template('show_genres.html', data=u.get_genres(),header=header)

@app.route('/show_Book', methods=['GET', 'POST'])
def show_Book():
    header=['Book ID','Book Name','Author ID','ISBN','Published Year','Quantity']
    return render_template('show_books.html', data=u.get_books(),header=header)

@app.route('/show_Author', methods=['GET', 'POST'])
def show_Author():
    header=['AuthorID','authorname','birth_date','nationality']
    return render_template('show_authors.html', data=u.get_authors(),header=header)

@app.route('/show_Member', methods=['GET', 'POST'])
def show_Member():
    header=['Member ID','Name','Address','Email','Phone']
    return render_template('show_members.html', data=u.get_members(),header=header)

@app.route('/show_Loan', methods=['GET', 'POST'])
def show_Loan():
    header=['Loan ID','Book ID','Member ID','Loan Date','Return Date']
    return render_template('show_loans.html', data=u.get_loans(),header=header)


@app.route('/success')
def success():
    return render_template('success.html')

@app.route('/fail')
def fail():
    return render_template('fail.html')

        
        


app.run(debug=True)