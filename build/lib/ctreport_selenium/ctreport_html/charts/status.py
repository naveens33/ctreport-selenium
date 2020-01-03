def chart(status):
    content='''
        var statuschart=new Chart(document.getElementById("statuschart"), {
            type: 'doughnut',
            data: {
                labels: ["Passed", "Failed", "Skipped","Broken"],
                datasets: [{
                    label: "Population (millions)",
                    backgroundColor: ["#00AF00", "#F7464A","#1E90FF","#aaa"],
                      data: ['''+str(status[0])+''','''+str(status[1])+''','''+ \
            str(status[2])+''','''+str(status[3])+''']
                }]	
            },
            options: {
                responsive: true,
                cutoutPercentage: 80,
                title: {
                    display: false,
                    text: 'Status'
                  },
                legend: {
                    position:'right',
                },
                onClick:function(e){
                    try {
                        var dict = {
                          0: "passed",
                          1: "failed",
                          2: "skipped",
                          3: "broken",
                        };
                        var activePoints = statuschart.getElementsAtEvent(e);
                        var selectedIndex = activePoints[0]._index;
                        var status=selectedIndex;
                        console.log(status);
                        display_other_page();
                        filterSelection(dict[status]);
                        toast_message(dict[status]);
                    }
                    catch(err) {}
                }
            },
        });
    '''
    return content
