from flask import Blueprint, render_template, request, redirect, url_for
from services import SearchSaucer
from services import SearchEatery

search_bp = Blueprint('searchs', __name__, template_folder='templates', static_folder='static')

@search_bp.route('/searchsaucer',  methods=['GET','POST'])
def searchsaucer():
    if request.method == 'POST':
        tag = request.form['search']

        result = SearchSaucer.read_like(tag)
    
        return render_template('searchsaucer.html', data = result, searched = tag)

    return redirect(url_for('/'))

@search_bp.route('/eatery')
def eatery():
    id_eatery = request.args.get('id_eatery')
    if id_eatery:
        eatery_data = SearchEatery.eatery_by_id(int(id_eatery))
    return render_template('eatery.html', eatery=eatery_data)