import json
from rest_framework.renderers import JSONRenderer
class UsuarioJSONRenderer(JSONRenderer):
    charset = 'utf-8'
    def render(self, data, media_type=None, renderer_context=None):
        errors = data.get('errors', None)

        if errors is not None:
            return super(UsuarioJSONRenderer, self).render(data)
        return json.dumps({
                'usuarios': data
            })

class PedidoJSONRenderer(JSONRenderer):
    charset = 'utf-8'
    def render(self, data, media_type=None, renderer_context=None):
        errors = data.get('errors', None)

        if errors is not None:
            return super(PedidoJSONRenderer, self).render(data)
        return json.dumps({
                'pedidos': data
            })

class ItemPedidoJSONRenderer(JSONRenderer):
    charset = 'utf-8'
    def render(self, data, media_type=None, renderer_context=None):
        errors = data.get('errors', None)

        if errors is not None:
            return super(ItemPedidoJSONRenderer, self).render(data)
        return json.dumps({
                'items': data
            })
class ProdutoJSONRenderer(JSONRenderer):
    charset = 'utf-8'
    def render(self, data, media_type=None, renderer_context=None):
        errors = data.get('errors', None)

        if errors is not None:
            return super(ProdutoJSONRenderer, self).render(data)
        return json.dumps({
                'produtos': data
            })

class ClienteJSONRenderer(JSONRenderer):
    charset = 'utf-8'
    def render(self, data, media_type=None, renderer_context=None):
        errors = data.get('errors', None)

        if errors is not None:
            return super(ClienteJSONRenderer, self).render(data)
        return json.dumps({
                'clientes': data
            })
