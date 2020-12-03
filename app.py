from flask import Flask, request, jsonify, render_template
import pandas as pd
app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to p4da capstone api!"

# static endpoint
# mendapatkan keseluruhan data buku dari books_c.csv
@app.route('/data/getallbook')
def get_all_book():
    data = pd.read_csv('data/books_c.csv',engine='python')
    # menyaring data buku agar tidak duplikat (Duplicates operation)
    return (data.drop_duplicates().to_json())

# static endpoint
# mendapatkan keseluruhan penulis buku dari books_c.csv
@app.route('/data/getallauthor')
def get_all_author():
    data = pd.read_csv('data/books_c.csv',engine='python')
    # memakai fungsi categorical data di panda (Categorical operation)
    return (pd.DataFrame({'authors': pd.
        Categorical(data["authors"]).categories}).to_json())

# dynamic endpoint
# mendapatkan keseluruhan penulis buku dari books_c.csv
@app.route('/data/getauthorbookcount/<author>', methods=['GET'])
def get_author_book_count(author):
    data = pd.read_csv('data/books_c.csv',engine='python')
    # Hitung jumlah penulisan buku oleh masing-masing author (Frequencies analysis)
    data = data["authors"].value_counts()
    dict = data.to_dict()
    # Penanganan missing value di dalam data (Missing Value operation)
    response = {"bookcount of "+author: None}
    if author in dict:
        response = {"bookcount of "+author: dict[author]}
    return(jsonify(response))

def isFloat(potential_float):
    try:
        float(potential_float)
        return True
    except ValueError:
        return False

# dynamic endpoint
# mendapatkan buku dengan minimal rating yang ditentukan
@app.route('/data/getbookminrating/<rating>', methods=['GET'])
def get_book_with_min_rating(rating):
    response = {"message": None}
    if isFloat(rating):
        data = pd.read_csv('data/books_c.csv',engine='python')
        mask = data["average_rating"] >= float(rating)
        data = data[mask]
        # penggunaan melt function untuk mendapatkan judul buku dan rata-rata rating
        data = pd.melt(data, id_vars =['title'], value_vars =['average_rating'])
        response = {"booktitle": data['title'].tolist(),
                    "rating": data['value'].tolist()}
    return(jsonify(response))

# static endpoint
# menampilkan rata-rata rating dari para penulis buku
@app.route('/data/getaveragebookauthors')
def get_average_book_authors():
    data = pd.read_csv('data/books_c.csv',engine='python')
    # penggunaan melt function untuk mendapatkan rata-rata rating dan authornya
    data = pd.melt(data, id_vars =['authors'], value_vars =['average_rating'])
    data = data.rename(columns = {'value': 'average_book_rating'}, inplace = False)
    # penggunaan groupby function untuk menghitung rata-rata rating per penulis
    data = data.groupby(['authors']).mean().reset_index()
    return(data.to_json())


# menampilkan rata-rata rating dari para penulis buku
@app.route('/docs')
def docs():
    data = {"url":"http://p4da-capstone-api.herokuapp.com/data"}
    return render_template('README.html', data=data)

if __name__ == '__main__':
    app.run()
