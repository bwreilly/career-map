Occupation = Backbone.Model.extend();
Occupations = Backbone.Collection.extend({
  model: Occupation,
  url: '/api/occupations/?format=json',
  parse: function(response) {
    return response.results;
  }
});