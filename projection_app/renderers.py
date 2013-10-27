from rest_framework.renderers import UnicodeJSONRenderer

class GeoJSONRenderer(UnicodeJSONRenderer):
    media_type = 'application/json'
    format = 'geojson'

    def render(self, data, media_type=None, renderer_context=None):
        geojson = {
            'count': data['count'],
            'next': data['next'],
            'previous': data['previous'],
            'type': 'FeatureCollection',
            'features': [] 
        }
        geometry_field = renderer_context.get('geometry_field', 'geometry')
        for f in data['results']:
            geometry = f.pop(geometry_field)
            feature = {
                'type': 'Feature',
                'geometry': geometry,
                'properties': f
            }
            geojson['features'].append(feature)

        ret = super(GeoJSONRenderer, self).render(geojson, media_type, renderer_context)

        return ret
