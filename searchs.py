from flask import Blueprint, render_template, request, redirect, url_for
from services import SearchSaucer
from config import connex_app

search_bp = Blueprint('searchs', __name__, template_folder='templates', static_folder='static')

@search_bp.route('/searchsaucer',  methods=['GET','POST'])
def searchsaucer():
    if request.method == 'POST':
        tag = request.form['search']

        result = SearchSaucer.read_like(tag)
        print(result)

        return render_template('searchsaucer.html', data = result, searched = tag)

    return redirect(url_for('pages.login'))