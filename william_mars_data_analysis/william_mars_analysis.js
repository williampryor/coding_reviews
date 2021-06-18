//Assign the data from 'mars.nasa.gov.json' to a variable
var mars_data = soles;

// Select the button
var button = d3.select("#button");

// Select the form
var form = d3.select("#form");

// Create event handlers 
button.on("click", runEnter);
form.on("submit",runEnter);

// Complete the event handler function for the form
function runEnter() {

  // Prevent the page from refreshing
  d3.event.preventDefault();
  
  // Select the input element and get the raw HTML node
  var inputElement = d3.select("#mars-form-input");

  // Get the value property of the input element
  var inputValue = inputElement.property("value");

  console.log(inputValue);
  console.log(soles);

  var filteredData = mars_data.filter(mars_data => mars_data.id === inputValue);

  console.log(filteredData);

  // create an array with just the pressure values
  var pressures = filteredData.map(mars_data => mars_data.pressure);

  // Next, use math.js to calculate the mean, median, mode, var, and std of the pressure
  var mean = math.mean(pressures);
  var median = math.median(pressures);
  var mode = math.mode(pressures);
  var variance = math.var(pressures);
  var standardDeviation = math.std(pressures);

  // Then, select the unordered list element by class name
  var list = d3.select(".summary");

  // append stats to the list
  list.append("li").text(`Mean: ${mean}`);
  list.append("li").text(`Median: ${median}`);
  list.append("li").text(`Mode: ${mode}`);
  list.append("li").text(`Variance: ${variance}`);
  list.append("li").text(`Standard Deviation: ${standardDeviation}`);
};
