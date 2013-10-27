Occupation = Backbone.Model.extend();
Occupations = Backbone.Collection.extend({
  model: Occupation,
  url: '/api/occupations/?format=json',
  geojson: function(f) {
    return {
        "type": "Feature",
        "id": f.id,
        "properties": f,
        "geometry": f["state"]["geometry"]
    };
  },
  parse: function(results) {
    return _.map(results.objects, this.geojson);
  }
});