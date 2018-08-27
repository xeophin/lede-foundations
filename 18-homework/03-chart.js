(function() {

  // Don't edit any of this
  var height = 50, width = 400;

  var svg = d3.select("#chart3")
    .select("svg")
    .attr("height", height + 50)
    .attr("width", width + 50)
    .select("g")
    .attr("transform", "translate(25, 25)")

  var datapoints = [
    { 'name': 'Panda', 'weight': 150 },
    { 'name': 'Cat', 'weight': 8 },
    { 'name': 'Horse', 'weight': 840 },
    { 'name': 'Pig', 'weight': 100 }
  ]

  // Build your scales here


  // Set your attributes here
  svg.selectAll("circle")

})()