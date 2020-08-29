from ctreport_selenium.utility_classes import Status, Priority


def chart(theme, tests):
    pass_ = [0, 0, 0]
    fail_ = [0, 0, 0]
    skip_ = [0, 0, 0]
    broken_ = [0, 0, 0]
    for test in tests:
        if test._result == Status.PASS:
            if test._priority == Priority.HIGH:
                pass_[0] += 1
            elif test._priority == Priority.MEDIUM:
                pass_[1] += 1
            else:
                pass_[2] += 1
        elif test._result == Status.FAIL:
            if test._priority == Priority.HIGH:
                fail_[0] += 1
            elif test._priority == Priority.MEDIUM:
                fail_[1] += 1
            else:
                fail_[2] += 1
        elif test._result == Status.SKIP:
            if test._priority == Priority.HIGH:
                skip_[0] += 1
            elif test._priority == Priority.MEDIUM:
                skip_[1] += 1
            else:
                skip_[2] += 1
        else:
            if test._priority == Priority.HIGH:
                broken_[0] += 1
            elif test._priority == Priority.MEDIUM:
                broken_[1] += 1
            else:
                broken_[2] += 1
    label = "labels: {fontColor:'#fff'}" if theme == "Dark Angel" else ""
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
        var prioritychart=new Chart(document.getElementById("prioritychart"), {
        type: 'bar',
        data: {
            labels: ["High", "Medium", "Low"],
            datasets: [{
                label: "Passed",
                backgroundColor: "#00AF00",
                data: ''' + str(pass_) + '''
            }, {
                label: "Failed",
                backgroundColor: "#F7464A",
                data: ''' + str(fail_) + '''
            },{
                label: "Skipped",
                backgroundColor: "#1E90FF",
                data: ''' + str(skip_) + '''
            },{
                label: "Broken",
                backgroundColor: "#aaa",
                data: ''' + str(broken_) + '''
            }
            ]
        },
        options: {
            title: {
                fontSize:20,
                display: false,
                text: 'Group under Priority'
            },
            legend: {
                position:'bottom',
                '''+label+'''
            },
            scales: {
                xAxes: [{
                    barThickness : 25,
                    barPercentage: 169,
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
