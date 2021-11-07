from webargs import fields, validate

PRODUCT_ARGS = {
    'id': fields.Int(),
    'codigo': fields.Str(required=True, validate=[validate.Length(min=1, max=30)]),
    'nome': fields.Str(required=True, validate=[validate.Length(min=5, max=250)]),
    'cod_barras': fields.Str(required=True, validate=[validate.Length(max=14)]),
    'referencia': fields.Str(required=True, validate=[validate.Length(max=14)]),
    'observacao': fields.Str(required=True, validate=[validate.Length(max=250)]),
    'pr_venda_vista': fields.Decimal(required=False, validate=[validate.Range(min=0.01)]),
    'pr_venda_prazo': fields.Decimal(required=False, validate=[validate.Range(min=0.01)]),
    'pr_custo': fields.Decimal(required=False, validate=[validate.Range(min=0)]),
    'outros': fields.Decimal(required=False, validate=[validate.Range(min=0)]),
    'estoque_minimo': fields.Decimal(required=False, validate=[validate.Range(min=0)]),

    'unidade': fields.Str(required=True, validate=validate.Length(min=2, max=4)),
    'setor_id': fields.Int(required=True),
    'qtd_embalagem': fields.Decimal(required=False),

    'ativo': fields.Boolean(),

}
