from marshmallow_sqlalchemy import SQLAlchemySchema, auto_field
from marshmallow_sqlalchemy.fields import Nested
from .section_schema import SectionSchema
from src.model.entities import Produto


class ProductSchema(SQLAlchemySchema):
    class Meta:
        load_instance = True
        model = Produto

    codigo = auto_field()
    nome = auto_field()
    cod_barras = auto_field()
    referencia = auto_field()
    observacao = auto_field()

    pr_venda_vista = auto_field()
    pr_venda_prazo = auto_field()

    estoque = auto_field()
    estoque_minimo = auto_field()
    pr_custo = auto_field()
    outros = auto_field()

    unidade = auto_field()
    qtd_embalagem = auto_field()
    setor_id = auto_field()
    setor = Nested(SectionSchema, exclude=('ativo',))

    ultima_compra = auto_field()
    ultima_venda = auto_field()
    ativo = auto_field()

