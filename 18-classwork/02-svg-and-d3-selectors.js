(function () {

  console.log('test')
  
  let colorScale = d3.scaleLinear()
    .domain([0,500])
    .range(['beige', 'teal'])
  
  d3.select('circle')
    .attr('r', 100)
    .attr('cx', 100)
    .attr('cy', 100)
    .attr('fill', colorScale(300))
  
  d3.select('svg')
    .append('rect')
    .attr('width', 200)
    .attr('height', 400)
    .attr('x', 200)
    .attr('y', 300)

})()