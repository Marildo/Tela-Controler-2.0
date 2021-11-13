from webargs import fields, validate

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
    'estoque_minimo': fields.Decimal(required=False, validate=[validate.Range(min=0)], missing=0),
    'unidade_id': fields.Int(required=True),
    'setor_id': fields.Int(required=True),
    'qtd_embalagem': fields.Decimal(required=False, missing=0),
    'ativo': fields.Boolean(required=False,missing=True),
}
