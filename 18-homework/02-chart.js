(function() {

  // Here is your data
  var countries = [
    {
      name: "Blahstia",
      continent: "North America",
      gdp: 40
    },
    {
      name: "Bleers",
      continent: "Europe",
      gdp: 12
    },
    {
      name: "Blolo",
      continent: "Antarctica",
      gdp: 35
    },
    {
      name: "Blurben",
      continent: "North America",
      gdp: 90
    }
  ]

  // Get the svg with the id of 'chart2'
  var svg = d3.select("#chart2")

  // Get the rectangles inside of it
  svg.selectAll("rect")

})()