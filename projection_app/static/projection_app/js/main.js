MainView = Backbone.View.extend({
  el: '#main',
  statistics: {
    'Growth': 'percentchange',
    'Projected Total': 'proj',
    'Avg Annual Openings': 'avgannualopenings'
  },
  events: {
    'click button': 'update_stat'
  },
  names: function(query, process) {
    $.getJSON('api/names/', {'name': query, 'format': 'json'},
      function(d) {
        process(_.pluck(d.results, 'name'));
    });
  },
  update_stat: function(e) {
    var view = this;
    view.map.metric = view.statistics[e.target.textContent];
    view.map.render();
  },
  update: function(item) {
    this.map.name = item;
    this.map.collection.fetch({data: {"name": item}, 'reset': true});
    return item;
  },
  initialize: function() {
    _.bindAll(this);
    var view = this;
    view.map = new StateMap();
    $('#search').typeahead({
      updater: view.update,
      source: view.names
    });
  }
});

$(function() {
  var main = new MainView();
});