(function () {

  var cities = [
    {
      'name': 'NYC',
      'population': 8,
      'sq_mi': 304
    },
    {
      'name': 'Tokyo',
      'population': 14,
      'sq_mi': 845
    },
    {
      'name': 'LA',
      'population': 4,
      'sq_mi': 4500
    },
    {
      'name': 'Brooklyn',
      'population': 4,
      'sq_mi': 97
    }
  ]

  var height = 300
  var width = 800

  // First you grab the svg...
  var svg = d3.select('#viz')
    .attr('height', height)
    .attr('width', width)

  // ...then you grab the circles in
  // the svg and manipulate them
  // We need to specify: cy, cx, r
  // But we'll also need some scales...

  svg.selectAll('circle')

})()
