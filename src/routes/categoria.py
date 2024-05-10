from flask import Blueprint, render_template
from src.modules import db
import sqlalchemy as sa
from src.models.categoria import Categoria

bp = Blueprint('categoria', __name__, url_prefix='/categoria')


@bp.route('/', methods=['GET'])
def lista():
    sentenca = sa.select(Categoria).order_by(Categoria.nome)
    rset = db.session.execute(sentenca).scalars()

    return render_template('categoria/lista.jinja2', rset=rset)
