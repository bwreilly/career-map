// http://www.projectionscentral.com/Projections/AboutLT

State = Backbone.Model.extend();
States = Backbone.Collection.extend({
  model: State,
  url: '/static/projection_app/js/states.json',
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

    var projection = d3.geo.albersUsa();

    var path = d3.geo.path()
      .projection(projection);

    view.draw(path);
  },
  draw: function(path) {
    var view = this;
    var svg = d3.select("#mapcontainer").append("svg:svg")
        .attr("class", "RdYlGn")
        .attr("width", view.w)
        .attr("height", view.h);

    d3.json("/static/projection_app/js/states.json", function(error, us) {
      svg.append("path")
        .datum(topojson.feature(us, us.objects.states))
        .attr("d", path);
    });
  },
  render: function() {
    var view = this;
    var occupations = this.collection;
    $('#maptitle').html(view.name);

    var metric = view.metric;
    var median, stddev;

    if (metric !== 'percentchange'){
      var vals = _.pluck(occupations, metric);
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

    // d3.json("/static/projection_app/js/states.json", function(error, us) {
    //   // states_svg.append("path")
    //   //     .datum(topojson.feature(us, us.objects.states))
    //   //     .attr("d", view.path)
    //   //     .attr("class", function(d) {
    //   //       return "q" + quantize(d[view.metric]) + "-9";
    //   //     });
    //   states_svg.selectAll("path")
    //     .data(topojson.feature(us, us.objects.states).features)
    //   .enter().append("path")
    //     .attr("class", function(d) {
    //       return "q" + quantize(d[view.metric]) + "-9";
    //     })
    //     .attr("d", view.path);
    // });

    // var features = occupations.toJSON();
    // var states = new States();
    // states.fetch();
    // var map = states_svg.selectAll("path")
    //   .data(features)
    // .enter().append("svg:path")
    //   .attr("d", view.path)
    //   .attr("class", function(d) {
    //     return "q" + quantize(d[view.metric]) + "-9";
    //   });
    // map.append("svg:text")
    //   .text(function(d) {
    //     return d.properties["state"]["state_name"] + ": " + d.properties[view.metric];
    //   });

    // $('path').hover(function(e){
    //   console.log(e.target.textContent);
    //   $(e.target).popover({'container': e.target});
    // });
  }
});