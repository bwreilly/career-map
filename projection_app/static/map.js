
// State = Backbone.Model.extend();
// States = Backbone.Collection.extend({
//   model: State,
//   url: '/api/v1/state/?format=json',
//   parse: function(results) {
//     return results.objects;
//   }
// });

// http://www.projectionscentral.com/Projections/AboutLT

Occupation = Backbone.Model.extend();
Occupations = Backbone.Collection.extend({
  model: Occupation,
  url: '/api/v1/occupation/?format=json',
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

MainView = Backbone.View.extend({
  el: '#main',
  statistics: {
    'Growth': 'percentchange',
    'Projected Total': 'proj',
    'Avg Annual Openings': 'avgannualopenings'
  },
  events: {
    'click  button': 'update_stat'
  },
  names: function(query, process) {
    $.getJSON('api/v1/occupation/', {'name__icontains': query, 'state__id': 1, 'format': 'json'},
      function(d) {
        process(_(d.objects).pluck('name'));
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

StateMap = Backbone.View.extend({
  id: 'map',
  tagName: "div",
  w: 1280,
  h: 600,
  metric: "percentchange",
  name: '',
  metric_stats: {  // some precomputed values for domain
    "percentchange": {
      'median': 1,
      'stddev': 12.211
    }
  },
  initialize: function() {
    _.bindAll(this);
    var view = this;
    var occupations = new Occupations();
    view.name = "Computer Programmers";
    occupations.fetch({data: {"name": view.name}, 'reset': true});
    occupations.once("reset", view.draw, view);
    occupations.on("reset", view.render, view);
    view.collection = occupations;

    var projection = d3.geo.azimuthal()
      .mode("equiarea")
      .origin([-98, 38])
      .scale(1200)
      .translate([410, 340]);

    view.path = d3.geo.path()
      .projection(projection);
  },
  draw: function() {
    console.log('welp');
  },
  render: function() {
    var view = this;
    var occupations = this.collection;
    $('#maptitle').html(view.name);
    d3.select("#mapcontainer").html('');
    var svg = d3.select("#mapcontainer").append("svg:svg")
        .attr("class", "RdYlGn")
        .attr("width", view.w)
        .attr("height", view.h);

    var states = svg.append("svg:g")
        .attr("id", "states");

    var metric = view.metric;
    var median, stddev;

    if (metric !== 'percentchange'){
      var vals = _(occupations.pluck('properties')).pluck(metric);
      median = vals.sort()[25];
      var total = _(vals).reduce(function(m, f) {
        return f + m;
      }, 0);
      var avg = total / 50;
      stddev = Math.sqrt(vals.reduce(function(a, x) {
        return Math.pow(x - avg, 2) + a;
      }, 0) / 50);
    } else {
      median = view.metric_stats[metric]['median'];
      stddev = view.metric_stats[metric]['stddev'];
    }
    var pad = d3.format("05d");
    var quantize = d3.scale.quantize()
      .domain([median - stddev, median, median + stddev])
      .range(d3.range(9));

    var features = occupations.toJSON();
    var map = states.selectAll("path")
      .data(features)
    .enter().append("svg:path")
      .attr("d", view.path)
      .attr("class", function(d) {
        return "q" + quantize(d.properties[view.metric]) + "-9";
      });
    map.append("svg:text")
      .text(function(d) {
        return d.properties["state"]["state_name"] + ": " + d.properties[view.metric];
      });

    $('path').hover(function(e){
      console.log(e.target.textContent);
      $(e.target).popover({'container': e.target});
    });
  }
});

$(function() {
  var main = new MainView();

});