(function () {

  var margin = {top: 20, right: 10, bottom: 20, left: 20}

  var width  = 960 - margin.left - margin.right,
      height = 500 - margin.top - margin.bottom

  // Create the SVG
  var svg = d3.select('#chart').append('svg')
    .attr('width', width + margin.left + margin.right)
    .attr('height', height + margin.top + margin.bottom)
    .append('g')
    .attr('transform', 'translate(' + margin.left + ',' + margin.top + ')')

  var tableRows = d3.selectAll('tr')
    .data(laughByName)
    .enter().append('tr')

  tableRows.selectAll('th').enter().append('th').text(function (d) {return d.key})

  tableRows.selectAll('td div')
    .data(function (d) {
      return d.values
    })
    .enter().append('div')
    .style('background-color', 'red')

  var xPositionScale = d3.scaleLinear()
    .domain([0, 80000])
    .range([0, width])

  var yPositionScale = d3.scaleLinear()
    .domain([0, 90])
    .range([height, 0])

  let colorScale = d3.scaleOrdinal()
    .range(['red', 'blue', 'orange', 'cyan', 'violet'])

  // Read in some external data. When we're done, run the function 'ready'
  d3.queue()
    .defer(d3.csv, 'countries.csv')
    .await(ready)

  // This is 'ready':
  // it receives an error (if there is one)
  // and datapoints, our newly-read-in data
  function ready (error, datapoints) {
    console.log('Data is', datapoints)
    // d3 code goes here
    svg.selectAll('circle')
      .data(datapoints)
      .enter().append('circle')
      .attr('r', 5)
      .attr('cx', d => xPositionScale(d.gdp_per_capita))
      .attr('cy', d => yPositionScale(d.life_expectancy))
      .attr('fill', d => colorScale(d.continent))

    // Always cut and paste the code for the axes!
    var yAxis = d3.axisLeft(yPositionScale)
    svg.append('g')
      .attr('class', 'axis y-axis')
      .call(yAxis)

    var xAxis = d3.axisBottom(xPositionScale)
    svg.append('g')
      .attr('class', 'axis x-axis')
      .attr('transform', 'translate(0,' + height + ')')
      .call(xAxis)

  }

})()