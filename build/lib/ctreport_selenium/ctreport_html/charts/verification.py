from ctreport_selenium.utility_classes import Severity
def chart(count):
    label=[Severity.BLOCKER,Severity.CRITICAL,Severity.MAJOR,Severity.MINOR]
    content = '''
            new Chart(document.getElementById("verificationchart"), {
            type: 'bar',
            data: {
              labels: ["High", "Medium", "Low"],
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
                text: 'Group under Priority'
              },
              legend: {
                position:'bottom'
              },
              scales: {
                xAxes: [{
                    barThickness : 40,
                    barPercentage: 19,			
                }],
                yAxes: [{
                    display: true,
                    ticks: {
                        display: false,
                        maxTicksLimit: 6,
                        precision:0,
    				}
                }],
              }
            }
        });
        '''
    return content
