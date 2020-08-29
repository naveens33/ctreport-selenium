from ctreport_selenium.utility_classes import Severity


def chart(theme, count):
    pass_ = str(count[0])
    fail_ = str(count[1])
    label = Severity.BLOCKER.capitalize()
    legend_labels = '''
                labels: {
					fontColor:'#fff'
				}
				''' if theme == "Dark Angel" else ""
    xAxis_ticks_gridlines = '''ticks: {
                            fontColor: '#fff'
                        },
    					gridLines: {
    					  color: "rgba(176, 92, 94,0.5)",
    					}''' if theme == "Dark Angel" else ""
    yAxis_gridlines = '''
                        gridLines: {
    					  color: "rgba(176, 92, 94,0.5)",
    					}''' if theme == "Dark Angel" else ""
    content = '''
        new Chart(document.getElementById("assertionchart"), {
        type: 'bar',
        data: {
          labels: ["''' + label + '''"],
          datasets: [
            {
              label: "Passed",
              backgroundColor: "#00AF00",
              data: [''' + str(pass_) + ''']
            }, {
              label: "Failed",
              backgroundColor: "#F7464A",
              data: [''' + str(fail_) + ''']
            }
          ]},
        options: {
          title: {
            fontSize:20,
            display: false,
            text: 'Group Assertion under Severity'
          },
          legend: {
            position:'bottom',
            '''+legend_labels+'''
          },
          scales: {
            xAxes: [{
                barThickness : 40,
                barPercentage: 19,	
                '''+xAxis_ticks_gridlines+'''		
            }],
            yAxes: [{
                display: true,
                ticks: {
                    display: false,
                    maxTicksLimit: 6,
                    precision:0,
				},
				'''+yAxis_gridlines+'''
            }],
          }
        }
    });
    '''
    return content
