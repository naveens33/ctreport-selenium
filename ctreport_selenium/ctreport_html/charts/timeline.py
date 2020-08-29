def chart(theme, tests):
    id_name_dict = {}
    min_li = []
    for test in tests:
        id_name_dict[test._id] = test._name
        duration = test._duration.split(':')
        hour = float(duration[0])
        min = float(duration[1])
        sec = float(duration[2]) + min * 60 + hour * 60 * 60
        min_li.append(sec)
    backgroundColor = "rgba(95, 164, 186,0.5)" if theme == "Dark Angel" else "rgba(188, 216, 249,0.4)"
    borderColor = "#e8f2fd" if theme == "Dark Angel" else "rgb(188, 216, 249)"
    pointBorderColor =  "#ffffff" if theme == "Dark Angel" else "#000000"
    scales = '''scales: {
        yAxes: [{
            ticks: {
                fontColor: '#fff'
            },
            gridLines: {
                color: "rgba(176, 92, 94,0.5)",
            }
        }],
        xAxes: [{
            ticks: {
                fontColor: '#fff'
            },
            gridLines: {
                color: "rgba(176, 92, 94,0.5)",
            }
        }]
    },''' if theme == "Dark Angel" else ""
    content = '''
        var dict= ''' + str(id_name_dict) + '''
        var timelinechart = new Chart(document.getElementById("timelinechart"), {
            type: 'line',
            data: {
                labels: ''' + str(list(id_name_dict.keys())) + ''',
                datasets: [
                    {
                        backgroundColor:"'''+backgroundColor+'''",
                        borderColor:"'''+borderColor+'''",
                        pointBackgroundColor: "rgba(188, 216, 249,0.6)",
                        pointBorderColor: "'''+pointBorderColor+'''",
                        pointStyle:"crossRot",
                        showLine:true,
                        data: ''' + str(min_li) + ''',
                        lineTension:0,
                    },
                ]
            },
            options: {
                legend: {
                    display: false
                },
                '''+scales+'''
                tooltips: {
                    callbacks: {
                        label: function(tooltipItem, data) {
                            var label ='';
                            label += Math.round(tooltipItem.yLabel * 100) / 100;
                            label +=' sec';
                            return label;
                        },
                        title: function(tooltipItem, data) {
                            var title ='';
                            title += dict[tooltipItem[0].xLabel];
                            return title;
                        }
                    }
                },
                onClick: function(evt,i) {
                    var activePoint = timelinechart.getElementAtEvent(evt)[0];
                    var data = activePoint._chart.data;
                    var datasetIndex = activePoint._datasetIndex;
                    var value = this.data.datasets[datasetIndex].data[activePoint._index];
                    e = i[0];
                    var id = this.data.labels[e._index];
                    console.log(id);
                    display_other_page();
                    filterSelection("all");
                    document.getElementById(id).scrollIntoView();
                }
            },
            
        });
    '''
    return content
