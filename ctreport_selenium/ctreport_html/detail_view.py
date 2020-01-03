from ctreport_selenium.ctreport_html.testdetail import summary,details

def content(status, tests):
    c = '''
        <div id="test-view" class="wrapper" style="display: none;">
        <div class="container-fluid">
            <section class="pading">
                <div class="row  mt-3">
                    <!--test summary-->
                    ''' + summary.content(status, tests) + '''
                    <!-- test details-->
                    ''' + details.content(tests) + '''
                </div>
            </section>
        </div>
    </div>
    '''
    return c