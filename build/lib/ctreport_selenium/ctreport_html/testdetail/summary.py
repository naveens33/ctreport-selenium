from ctreport_selenium.ctreport_html.properties import status, priority, info_
from ctreport_selenium.utility_classes import Status

def search_filter(status_):
    c='''
    <div style="display:flex">
        <input type="text" id="myInput" onkeyup="myFunction()" placeholder="Search by #id or name..." style="font-size:15px; max-height:32px; max-width:100%; width:300px">
        <div id="myBtnContainer" style="text-align: right; padding: 3px 0px 0px 40px;">
            <span class="font-weight-normal small" style="padding-right:15px">Filter By:</span>
            <i class="fa fa-sync-alt pointer" style="font-size: 18px; color:#696969" onclick="filterSelection('all')" data-toggle="tooltip" data-placement="top" title="Show all({})"></i>
            <i class="{} passicon pointer" style="{}" onclick="filterSelection('passed')" data-toggle="tooltip" data-placement="top" title="Passed({})"></i>
            <i class="{} failicon pointer" style="{}" onclick="filterSelection('failed')" data-toggle="tooltip" data-placement="top" title="Failed({})"></i>
            <i class="{} skipicon pointer" style="{}" onclick="filterSelection('skipped')" data-toggle="tooltip" data-placement="top" title="Skipped({})"></i>
            <i class="{} brokenicon pointer" style="{}" onclick="filterSelection('broken')" data-toggle="tooltip" data-placement="top" title="Broken({})"></i>
        </div>
    </div>
    '''.format(status_[4],status[Status.PASS][0],status[Status.PASS][1],status_[0],status[Status.FAIL][0],status[Status.FAIL][1],status_[1],
               status[Status.SKIP][0],status[Status.SKIP][1],status_[2],status[Status.BROKEN][0],status[Status.BROKEN][1],status_[3])
    return c

def summary_table(tests):
    tr = ''''''
    for test in tests:
        tr += '''
            <tr class="filterDiv {} border-bottom" onclick="window.location='#{}'">
                <td class="align-middle text-sm-center">
                    <i class="{}" style="{}"></i>
                </td>
                <td class="align-middle text-sm-center">
                    <i class="{}" style="{}"></i>
                    <span style="display: none">High</span>
                </td>
                <td class="align-middle text-sm-center">
                <span>{}</span>
                </td>
                <td class="align-middle">
                    <span>{}</span>
                    </td>
            </tr>
        '''.format(test._result,test._id,status[test._result][0], status[test._result][1], priority[test._priority][0],
                   priority[test._priority][1], test._id, test._name)
    c='''
        <table class="table table-borderless table-hover " style="font-size: 15px;">
        <thead>
          <tr class="text-sm-center border-bottom">
            <th>
                Status
                <i class="{} small pointer " onclick="expandFooter('info')"></i>
            </th>
            <th>
                Priority
                <i class="{} small pointer" onclick="expandFooter('info')"></i>
            </th>
            <th>ID</th>
            <th>Summary</th>
          </tr>
        </thead>
        <tbody id="search1">											
            {}
        </tbody>
    </table>
    '''.format(info_["class"],info_["class"],tr)
    return c

def content(status, tests):
    c = '''
    <!--Summary table-->
    <div class="col-sm-12 col-lg-5">
        <nav class=" p-2 test_details p-md-4">
            '''+search_filter(status)+'''
            '''+summary_table(tests)+'''
        </nav>
    </div>
    '''
    return c