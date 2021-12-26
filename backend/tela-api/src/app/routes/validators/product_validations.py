from webargs import fields, validate

from .section_validations import SECTION_ARGS
from .unity_validations import UNITY_ARGS

PRODUCT_ARGS = {
    'id': fields.Int(),
    'codigo': fields.Str(required=True, validate=[validate.Length(min=1, max=30)]),
    'nome': fields.Str(required=True, validate=[validate.Length(min=5, max=250)]),
    'cod_barras': fields.Str(required=False, validate=[validate.Length(max=14)]),
    'referencia': fields.Str(required=False, validate=[validate.Length(max=14)]),
    'observacao': fields.Str(required=False, validate=[validate.Length(max=250)]),
    'pr_venda_vista': fields.Decimal(required=False, validate=[validate.Range(min=0.01)], missing=0.01),
    'pr_venda_prazo': fields.Decimal(required=False, validate=[validate.Range(min=0.01)], missing=0.01),
    'pr_custo': fields.Decimal(required=False, validate=[validate.Range(min=0)], missing=0.01),
    'outros': fields.Decimal(required=False, validate=[validate.Range(min=0)], missing=0.01),
    'estoque': fields.Decimal(required=False, missing=0),
    'estoque_minimo': fields.Decimal(required=False, validate=[validate.Range(min=0)], missing=0),
    'qtd_embalagem': fields.Decimal(required=False, missing=1),
    'ativo': fields.Boolean(required=False, missing=True),
    'unidade': fields.Nested(UNITY_ARGS, required=True, error_messages={'_schema': 'A unidade é obrigatória'}),
    'setor': fields.Nested(SECTION_ARGS, required=True, error_messages={'_schema': 'o Setor é obrigatória'}),
    'ultima_compra': fields.Str(required=False),
    'ultima_venda': fields.Str(required=False)
}
