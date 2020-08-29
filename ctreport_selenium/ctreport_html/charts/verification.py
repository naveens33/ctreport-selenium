from ctreport_selenium.utility_classes import Severity
def chart(theme, count):
    label = [Severity.BLOCKER.capitalize(), Severity.CRITICAL.capitalize(), Severity.MAJOR.capitalize(),
             Severity.MINOR.capitalize()]
    legend_labels = '''
                    labels: {
    					fontColor:'#fff'
    				}
    				''' if theme == "Dark Angel" else ""
    xAxis_gridlines = '''
        					gridLines: {
        					  color: "rgba(176, 92, 94,0.5)",
        					}''' if theme == "Dark Angel" else ""
    yAxis_gridlines = '''
                            gridLines: {
        					  color: "rgba(176, 92, 94,0.5)",
        					}''' if theme == "Dark Angel" else ""
    content = '''
            new Chart(document.getElementById("verificationchart"), {
            type: 'bar',
            data: {
              labels: '''+ str(label) + ''',
              datasets: [
                {
                  label: "Passed",
                  backgroundColor: "#00AF00",
                  data: ''' + str(count[0]) + '''
                }, {
                  label: "Failed",
                  backgroundColor: "#F7464A",
                  data: ''' + str(count[1]) + '''
                }
              ]},
            options: {
              title: {
                fontSize:20,
                display: false,
                text: 'Group Verification under Severity'
              },
              legend: {
                position:'bottom',
                '''+legend_labels+'''
              },
              scales: {
                xAxes: [{
                    barThickness : 40,
                    barPercentage: 19,	
                    '''+xAxis_gridlines+'''		
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
