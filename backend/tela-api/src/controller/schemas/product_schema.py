from marshmallow_sqlalchemy import SQLAlchemySchema, auto_field
from marshmallow_sqlalchemy.fields import Nested, fields

from src.model.entities import Produto
from .section_schema import SectionSchema


class ProductSchema(SQLAlchemySchema):
    class Meta:
        load_instance = True
        model = Produto

    codigo = auto_field()
    nome = auto_field()
    cod_barras = auto_field()
    referencia = auto_field()
    observacao = auto_field()

    pr_venda_vista = fields.String()
    pr_venda_prazo = fields.String()

    estoque = fields.String()
    estoque_minimo = fields.String()
    pr_custo = fields.String()
    outros = fields.String()

    qtd_embalagem = fields.String()

    unidade = Nested(SectionSchema, exclude=('ativo',))
    setor = Nested(SectionSchema, exclude=('ativo',))

    ultima_compra = fields.String()
    ultima_venda = fields.String()
    ativo = auto_field()
