function getData6(){
    console.log("getting data from graph6")
    $.ajax({
      type:"GET",
      url: "http://158.108.182.2:3000/get_graph6",
      success: (data) => {graphData6(data), console.log(data)},
      contentType: "application/json",
      dataType: "json"
    })
  }

  function graphData6(data){
    var dataPoint6 = [];
    var numloop = Object.keys(data).length;
    for (var i = 0; i < numloop; i++) {
      dataPoint6.push({
        label: String(Object.keys(data)[i]),
        y: parseInt(Object.values(data)[i])
      });
    }
    console.log(dataPoint6)
    var chart6 = new CanvasJS.Chart("chartContainer6", {
      animationEnabled: true,
      theme: "light2",
      title: {
        text: "Number of customers most preferred shop catagories"
      },
      axisY: {
        title: "Number of People",
        titleFontSize: 24,
        includeZero: true
      },
        axisX: {
        title: "Shop Catagories",
        titleFontSize: 24
      },
      data: [{
        type: "column",
        yValueFormatString: "People",
        dataPoints: dataPoint6
      }]
    });
  chart6.render();
}